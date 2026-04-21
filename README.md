# AI Agent 家教課

2 小時 Private Lesson，教創業家從零建造一個越用越懂你的 AI 夥伴。

## 課程對象

- 已用過 ChatGPT/Claude 但沒用過 Claude Code CLI
- 需要 AI 幫忙整理脈絡、挖 insight、起草內容
- 不需要寫程式，但要理解架構設計

## 專案結構

```
├── kit/                  ← 安裝包（上課時 Joey 帶走的東西）
│   ├── guides/           ← 引導式安裝 prompt（雙層結構）
│   ├── skills/           ← 預建 Skill
│   ├── routines/         ← 排程範例
│   ├── tools/            ← 程式工具（ChatGPT 解析器）
│   ├── vault/            ← 知識庫結構
│   └── milestones/       ← 第一週任務 + 驗收
├── presentation/         ← 簡報
│   ├── slides-content.md ← 內容結構（餵 Claude Design 用）
│   └── index.html        ← 簡報網頁（待改淺色版）
├── references/           ← 參考資料連結索引（不含實際檔案）
├── docs/plans/           ← 課程設計文件
└── tools/                ← 開發用工具
```

## 課程架構

```
Part 0 — 環境設定（背景裝 Homebrew）
Part 1 — 設計原理（Context Window、三層架構、Best Practice）
Part 2 — 建造（安裝、匯入 ChatGPT、Onboarding、記憶、Skill）
Part 3 — 實戰（讀信、挖 Insight、起草內容）
Part 4 — 帶走（作業 + 驗收）
Part 5 — 深入（Skill 展開、參考架構）
```

## 安裝包核心設計

所有設計圍繞 Context Window 管理：

| 元件 | Context 策略 |
|------|-------------|
| CLAUDE.md | 每次自動載入，精煉 |
| MEMORY.md | 只載入相關記憶 |
| vault/ | 按需搜尋，不預載 |
| skills/ | 觸發時才載入 |
| CLI 工具 | 程式跑，零 token |

## 參考資料

見 [references/README.md](references/README.md) 的完整連結列表。

## 需要的工具

- Claude Code Desktop App（已有 Claude Pro 訂閱）
- Homebrew → gh, gws, better-rm
- GitHub 帳號
- Google 帳號（GWS CLI 認證用）
