# AI 夥伴安裝包

這是你的 AI 夥伴的完整框架。所有設計都圍繞一個原則：

**讓 AI 有限的工作記憶裡，永遠放著最重要的東西。**

## 快速開始

1. 跟 Agent 說：**「讀 guides/01-setup.md 然後幫我跑安裝」**
2. 安裝完後說：**「讀 guides/03-import-chatgpt.md 幫我匯入」**（如果有 ChatGPT 匯出檔）
3. 然後說：**「讀 guides/02-onboarding.md 然後幫我跑 onboarding」**
4. 跑完就有一個認識你的 AI 夥伴了

## 架構

```
核心（今天建好）
  CLAUDE.md    — 身份。每次對話自動載入。精煉。
  MEMORY.md    — 記憶。只載入相關的。自動累積。
  進化規則      — 寫在 CLAUDE.md 裡。讓它自己變好。

擴展（用到時加）
  vault/       — 知識庫。按需搜尋，不預載。
  skills/      — 專長。觸發時才載入。
  CLI 串接     — 程式取資料，零 token。

自動化（穩定後開）
  routines/    — 排程。每日晨報、每週沉澱。
```

## 資料夾說明

| 資料夾 | 用途 | Context 策略 |
|--------|------|-------------|
| `vault/` | 知識庫（公司/產業/會議/個人） | 按需搜尋，不預載 |
| `skills/` | 可重複用的 SOP | 觸發時才載入 |
| `routines/` | 排程任務 | 獨立執行 |
| `guides/` | 建造引導（雙層結構） | 用完可不管 |
| `tools/` | 程式工具 | 程式跑，零 token |
| `milestones/` | 進度追蹤 + 驗收 | 需要時查 |
| `references/` | 深入知識連結 | Agent 搜尋用 |

## 預建 Skill

| Skill | 觸發 | 功能 |
|-------|------|------|
| `insight-finder` | 「找 insight」「分析一下」 | 整理脈絡 → 標關鍵訊號 → 挖隱藏洞察 |
| `content-drafter` | 「幫我寫」「起草」 | 用你的口吻和思維方式起草內容 |
| `git-sync` | `/commit`「同步」「備份」 | git add → AI 生成 commit message → push |

## 進化邏輯

```
日常對話 → 記憶自動累積
         → 發現重複需求（≥3 次）→ 建議建 Skill
         → 被糾正 → 記住不再犯
         → 每週沉澱 → 建議更新身份/Skill
         → 你批准 → 系統升級
         → 繼續對話（越來越懂你）
```

## Context 管理提醒

- 不同任務開不同對話
- 長對話品質會衰退，重要任務開新的
- 兩段式：先討論產出文件，再開新對話照文件執行
- CLAUDE.md 要精煉（每次都載入）
- .env / API key / 密碼不要貼進對話

## 備份

說 `/commit` 或「備份」就會自動 git commit + push 到你的 private repo。

## 安裝的工具

| 工具 | 為什麼 |
|------|--------|
| gh | GitHub CLI。版本控制 + 備份。 |
| gws | Google Workspace CLI。讀信/行事曆/Drive。 |
| better-rm | 安全刪除。Agent 刪檔案移到垃圾桶。 |

## 參考資料

見 `references/README.md` 的完整連結列表。
