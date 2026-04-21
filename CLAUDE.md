# AI Agent 家教課

## 專案概述

2 小時 Private Lesson，教 Joey（ShiFu CEO）建造個人 AI Agent。
使用 Claude Code CLI + GWS CLI + GitHub CLI 的純 CLI 架構。

## 目錄結構

- `kit/` — 安裝包，課堂上 Joey 帶走的東西
- `kit/guides/` — 雙層結構引導（上半人讀、下半 AI 執行）
- `kit/skills/` — 預建 Skill（insight-finder, content-drafter, git-sync）
- `kit/tools/` — 程式工具（ChatGPT 匯出解析器）
- `presentation/` — 簡報（slides-content.md 是內容結構）
- `references/` — 參考資料連結索引（實際檔案在 .gitignore 中）
- `docs/plans/` — 課程設計文件

## 設計原則

1. **Context Window 管理** — 所有設計都在解決「讓 AI 有限的工作記憶裡放最重要的東西」
2. **CLI 先行** — 能用程式做的不用 AI 做，省 token
3. **漸進式** — 核心今天建，擴展用到時加，自動化穩定後開
4. **Agent-centric 寫法** — 給 AI 讀的文件：結構清晰、規則明確、不要客氣話

## 編輯慣例

- 繁體中文（台灣用語）
- guides/ 裡的文件是雙層結構：上半給人看的說明，`<!-- 以下是給 Claude 讀的執行指令 -->` 以下給 AI 執行
- Skill 格式：YAML frontmatter（name, description）+ Markdown 內容
- references/ 裡只放 README.md 連結索引，實際檔案不進 repo
