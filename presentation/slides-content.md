# AI Agent 家教課 — 簡報內容結構

> 設計方向：淺色系，Claude 經典配色（米白底、terra cotta 強調色、乾淨 sans-serif）
> 每頁都要有示意圖/圖表/視覺元素
> 29 頁，鍵盤操作（←→ Space F N）

---

## S00 — 封面

**標籤：** Private Lesson
**大標：** 打造你的 AI 夥伴
**副標：** 從 Context 管理到自主進化的完整框架

---

## S01 — 環境設定（先跑這個）

**標籤：** 先跑這個
**標題：** 環境設定
**說明：** 先啟動安裝（背景跑），我們邊裝邊講。

**程式碼：**
```
# 第一步：裝 Homebrew（會自動裝 Xcode CLT，最久）
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**四張卡片（2x2）：**
1. **gh — GitHub CLI** → 版本控制 + 備份。讓 Agent 建 repo、commit、push。
2. **gws — Google Workspace** → 讀信、行事曆、Drive、Sheets。一個工具打通 Google。
3. **better-rm — 安全刪除** → Agent 刪檔案時移到垃圾桶。誤刪可以救回來。
4. **資料夾位置** → 推薦 iCloud：多裝置同步 + 自動備份。或 Documents：單機穩定。

---

## S02 — AI Agent 現在能做什麼

**標籤：** 現況
**標題：** AI Agent 現在能做什麼

**兩欄對比：**
- 能做到：讀寫檔案、跑程式、搜尋資料、串接工具、生成內容、分析資料、管理專案
- 限制：會幻覺（編造數字）、長對話品質衰退、沒有真正的記憶、不會自己判斷該不該做

**重點框：**
品質好不好，90% 取決於框架設計。同一個模型，沒框架 = 通用回答。有框架 = 像用了三個月的夥伴。今天要建的就是這個框架。

---

## S03 — 不是工具，是夥伴

**標籤：** 心智模型
**標題：** 你要建的不是工具，是夥伴

**VS 對比：**
- 工具：每次重新解釋背景。換話題從頭來。關掉全忘。你遷就它。
- 夥伴：知道你的公司、思考方式、上次的決定。你只說新的事。它遷就你。

**重點框：**
今天建的不是設定好就不動的系統。是一個活的、會跟著你進化的夥伴。

---

## S04 — Context Window

**標籤：** 底層邏輯
**標題：** Context Window — AI 的工作記憶

**左側文字：**
- 每次對話有「工作記憶」上限
- 就算 100 萬 token，塞越滿越笨
- Context 污染：塞不相關的東西 = 稀釋 AI 注意力。像開會時旁邊有人一直講無關的事。

**右側卡片：**
塞滿的後果：回答變泛、忘記前面說的、開始幻覺、語氣變奇怪、重複自己

**重點框：**
所有設計都在解決同一個問題：讓 AI 有限的工作記憶裡，永遠放著最重要的東西。

**視覺建議：** 畫一個 context window 的示意圖 — 一個長條框，裡面分成「身份」「記憶」「當前對話」「空間」四塊，顯示怎麼分配。

---

## S05 — 三層設計

**標籤：** 架構
**標題：** 三層設計

**視覺：** 同心圓圖（正圓）
- 外圈：自動化（紫色）
- 中圈：擴展（藍色）
- 內圈：核心（terra cotta 色）

**右側表格：**

| 層 | 內容 | Context 策略 |
|---|------|-------------|
| 核心 CLAUDE.md | 身份 | 每次自動載入，精煉佔位 |
| 核心 MEMORY.md | 記憶 | 只載入相關的 |
| 核心 進化規則 | 自我改善 | 寫在 CLAUDE.md 裡 |
| 擴展 vault/ | 知識庫 | 按需搜尋，不預載 |
| 擴展 skills/ | 專長 | 觸發才載入 |
| 擴展 CLI | 外部工具 | 程式跑，零 token |
| 自動化 routines/ | 排程 | 獨立執行 |

---

## S06 — Context 管理 Best Practice

**標籤：** 實戰技巧
**標題：** Context 管理

**六張卡片（2x3 或 3x2）：**
1. **不同任務開不同對話** — 寫文案和分析數據不混。上下文互相污染。
2. **兩段式工作法** — 第一輪討論→產出文件。第二輪拿文件當指令執行。
3. **長對話會衰退** — 聊越久品質越差。重要任務開新對話帶上 CLAUDE.md。
4. **Agent-centric 寫法** — 寫給 AI 讀：結構清晰、規則明確、不要客氣話。
5. **Checkpoint 可回滾** — 做錯隨時退回上一步。放心讓它嘗試。
6. **.env 不要貼** — API key、密碼、token 不直接貼進對話。

---

## S07 — 不做的後果

**標籤：** 為什麼
**標題：** 不做的後果

**表格：**

| 如果不建... | 會怎樣 |
|------------|--------|
| CLAUDE.md | 每次重新解釋你是誰。token 一半花在重複背景。 |
| MEMORY.md | 上週討論三小時的策略，今天全忘了。永遠原地打轉。 |
| 進化規則 | 用三個月還跟第一天一樣。教過的不會保留。 |
| vault/ | 你的文件、會議紀錄都用不上。只靠訓練資料。 |
| Git 備份 | CLAUDE.md 改壞沒法回滾。換電腦一切從零。 |

---

## S08 — Claude Code + CLI vs MCP

**標籤：** 工具
**標題：** 為什麼是 Claude Code CLI

**說明：** Claude Code 是唯一能直接跑 CLI 指令的介面。Chat 和 Cowork 做不到。

**對比表格：**

| | CLI | MCP |
|---|-----|-----|
| 本質 | 程式直接執行，結果給 AI | AI 透過協議呼叫外部服務 |
| Token | 零。程式跑完只餵結果 | 每次呼叫消耗 token |
| 上手 | 一行指令 | 裝 server + 寫設定 |
| 透明 | 看得到在幹嘛 | 黑盒 |
| 維護 | 零 | server 要更新 |

**重點框：** CLI 先行，MCP 備用。兩者不衝突。

---

## S09 — 安裝包結構

**標籤：** 我們的設計
**標題：** 安裝包結構

**資料夾樹狀圖：**
```
[你取的名字]/
├── CLAUDE.md          ← 身份（每次自動載入，精煉）
├── MEMORY.md          ← 記憶（只載入相關的）
├── vault/             ← 知識庫（按需搜尋，不預載）
│   ├── company/          策略、產品
│   ├── industry/         產業觀察
│   ├── meetings/         會議紀錄
│   └── personal/         個人思考
├── skills/            ← 專長（觸發時才載入）
│   └── git-sync/         /commit 快速備份
├── routines/          ← 排程（穩定後開）
├── guides/            ← 引導 prompt（建造用）
├── tools/             ← 程式工具（零 token）
├── milestones/        ← 進度追蹤
└── references/        ← Agent 搜深入問題
```

**重點框：** 什麼時候載入、載入多少、誰來處理 — 都是設計過的。

---

## S10 — 裝工具 + 認證

**標籤：** 安裝
**標題：** 裝工具 + 認證

**程式碼：**
```
# 裝工具
brew install gh
brew install googleworkspace-cli
curl -sSL https://raw.githubusercontent.com/doggy8088/better-rm/main/install.sh | bash

