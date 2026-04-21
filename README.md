# AI Agent 家教課

2 小時 Private Lesson，教創業家從零建造一個越用越懂你的 AI 夥伴。

## 使用者安裝

在 Claude Code Desktop 裡說：

> 讀 https://github.com/shifu-tw/ai-agent-lesson/raw/main/install.md 然後幫我建一個 AI 夥伴

Agent 會自動完成所有設定。使用者不需要碰 terminal。

## 專案結構

```
├── install.md              ← Agent 讀的安裝劇本（核心文件）
├── templates/              ← 模板（Agent 讀取後生成成品）
│   └── CLAUDE.md.template
├── skills/                 ← 預建 Skill（複製到成品）
├── routines/               ← 排程範例（Phase 3 複製）
├── guides/                 ← Phase 2/3 引導（複製到成品）
├── tools/                  ← 程式工具（複製到成品）
├── milestones/             ← 進度追蹤（複製到成品）
├── references/             ← 進化教科書（連結索引）
├── presentation/           ← 簡報
└── docs/plans/             ← 設計文件
```

## 使用者電腦上的成品

```
[使用者取名]/              ← iCloud 或 Documents
├── CLAUDE.md              ← 根據訪談生成（50 行精煉版）
├── MEMORY.md              ← 記憶（自動累積）
├── vault/                 ← 知識庫（按需搜尋）
├── skills/                ← Skill（symlink 到 ~/.claude/skills）
├── guides/                ← Phase 2/3 引導（成長觸發自動建議）
├── routines/              ← 排程範例
├── tools/                 ← 程式工具
├── milestones/            ← 進度追蹤
└── references/            ← 進化教科書連結
```

## 設計原則

1. **Context Window 管理** — 所有設計讓 AI 有限的工作記憶裡放最重要的東西
2. **零手動觸發** — Phase 1 偵測新使用者自動跑，Phase 2/3 成長觸發自動建議
3. **漸進式** — 陽春版 → 用出來 → 全能版
4. **references 是進化教科書** — Agent 升級時的方法論來源，不是搜尋資料庫

## 課程架構

```
Part 0 — 環境設定（背景裝 Homebrew）
Part 1 — 設計原理（Context、架構、Best Practice）
Part 2 — 建造（Agent 自動跑 install.md）
Part 3 — 實戰（讀信、挖 Insight、起草）
Part 4 — 帶走（作業 + 驗收）
Part 5 — 深入（Skill 展開、參考架構）
```
