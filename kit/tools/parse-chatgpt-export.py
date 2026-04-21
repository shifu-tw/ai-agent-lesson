#!/usr/bin/env python3
"""
ChatGPT 匯出資料解析器
=====================
用途：解析 ChatGPT 匯出的 conversations.json，
      用純程式預處理（不燒 token），產出結構化摘要，
      再用一次 AI prompt 分類到 vault/。

使用方式：
  python3 parse-chatgpt-export.py /path/to/conversations.json --output ./vault

它會產出：
  1. vault/chatgpt-import/raw-summary.md     — 純程式產出的統計摘要
  2. vault/chatgpt-import/topics/             — 按主題分類的對話摘要
  3. vault/chatgpt-import/user-profile.md     — 從對話模式推斷的使用者輪廓
  4. vault/chatgpt-import/classify-prompt.md  — 餵給 AI 做最終分類的 prompt
"""

import json
import sys
import os
import re
import zipfile
import tempfile
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
import argparse


def load_conversations(path: str) -> list:
    """載入 conversations.json，支援直接 JSON 或 ZIP 檔"""
    p = Path(path)

    if p.suffix == '.zip':
        with zipfile.ZipFile(p) as zf:
            for name in zf.namelist():
                if name.endswith('conversations.json'):
                    with zf.open(name) as f:
                        return json.load(f)
        raise FileNotFoundError("ZIP 裡找不到 conversations.json")

    with open(p, 'r', encoding='utf-8') as f:
        return json.load(f)


def extract_messages(conv: dict) -> list[dict]:
    """從一個對話中提取所有訊息，按時間排序"""
    messages = []
    mapping = conv.get('mapping', {})

    for node in mapping.values():
        msg = node.get('message')
        if not msg:
            continue
        content = msg.get('content', {})
        parts = content.get('parts', [])
        text = ''
        for part in parts:
            if isinstance(part, str):
                text += part
        if not text.strip():
            continue
        messages.append({
            'role': msg.get('author', {}).get('role', 'unknown'),
            'text': text.strip(),
            'time': msg.get('create_time'),
        })

    messages.sort(key=lambda m: m.get('time') or 0)
    return messages


def analyze_conversations(convs: list) -> dict:
    """純程式分析，不用 AI，不燒 token"""

    stats = {
        'total_conversations': len(convs),
        'total_user_messages': 0,
        'total_assistant_messages': 0,
        'date_range': {'earliest': None, 'latest': None},
        'monthly_activity': Counter(),
        'topics_by_title': [],
        'user_message_lengths': [],
        'frequent_phrases': Counter(),
        'question_patterns': Counter(),
        'user_messages_sample': [],  # 取樣，不全放
        'conversations_by_month': defaultdict(list),
    }

    all_user_texts = []

    for conv in convs:
        title = conv.get('title', '(untitled)')
        create_time = conv.get('create_time')
        messages = extract_messages(conv)

        user_msgs = [m for m in messages if m['role'] == 'user']
        asst_msgs = [m for m in messages if m['role'] == 'assistant']

        stats['total_user_messages'] += len(user_msgs)
        stats['total_assistant_messages'] += len(asst_msgs)

        if create_time:
            dt = datetime.fromtimestamp(create_time, tz=timezone.utc)
            month_key = dt.strftime('%Y-%m')
            stats['monthly_activity'][month_key] += 1
            stats['conversations_by_month'][month_key].append(title)

            if not stats['date_range']['earliest'] or dt.isoformat() < stats['date_range']['earliest']:
                stats['date_range']['earliest'] = dt.isoformat()
            if not stats['date_range']['latest'] or dt.isoformat() > stats['date_range']['latest']:
                stats['date_range']['latest'] = dt.isoformat()

        stats['topics_by_title'].append({
            'title': title,
            'user_msg_count': len(user_msgs),
            'total_msg_count': len(messages),
            'date': datetime.fromtimestamp(create_time, tz=timezone.utc).strftime('%Y-%m-%d') if create_time else 'unknown',
        })

        for msg in user_msgs:
            text = msg['text']
            all_user_texts.append(text)
            stats['user_message_lengths'].append(len(text))

            # 偵測問句模式
            if '?' in text or '？' in text:
                stats['question_patterns']['questions'] += 1
            if any(w in text.lower() for w in ['幫我', '請幫', 'help me', 'can you']):
                stats['question_patterns']['requests'] += 1
            if any(w in text.lower() for w in ['為什麼', 'why', '怎麼', 'how']):
                stats['question_patterns']['why_how'] += 1
            if any(w in text.lower() for w in ['比較', 'compare', '差別', 'difference', 'vs']):
                stats['question_patterns']['comparisons'] += 1

    # 高頻詞分析（簡易版，用空格分詞 + 中文 2-4 字 ngram）
    word_counter = Counter()
    for text in all_user_texts:
        # 英文詞
        words = re.findall(r'[a-zA-Z]{3,}', text.lower())
        word_counter.update(words)
        # 中文 2-4 字 ngram
        chinese_chars = re.findall(r'[\u4e00-\u9fff]+', text)
        for segment in chinese_chars:
            for n in range(2, 5):
                for i in range(len(segment) - n + 1):
                    ngram = segment[i:i+n]
                    word_counter[ngram] += 1

    # 過濾停用詞
    stopwords = {'the', 'and', 'for', 'that', 'this', 'with', 'you', 'are', 'was',
                 'have', 'has', 'not', 'but', 'can', 'will', 'from', 'they', 'been',
                 '的是', '我的', '一個', '可以', '不是', '這個', '沒有', '什麼', '他們',
                 '就是', '然後', '因為', '如果', '但是', '所以', '還是', '已經', '或者'}
    stats['frequent_phrases'] = Counter({
        k: v for k, v in word_counter.items()
        if v >= 3 and k not in stopwords and len(k) >= 2
    })

    # 取樣 user messages（最長的 50 條，代表深度對話）
    sorted_texts = sorted(all_user_texts, key=len, reverse=True)
    stats['user_messages_sample'] = sorted_texts[:50]

    # 按對話數排序 topics
    stats['topics_by_title'].sort(key=lambda t: t['user_msg_count'], reverse=True)

    return stats


