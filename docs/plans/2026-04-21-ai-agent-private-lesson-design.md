# AI Agent 家教課設計文件

> 日期：2026-04-21
> 對象：Joey（ShiFu CEO，創業家，完全新手）
> 時長：2 小時
> 設備：Mac，已有 Claude Pro 訂閱
> 目標：理解什麼是好的 AI Agent + 帶走一個能用的核心

---

## 第一性原理

Joey 是 CEO，最稀缺的資源是**注意力**。

他的痛點：
- 大量資訊進來，沒時間消化
- 不同專案/人/脈絡不斷切換
- 想法散落各處，沒有統一的地方整理
- 需要產出內容但沒時間慢慢寫
- **最痛的：每次都要重新解釋一遍**

他真正需要的只有一件事：**一個越用越懂他的對話夥伴。**

---

## 同心圓架構

```
        ┌─────────────────────────┐
        │   自動化（穩定後開啟）     │
        │   排程・沉澱・主動通知    │
        │  ┌───────────────────┐  │
        │  │  擴展（用到時再加）  │  │
        │  │  知識庫・專長・CLI  │  │
        │  │  ┌─────────────┐  │  │
        │  │  │   核心        │  │  │
        │  │  │  認識我       │  │  │
        │  │  │  記得住       │  │  │
        │  │  │  會長大       │  │  │
        │  │  └─────────────┘  │  │
        │  └───────────────────┘  │
        └─────────────────────────┘
```

### 核心（課堂建好）
- **認識我** → CLAUDE.md（身份、思考方式、原則、溝通風格）
- **記得住** → MEMORY.md（對話中自動累積）
- **會長大** → 進化規則寫在 CLAUDE.md 裡

### 擴展（用到時再加）
- vault/ 知識庫
- skills/ 專長
- CLI 串接（gh, gws）

### 自動化（穩定後開啟）
- Routines（每日晨報、每週沉澱）
- 沉澱機制（類 OpenClaw 做夢機制簡化版）

---

## CLAUDE.md 漸進式成長

一份活文件，課堂上從 3 行長到完整設定。每過一個環節就長一段，Joey 親眼看到它一層層變強。

### 課堂 Onboarding 後：
```markdown
# [Joey 取的名字]

## 你服務的人
- 名字、角色、公司、在做什麼

## 溝通原則
- Joey 的偏好

## 記憶管理
- 自動記住對話中的事
- 可手動「記住」/「忘掉」

## 知識後盾
- 遇到深入問題，搜尋 references/

## 自我進化規則
- 重複偵測：同類要求 ≥3 次 → 建議建 Skill
- 糾正學習：被糾正就記住，不再犯
- 品質棘輪：Skill 只進不退
- 修改前先給你看，你批准才改
```

---

## 自動學習機制

### 重複偵測（講三次就學會）
掃描近期 memory 和對話 → 發現重複模式 → 建議建 Skill → 你同意 → 自動生成 SKILL.md

### 糾正學習
被糾正 → 更新 memory → 不再犯

### 沉澱機制（簡化版 OpenClaw 做夢）
每週自動：掃 memory → 掃 vault → 找模式 → 產出沉澱日誌 → 建議升級（你批准才改）

### 品質棘輪（達爾文機制）
更新 Skill 前先比對新舊版本，變差就不改。

---

## 外部串接：CLI 優先

### 為什麼 CLI > MCP
- 上手門檻低、通用性高、透明可 audit、零維護
- MCP 等用到每天 10 次以上再考慮

### GitHub CLI (`gh`)
- 專案管理通道

### Google Workspace CLI (`gws`)
- 40+ Google API 統一介面
- `gws +triage`（讀信）、`gws +agenda`（行事曆）、Drive、Sheets、Docs

---

## 課程流程（2 小時）

| 時間 | 做什麼 | 產出 |
|-----|--------|-----|
| 0:00-0:15 | 開場 demo 差異感 + 同心圓框架 | 理解 |
| 0:15-0:30 | 安裝 Claude Code + GWS CLI 全設定 | 工具就位 |
| 0:30-0:55 | 跑 Onboarding 引導 → 建 CLAUDE.md | 核心完成 |
| 0:55-1:00 | 體驗記憶累積 | MEMORY.md 開始長 |
| 1:00-1:20 | 真實任務：gws 讀信/行事曆 + 整理 insight | 體驗威力 |
| 1:20-1:35 | 真實任務：起草內容 | 體驗核心威力 |
| 1:35-1:50 | 展示擴展圈 + 自動化圈（不建，只看） | 知道路在哪 |
| 1:50-2:00 | 交付 week-1 任務 + Q&A | 帶走作業 |

---

## 第一週：用爆它

原則：本來就在做的事，全部改用 Agent 做。

### 驗收標準
- MEMORY.md ≥ 15 條
- vault/ ≥ 5 份文件
- 至少起草 3 份內容、整理 3 場會議
- gws 至少用 10 次
- 問「你了解我什麼？」→ 準確 ≥ 10 點
- 它寫的東西 ≥ 60% 不用大改
- 至少糾正過 3 次且沒再犯

---

## 安裝包結構

```
[joey-names-this]/
├── README.md
├── CLAUDE.md
├── MEMORY.md
├── guides/
│   ├── 01-setup.md
│   ├── 02-onboarding.md
│   ├── 03-vault.md
│   ├── 04-skills.md
│   ├── 05-routines.md
│   └── 06-cli-advanced.md
├── vault/
│   ├── company/
│   ├── industry/
│   ├── meetings/
│   └── personal/
├── skills/
│   ├── insight-finder/SKILL.md
│   └── content-drafter/SKILL.md
├── routines/
│   ├── daily-briefing.md
│   └── weekly-evolution.md
├── milestones/
│   ├── week-1.md
│   └── review-template.md
└── references/
    ├── README.md
    ├── claude-code-docs/
    ├── vault-for-founders/
    ├── nuwa-skill/
    ├── gws-cli/
    ├── hermes-agent/
    ├── openclaw/
    └── qmd/
```

---

## 互動引導機制（雷蒙模式）

每份 guides/ 文件都是雙層結構：
- 上半：給人看的說明
- 下半：給 Claude 執行的指令

關鍵模式：
- AskUserQuestion 收集輸入（選擇題 + 開放題混搭）
- 不跳過任何 Section
- Append 不 Overwrite
- 完成後 grep 檢查 placeholder
- 狀態偵測：已存在的設定不重複建

---

## References

| 參考資料 | 取用的概念 |
|---------|----------|
| Vault-for-Founders | 知識庫結構、Agent-centric 寫法、引導式建立 |
| Raymond 迷你課 | 雙層引導文件、AskUserQuestion 模式、安裝包結構 |
| OpenClaw | 做夢/沉澱機制 |
| Nuwa Skill + 達爾文 | Skill 品質棘輪、自動進化 |
| Hermes Agent | 複雜任務後自動存 Skill、糾正學習 |
| Claude Code Docs | Routines、Memory、Skills、Hooks、Channels |
| GWS CLI | Google Workspace 統一 CLI 介面 |
| QMD | 本地知識搜尋（進階參考） |