# 認證
gh auth login
gws auth login -s gmail,calendar,drive

# 驗證
gws gmail +triage        # 信件摘要 ✓
gws calendar +agenda     # 今天行程 ✓
```

---

## S11 — 匯入 ChatGPT

**標籤：** 匯入
**標題：** 搬 ChatGPT 資料
**說明：** 幾百個對話直接餵 AI = 燒 token + 污染 context。程式先壓縮，AI 最後讀一次。

**流程圖（左到右）：**
匯出 JSON → 程式解析（0 token）→ 統計摘要 → AI 分類（1 次 token）

**程式碼：**
```
python3 tools/parse-chatgpt-export.py conversations.json -o vault/
# → 統計總覽 / 使用者輪廓 / 分類 prompt
```

---

## S12 — Onboarding → CLAUDE.md

**標籤：** 建造
**標題：** Onboarding → CLAUDE.md

**流程圖：**
「跑 onboarding」→ 回答問題 → 結合 ChatGPT → CLAUDE.md → git init + push

**四張卡片（2x2）：**
1. **你是誰** — 角色、公司。決定回答角度。
2. **你怎麼思考** — 決策框架。讓它用你的邏輯。
3. **溝通偏好** — 設一次，省每次改格式。
4. **紅線 + 權限** — 不幫做決定。Permission mode 先用 default。

---

## S13 — 記憶 + 進化規則

**標籤：** 建造
**標題：** 記憶 + 進化規則

**左欄 — MEMORY.md：**
- 自動：正常聊天就累積
- 手動：記住 / 忘掉 / 列出
- 透明：打開就看得到，跟 ChatGPT 黑箱不同

**右欄 — 進化規則（加進 CLAUDE.md）：**
- 講 3 次就學會 → 提議建 Skill
- 糾正就記住 → 不再犯
- 只進不退 → 更新前比對新舊
- 你批准才改 → 身份設定你控制

---

## S14 — 裝 Skill

**標籤：** 建造
**標題：** 裝 Skill

**程式碼：**
```
cp -r references/nuwa-skill/examples/munger-perspective skills/
cp -r references/nuwa-skill/examples/naval-perspective skills/
```

**說明：** 用一個真正在想的商業問題問芒格。一個指令切換思維框架。

**結尾提醒：** /commit — 把今天所有設定備份到 GitHub。

---

## S15 — 實戰：讀信 + 行事曆

**標籤：** 實戰
**標題：** 今天最該注意什麼

**Prompt 範例：**
```
"讀我今天的信跟行事曆。
按重要性排，不是按時間排。
需要準備的會議列出來。"
```

**兩欄對比：**
- CLI 做：gws +triage 讀信 / gws +agenda 看行事曆 → 零 token
- AI 做：結合 CLAUDE.md 判斷優先順序 → 為你量身排序

**重點框：** 注意它怎麼排。是按「它知道你在意什麼」排的。

---

## S16 — 實戰：挖 Insight + 芒格模式

**標籤：** 實戰
**標題：** 整理脈絡 + 挖 Insight

**Prompt 範例：**
```
# 你的視角
"整理這份資料的脈絡，找出我可能沒注意到的。"