def generate_raw_summary(stats: dict, output_dir: Path):
    """產出純程式統計摘要 markdown"""
    out = output_dir / 'chatgpt-import'
    out.mkdir(parents=True, exist_ok=True)

    lines = []
    lines.append('# ChatGPT 對話統計摘要\n')
    lines.append(f'> 由程式自動分析產出，不消耗 AI token\n')
    lines.append(f'## 總覽\n')
    lines.append(f'- 對話總數：{stats["total_conversations"]}')
    lines.append(f'- 你的訊息數：{stats["total_user_messages"]}')
    lines.append(f'- AI 回覆數：{stats["total_assistant_messages"]}')
    lines.append(f'- 時間範圍：{stats["date_range"]["earliest"][:10] if stats["date_range"]["earliest"] else "N/A"} ~ {stats["date_range"]["latest"][:10] if stats["date_range"]["latest"] else "N/A"}')

    avg_len = sum(stats['user_message_lengths']) / max(len(stats['user_message_lengths']), 1)
    lines.append(f'- 平均訊息長度：{avg_len:.0f} 字元')
    lines.append('')

    # 月度活躍度
    lines.append('## 月度活躍度\n')
    for month, count in sorted(stats['monthly_activity'].items()):
        bar = '#' * min(count, 50)
        lines.append(f'- {month}: {count} 次 {bar}')
    lines.append('')

    # 對話模式
    lines.append('## 對話模式\n')
    for pattern, count in stats['question_patterns'].most_common():
        label = {
            'questions': '問問題',
            'requests': '請求幫忙',
            'why_how': '問為什麼/怎麼做',
            'comparisons': '比較/分析',
        }.get(pattern, pattern)
        lines.append(f'- {label}：{count} 次')
    lines.append('')

    # 高頻主題詞
    lines.append('## 高頻關鍵詞（前 40）\n')
    for word, count in stats['frequent_phrases'].most_common(40):
        lines.append(f'- {word}: {count}')
    lines.append('')

    # 最深度的對話（按訊息數）
    lines.append('## 最深度的對話（前 30）\n')
    for topic in stats['topics_by_title'][:30]:
        lines.append(f'- [{topic["date"]}] **{topic["title"]}** ({topic["user_msg_count"]} 則你的訊息)')
    lines.append('')

    # 所有對話標題列表
    lines.append('## 所有對話標題\n')
    for topic in stats['topics_by_title']:
        lines.append(f'- [{topic["date"]}] {topic["title"]}')

    (out / 'raw-summary.md').write_text('\n'.join(lines), encoding='utf-8')
    print(f'  -> {out / "raw-summary.md"}')


def generate_user_profile_draft(stats: dict, output_dir: Path):
    """從對話模式推斷使用者輪廓草稿"""
    out = output_dir / 'chatgpt-import'

    lines = []
    lines.append('# 使用者輪廓草稿\n')
    lines.append('> 從 ChatGPT 對話模式自動推斷，需要你確認和修正\n')

    # 從高頻詞推斷興趣領域
    lines.append('## 可能的興趣/工作領域\n')
    lines.append('根據高頻關鍵詞推斷：\n')
    for word, count in stats['frequent_phrases'].most_common(20):
        lines.append(f'- {word} (出現 {count} 次)')

    lines.append('\n## 使用模式\n')
    total_q = stats['question_patterns'].get('questions', 0)
    total_r = stats['question_patterns'].get('requests', 0)
    total_w = stats['question_patterns'].get('why_how', 0)
    if total_w > total_r:
        lines.append('- 偏向探索型：常問「為什麼」和「怎麼做」，喜歡理解原理')
    elif total_r > total_w:
        lines.append('- 偏向執行型：常請 AI 幫忙做事，注重效率和結果')
    if stats['question_patterns'].get('comparisons', 0) > 5:
        lines.append('- 喜歡比較分析：常做方案比較和權衡')

    avg_len = sum(stats['user_message_lengths']) / max(len(stats['user_message_lengths']), 1)
    if avg_len > 200:
        lines.append('- 習慣給詳細的上下文和指令')
    elif avg_len < 50:
        lines.append('- 習慣簡短直接的指令')
    else:
        lines.append('- 指令長度適中')

    # 從取樣的長訊息中提取可能的偏好
    lines.append('\n## 代表性的長訊息（你表達最多的時刻）\n')
    lines.append('以下是你在 ChatGPT 中寫過最長的訊息，可能代表你最在意的議題：\n')
    for i, msg in enumerate(stats['user_messages_sample'][:10]):
        preview = msg[:200].replace('\n', ' ')
        lines.append(f'{i+1}. {preview}...\n')

    (out / 'user-profile.md').write_text('\n'.join(lines), encoding='utf-8')
    print(f'  -> {out / "user-profile.md"}')


