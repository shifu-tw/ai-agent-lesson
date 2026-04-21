# AI Agent 家教課設計文件

> 日期：2026-04-21
> 對象：Joey（ShiFu CEO，創業家，用過 ChatGPT 但沒用過 Claude Code）
> 時長：2 小時
> 設備：Mac，已有 Claude Pro 訂閱 + Claude Code Desktop App
> 目標：理解 AI Agent 架構設計 + 帶走一個能用的核心

---

## 第一性原理

Joey 是 CEO，最稀缺的資源是注意力。

他需要的只有一件事：**一個越用越懂他的對話夥伴。**

這件事需要三樣東西：
1. **認識他** → CLAUDE.md
2. **記得住** → MEMORY.md
3. **會長大** → 進化規則

其他所有東西都是這三件事的延伸。

---

## 核心概念：Context Window 管理

**所有設計決策的底層邏輯。**

- AI 每次對話有工作記憶上限
- 就算 100 萬 token，塞越滿越笨 — 關鍵資訊被雜訊淹沒
- **Context 污染**：塞不相關的東西 = 稀釋 AI 注意力

| 設計 | Context 策略 |
|------|-------------|
| CLAUDE.md | 每次自動載入。只放最精煉的身份資訊。 |
| MEMORY.md | 只載入相關記憶，不全塞。 |
| vault/ 知識庫 | 按需搜尋，不預載。 |
| skills/ | 觸發時才載入。 |
| CLI 工具 | 程式跑，只把結果餵 AI。零 token。 |
| ChatGPT 匯入 | 程式壓縮後只把摘要給 AI。 |

### Context 管理 Best Practice

- **不同任務開不同對話** — 上下文互相污染
- **兩段式工作法** — 第一輪討論 → 產出文件。第二輪拿文件當指令執行。
- **長對話會衰退** — 聊越久品質越差。重要任務開新對話。
- **CLAUDE.md 要精煉** — 每次都載入，太囉唆浪費 context
- **Agent-centric 寫法** — 寫給 AI 讀，結構清晰、規則明確、不要客氣話
- **Checkpoint 可回滾** — 做錯隨時退回上一步
- **.env 不要貼** — API key、密碼、token 不直接貼進對話

---

## 同心圓架構

```
        ┌─────────────────────────┐
        │   自動化（穩定後開）       │
        │   排程・沉澱・事件觸發    │
        │  ┌───────────────────┐  │
        │  │  擴展（用到時加）    │  │
        │  │  vault・skills・CLI │  │
        │  │  ┌─────────────┐  │  │
        │  │  │   核心        │  │  │
        │  │  │  CLAUDE.md   │  │  │
        │  │  │  MEMORY.md   │  │  │
        │  │  │  進化規則     │  │  │
        │  │  └─────────────┘  │  │
        │  └───────────────────┘  │
        └─────────────────────────┘
```

---

## 為什麼是 Claude Code CLI

Claude Code 是唯一能直接跑 CLI 指令的介面。Chat 和 Cowork 做不到。

### CLI vs MCP

| | CLI | MCP |
|--|-----|-----|
| 本質 | 程式直接執行，結果給 AI | AI 透過協議呼叫外部服務 |
| Token | 零 | 每次消耗 |
| 上手 | 一行指令 | 裝 server + 設定 |
| 透明度 | 看得到在幹嘛 | 黑盒 |
| 維護 | 零 | server 要更新 |

**CLI 先行，MCP 備用。** 兩者不衝突。

---

## 進化機制

### 重複偵測（講三次就學會）
同類要求 ≥3 次 → Agent 主動問「要不要建成 Skill？」→ 你同意 → 自動生成 SKILL.md

### 糾正學習
被糾正 → 更新 MEMORY.md → 不再犯

### 品質棘輪（達爾文機制）
更新 Skill 前比對新舊版本。變差就不改。

### 沉澱機制（簡化版 OpenClaw 做夢）
每週自動：掃記憶 → 掃知識庫 → 找模式 → 產出沉澱日誌 → 你批准才改

### 安全閥
修改 CLAUDE.md 或 Skill 前，先給你看建議。你批准才改。

---

## Skill 生態

### Skill 的本質
一份 SKILL.md = 寫給 AI 讀的 SOP。觸發時才載入，不佔 context。

### 預建 Skill

| Skill | 功能 |
|-------|------|
| insight-finder | 丟素材 → 整理脈絡 → 標關鍵訊號 → 挖隱藏洞察 |
| content-drafter | 給主題 → 用你的口吻起草內容 |
| git-sync | `/commit` 快速 git add + commit + push |

### Skill 生態系（參考）

| 專案 | 功能 |
|------|------|
| 女媧.skill | 蒸餾名人思維框架（芒格、Naval、Jobs 等 13 位） |
| 同事.skill | 蒸餾真實的人成 AI Skill |
| 達爾文.skill | Skill 自動進化（8 維評估 + 棘輪機制） |

---

## ChatGPT 匯入機制

程式先壓縮，AI 最後分類。

```
匯出 JSON → 程式解析（0 token）→ 統計摘要 → AI 分類（1 次 token）
```

程式做：統計對話數、抓高頻關鍵詞、取樣最長訊息、推斷使用模式
AI 做：讀壓縮後的摘要，判斷興趣領域和偏好，分類到 vault/

---

## 外部串接

### Google Workspace CLI (gws)
一個工具打通 40+ Google API：Gmail、Calendar、Drive、Sheets、Docs

### GitHub CLI (gh)
版本控制、備份、repo 管理