# 切芒格模式
"用芒格的視角看這件事。有什麼認知偏誤？"
```

**兩欄：**
- 你的視角：Agent 用你的思考框架（CLAUDE.md）整理
- 芒格視角：逆向思考、跨學科分析、找盲點

**重點框：** 兩個視角疊加。你的框架整理 + 芒格的鏡片挑戰。

---

## S17 — 實戰：起草 + 糾正

**標籤：** 實戰
**標題：** 用你的方式起草

**Prompt 範例：**
```
"幫我針對 [主題] 起草一封回覆。"
```

**兩欄：**
- 寫得好：直接用或微調。60% 不用大改的目標。
- 不太對：「太正式了。」→ 它記住 → 下次不用再說。進化規則運作中。

---

## S18 — 作業

**標籤：** 作業
**標題：** 這一週：用爆它
**重點：** 唯一規則：本來在做的事，全部先問它。

**列表：**
- 收到信 → 先讓它讀
- 開完會 → 跟它說剛聊什麼
- 要寫東西 → 讓它先起草
- 做決策前 → 把脈絡丟給它
- 讀到文章 → 丟進 vault/
- 想到什麼 → 直接跟它說
- 做完重要事 → /commit 備份

**提醒：** 不同任務開不同對話。長對話品質會衰退。

---

## S19 — 驗收

**標籤：** 驗收
**標題：** 一週後
**說明：** 跟 Agent 說「跑 review」。下次上課看結果。

**Checklist：**
- MEMORY.md ≥ 15 條記憶
- vault/ ≥ 5 份文件
- 起草 3+ 內容、整理 3+ 會議
- gws 至少用 10 次
- 問「你了解我什麼？」準確 10+ 點
- 它寫的 60%+ 不用大改
- 糾正 3+ 次且沒再犯
- 能說出「它最懂我的一件事」

---

## S20 — Skill 的本質

**標籤：** 深入
**標題：** Skill 的本質
**說明：** Skill = 一份 SKILL.md。寫給 AI 讀的 SOP。

**三張卡片：**
1. 觸發條件 — 什麼時候啟動
2. 執行步驟 — 做什麼、怎麼做
3. 品質標準 — 好的產出長什麼樣

**重點框：** Context 策略：Skill 不會一直佔 context。50 個 Skill 只載用到的那幾個。

---

## S21 — 女媧.skill

**標籤：** Skill 展開
**標題：** 女媧.skill — 蒸餾名人思維
**說明：** 輸入人名 → 6 個平行 Agent 深度調研 → 提煉思維框架 → 生成可運行 Skill

**資料夾結構：**
```
munger-perspective/
├── SKILL.md                    ← 芒格思維框架本體
│   ├── 5 個核心心智模型
│   ├── 8 條決策啟發式
│   └── 表達 DNA
└── references/
    ├── 25-biases.md            ← 25 種心理偏誤
    └── 深度調研報告.md          ← 50+ 來源