def generate_classify_prompt(stats: dict, output_dir: Path):
    """產出一個精簡的 prompt，餵給 AI 做最終分類"""
    out = output_dir / 'chatgpt-import'

    lines = []
    lines.append('# ChatGPT 資料分類 Prompt\n')
    lines.append('> 把這份檔案貼給你的 AI 夥伴，它會幫你把資料分類到 vault/\n')
    lines.append('---\n')
    lines.append('我剛從 ChatGPT 匯出了我的對話歷史。')
    lines.append('以下是程式自動分析的摘要（不是原始對話，已經壓縮過了）。')
    lines.append('請根據這些資訊：\n')
    lines.append('1. 整理出我最常討論的 5-10 個主題領域')
    lines.append('2. 推斷我的思考風格和溝通偏好')
    lines.append('3. 找出可能的隱藏 insight（重複出現但我可能沒意識到的模式）')
    lines.append('4. 建議哪些內容該放進 vault/ 的哪個資料夾')
    lines.append('5. 有哪些值得寫進 CLAUDE.md 的偏好或原則\n')
    lines.append('**重要：不要做決定，只給我分析和建議。**\n')
    lines.append('---\n')

    # 附上壓縮過的統計資料
    lines.append('## 統計摘要\n')
    lines.append(f'- {stats["total_conversations"]} 個對話，{stats["total_user_messages"]} 則我的訊息')
    lines.append(f'- 時間：{stats["date_range"]["earliest"][:10] if stats["date_range"]["earliest"] else "N/A"} ~ {stats["date_range"]["latest"][:10] if stats["date_range"]["latest"] else "N/A"}\n')

    lines.append('## 高頻關鍵詞\n')
    for word, count in stats['frequent_phrases'].most_common(30):
        lines.append(f'- {word}: {count}')

    lines.append('\n## 最深度的對話主題（前 20）\n')
    for topic in stats['topics_by_title'][:20]:
        lines.append(f'- [{topic["date"]}] {topic["title"]} ({topic["user_msg_count"]} 則)')

    lines.append('\n## 所有對話標題\n')
    for topic in stats['topics_by_title']:
        lines.append(f'- {topic["title"]}')

    lines.append('\n## 代表性訊息摘錄\n')
    for i, msg in enumerate(stats['user_messages_sample'][:15]):
        preview = msg[:300].replace('\n', ' ')
        lines.append(f'{i+1}. {preview}\n')

    (out / 'classify-prompt.md').write_text('\n'.join(lines), encoding='utf-8')
    print(f'  -> {out / "classify-prompt.md"}')


def main():
    parser = argparse.ArgumentParser(
        description='解析 ChatGPT 匯出資料，用程式預處理，不燒 token'
    )
    parser.add_argument('input', help='conversations.json 或匯出的 .zip 檔案路徑')
    parser.add_argument('--output', '-o', default='./vault',
                        help='輸出目錄（預設: ./vault）')
    args = parser.parse_args()

    print(f'載入 {args.input}...')
    convs = load_conversations(args.input)
    print(f'  找到 {len(convs)} 個對話')

    print('分析中（純程式，不用 AI）...')
    stats = analyze_conversations(convs)

    output_dir = Path(args.output)
    print(f'產出摘要到 {output_dir}/chatgpt-import/...')

    generate_raw_summary(stats, output_dir)
    generate_user_profile_draft(stats, output_dir)
    generate_classify_prompt(stats, output_dir)

    print()
    print('完成！接下來：')
    print(f'  1. 看一下 {output_dir}/chatgpt-import/raw-summary.md（統計總覽）')
    print(f'  2. 看一下 {output_dir}/chatgpt-import/user-profile.md（使用者輪廓草稿）')
    print(f'  3. 把 {output_dir}/chatgpt-import/classify-prompt.md 貼給你的 AI 夥伴')
    print(f'     它會幫你把資料分類到 vault/ 的對應資料夾')
    print()
    print('整個過程只消耗一次 AI token（最後的分類 prompt）。')
    print('前面所有分析都是程式做的。')


if __name__ == '__main__':
    main()