### better-rm
安全刪除。Agent 刪檔案移到垃圾桶，不會真刪。

---

## Git 備份

### 手動（課堂先用）
跟 Agent 說「幫我 commit 並 push」

### Skill（/commit）
`skills/git-sync/SKILL.md` — 一個指令完成 add + commit message + push

### Hook 自動化（進階）
PostToolUse 或定時自動 commit + push

---

## 安裝包結構

```
[joey-names-this]/
├── CLAUDE.md              ← 身份（每次自動載入）
├── MEMORY.md              ← 記憶（自動累積）
├── vault/                 ← 知識庫（按需搜尋）
│   ├── company/
│   ├── industry/
│   ├── meetings/
│   └── personal/
├── skills/                ← 專長（觸發才載入）
│   ├── insight-finder/
│   ├── content-drafter/
│   └── git-sync/
├── routines/              ← 排程（穩定後開）
│   ├── daily-briefing.md
│   └── weekly-evolution.md
├── guides/                ← 引導 prompt（雙層結構）
│   ├── 01-setup.md
│   ├── 02-onboarding.md
│   ├── 03-import-chatgpt.md
│   ├── 04-vault.md
│   ├── 05-skills.md
│   ├── 06-routines.md
│   └── 07-update-identity.md
├── tools/                 ← 程式工具
│   └── parse-chatgpt-export.py
├── milestones/            ← 進度追蹤
│   ├── week-1.md
│   └── review-template.md
└── references/            ← 知識後盾（連結索引）
    └── README.md
```

### 引導機制（雷蒙模式）

每份 guides/ 文件是雙層結構：
- 上半：給人看的說明
- 下半（`<!-- 以下是給 Claude 讀的執行指令 -->`）：給 AI 執行

關鍵設計模式：
- AskUserQuestion 收集輸入（選擇題 + 開放題）
- 不跳過任何 Section
- Append 不 Overwrite
- 完成後 grep 檢查 placeholder
- 狀態偵測：已存在的設定不重複建

### 資料夾位置

推薦放 iCloud（多裝置同步）：
```
~/Library/Mobile Documents/com~apple~CloudDocs/[名字]
```
或 Documents（單機穩定）：
```
~/Documents/[名字]
```

---

## 環境安裝

課堂一開始先跑（背景裝 Homebrew，15-20 min）：
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Homebrew 好後：
```bash
brew install gh
brew install googleworkspace-cli
curl -sSL https://raw.githubusercontent.com/doggy8088/better-rm/main/install.sh | bash
gh auth login
gws auth login -s gmail,calendar,drive
```

---

## 課程流程（2 小時）

### Part 0：環境設定 + 開場（10 min）
- S00: 封面
- S01: 貼 Homebrew 安裝指令（背景跑）+ 工具說明
- S02: AI Agent 現在能做什麼 + 限制 + 品質跟框架有關

### Part 1：設計原理（20 min）
- S03: 不是工具是夥伴
- S04: Context Window + 污染
- S05: 三層設計
- S06: Context Best Practice
- S07: 不做的後果
- S08: Claude Code + CLI vs MCP
- S09: 安裝包 MD 結構設計

### Part 2：建造（45 min）
- S10: 裝工具 + 認證（Homebrew 應該好了）
- S11: 匯入 ChatGPT
- S12: Onboarding → CLAUDE.md + git init + private repo
- S13: 記憶 + 進化規則 + Permission mode
- S14: 裝 Skill

### Part 3：實戰（25 min）
- S15: 讀信 + 行事曆 → 今天重點
- S16: 挖 Insight + 芒格模式
- S17: 起草內容 + 糾正示範

### Part 4：帶走（10 min）
- S18: 作業（用爆它）
- S19: 驗收標準

### Part 5：深入（10 min，彈性）
- S20: Skill 的本質
- S21-23: 女媧 / 同事 / 達爾文 展開
- S24: 雷蒙 Skill 結構對比
- S25-26: 雷蒙架構 / Vault 架構
- S27: 預覽未來
- S28: 結語

---

## 第一週：用爆它

唯一規則：**本來就在做的事，全部先問它。**

### 驗收標準
- MEMORY.md ≥ 15 條
- vault/ ≥ 5 份文件
- 起草 3+ 內容、整理 3+ 會議
- gws 至少用 10 次
- 問「你了解我什麼？」準確 ≥ 10 點
- 寫的東西 60%+ 不用大改
- 糾正 3+ 次且沒再犯
- 能說出「它最懂我的一件事」

一週後跟 Agent 說「跑 review」。下次上課看結果。

---

## 參考資料

| 資料 | 取用的概念 |
|------|----------|
| Vault for Founders | 知識庫結構、Agent-centric 寫法、引導式建立、夥伴 framing |
| 雷蒙迷你課 | 雙層引導文件、AskUserQuestion、安裝包結構、iCloud 同步 |
| OpenClaw | 做夢/沉澱機制 |
| 女媧.skill + 達爾文.skill | Skill 品質棘輪、自動進化、蒸餾方法論 |
| 同事.skill | 蒸餾真實的人 |
| Hermes Agent | 複雜任務後自動存 Skill、糾正學習 |
| Claude Code Docs | Routines、Memory、Skills、Hooks、Channels、Permission Modes |
| GWS CLI | Google Workspace 統一 CLI |
| Karpathy LLM Wiki | LLM 運作原理與限制 |
| AI Agent 工作術 | AI Agent 教學參考、CLI vs MCP vs API 概念 |
| better-rm | 安全刪除 |