```

**已蒸餾 13 位：** 芒格、Naval、Jobs、費曼、Musk、Paul Graham、張一鳴、Taleb、Karpathy...

---

## S22 — 同事.skill

**標籤：** Skill 展開
**標題：** 同事.skill — 蒸餾真實的人
**說明：** 把真實的人（同事、夥伴、顧問）的思維方式變成 AI Skill。GitHub 5000+ 星。

**重點框：** 女媧蒸餾名人（公開資料多）。同事.skill 蒸餾你身邊的人（你提供素材）。結合 = 名人顧問團 + 人脈智囊。

---

## S23 — 達爾文.skill

**標籤：** Skill 展開
**標題：** 達爾文.skill — Skill 自動進化
**說明：** 靈感來自 Karpathy autoresearch。讓 Skill 自動越來越好。

**三張卡片：**
1. **8 維評估** — 多角度評分 Skill 品質
2. **棘輪機制** — 只保留進步。退步回滾。
3. **雙 Agent 評分** — 兩個 AI 獨立評，防偏見

**重點框：** 你不用手動優化 Skill。達爾文自動測試、評估、迭代。

---

## S24 — 雷蒙的 Skill 結構對比

**標籤：** Skill 展開
**標題：** 雷蒙的 Skill — 三種複雜度

**三欄對比，每欄一個 Skill + 資料夾樹：**

**Learning Journal（最精簡）：**
每日 5 題回顧。
```
SKILL.md
README.md
```

**Landing Page（中等）：**
17 題問答 → 生成銷售頁。
```
SKILL.md
README.md
references/
  question-bank.md
  design-rules.md
templates/
  base.html
```

**Social Cards（最重）：**
文字 → 品牌 IG 圖卡。
```
SKILL.md
README.md
assets/
  blue-dark/   4 templates
  orange-light/ 4 templates
scripts/
  screenshot.mjs
```

**重點框：** Skill 的複雜度看需求。簡單的只要一個 SKILL.md。複雜的帶 references/、templates/、scripts/。

---

## S25 — 雷蒙的 Agent 架構

**標籤：** 參考架構
**標題：** 雷蒙的 Agent 架構

**資料夾樹：**
```
Raymond-Agent/                  ← iCloud 同步
├── 000_Agent/                  ← 核心（symlink 到 .claude/）
│   ├── CLAUDE.md                  身份 + 規則
│   ├── skills/                    可重用 Skill
│   ├── workflows/                 多步驟工作流
│   ├── memory/                    記憶檔案
│   └── hooks/                     自動化觸發
├── pro-kit/                    ← 引導式安裝包（雙層結構）
└── docs/                       ← 13 篇漸進教學
```

**重點框：** 關鍵設計：把 .claude/ 搬到 iCloud 可同步路徑，用 symlink 連回去。多機同步不失憶。

---

## S26 — Vault for Founders 架構

**標籤：** 參考架構
**標題：** Vault for Founders 架構

**資料夾樹：**
```
Your-Vault/                     ← Obsidian + Git
├── README.md                   ← Agent 的入口
├── cub-persona.md              ← AI 人格（不填空，對話產生）
├── memory-summary.md           ← 長期記憶摘要
├── identity/                   ← 你是誰
├── context/                    ← 公司背景
├── memory/                     ← 決策紀錄
├── sop/                        ← 標準操作流程
├── projects/                   ← 進行中專案
├── people/                     ← 重要聯絡人
└── skills/                     ← AI 技能
```

**重點框：** Agent-centric 寫法。persona 不能填空 template，要跟 AI 對話後產生。

---

## S27 — 預覽未來

**標籤：** 預覽
**標題：** 未來會長出什麼

**表格：**

| 當你... | 系統會... |
|---------|----------|
| 丟文件進 vault/ | 知識庫長大 |
| 同一件事講 3 次 | 提議建 Skill |
| 想讓它主動跑 | 開 Routine（每日晨報） |
| 穩定用兩週 | 開沉澱機制（每週回顧） |
| 想做小工具 | Vibe Coding |
| 想跨裝置用 | iCloud 同步 + GitHub 備份 |

---

## S28 — 結語

**大標：** 最好的 AI 夥伴，不是最聰明的，是最懂你的

---

## 講師筆記（按 N 顯示，Joey 看不到）

| Slide | 筆記 |
|-------|------|
| S01 | 第一件事就貼 Homebrew 指令。15-20 分鐘跑完。邊裝邊講概念。 |
| S02 | 不是教 AI Agent 是什麼。是講品質跟框架的關係。 |
| S04 | 核心概念。講慢。所有設計的底層邏輯。 |
| S10 | Homebrew 應該裝好了。如果沒有就等一下。 |
| S11 | Joey 事先匯出：ChatGPT Settings → Data Controls → Export。 |
| S12 | 最長環節 20-25 min。建完用開場問題驗證差異。 |
| S14 | 芒格 + Naval。當場用真問題試。最後 /commit。 |
| S15-17 | 用 Joey 當天真實的工作內容。不用假資料。 |
