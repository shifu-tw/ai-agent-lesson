# AI Agent 家教課 — 簡報內容結構

> 給 Claude Design 用。生成淺色系簡報網頁。
> 設計方向：Claude 經典配色（米白底 #FAF9F6、terra cotta 強調色 #D97757、深灰文字 #1a1a1a）
> 每頁都要有示意圖/圖表/視覺元素（不用 emoji，用 CSS 繪製的 icon 或 SVG）
> 鍵盤操作：←→ Space 換頁、F 全螢幕、N 講師筆記
> 總共 29 頁

---

## S00 — 封面

**標籤：** Private Lesson
**大標：** 打造你的 AI 夥伴
**副標：** 從 Context 管理到自主進化的完整框架

---

## S01 — 環境設定（邊裝邊講）

**標籤：** 先跑這個
**標題：** 環境設定
**說明：** 先啟動安裝（背景跑），我們邊裝邊講。

**程式碼區塊：**
```
# Homebrew（會自動裝 Xcode CLT，最久 15-20 min）
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**四張卡片（2x2），每張要有 icon：**
1. **gh — GitHub CLI** → 版本控制 + 備份
2. **gws — Google Workspace** → 讀信、行事曆、Drive
3. **better-rm — 安全刪除** → 刪檔案移到垃圾桶，誤刪可救
4. **資料夾位置** → 推薦 iCloud（多裝置同步）或 Documents

**講師筆記：** Homebrew 最久。先貼指令背景跑，然後開始講概念。如果 Joey 課前已裝就跳過。

---

## S02 — AI Agent 現在能做什麼

**標籤：** 現況
**標題：** AI Agent 現在能做什麼

**兩欄對比（示意圖：能力圈 vs 限制圈）：**
- ✓ 能做到：讀寫檔案、跑程式、搜尋資料、串接工具、生成內容、分析資料、管理專案
- ✗ 限制：會幻覺（編造數字）、長對話品質衰退、沒有真正的記憶、不會自己判斷該不該做

**重點框（terra cotta）：**
品質好不好，90% 取決於框架設計。同一個模型，沒框架 = 通用回答。有框架 = 像用了三個月的夥伴。今天要建的就是這個框架。

---

## S03 — 不是工具，是夥伴

**標籤：** 心智模型
**標題：** 你要建的不是工具，是夥伴

**VS 對比（左紅右綠）：**
- 工具：每次重新解釋背景。換話題從頭來。關掉全忘。你遷就它。
- 夥伴：知道你的公司、思考方式、上次的決定。你只說新的事。它遷就你。

**重點框：**
今天建的不是設定好就不動的系統。是一個活的、會跟著你進化的夥伴。

---

## S04 — Context Window

**標籤：** 底層邏輯
**標題：** Context Window — AI 的工作記憶

**示意圖：** 一個長條框代表 context window，裡面分成幾個色塊：
- CLAUDE.md（小塊，固定）
- 相關記憶（小塊，按需）
- 當前對話（中塊，動態）
- 剩餘空間（越多越好）
旁邊標注：塞越滿 → 品質越差

**文字：**
- 每次對話有工作記憶上限
- 就算 100 萬 token，塞越滿越笨
- **Context 污染：** 塞不相關的東西 = 稀釋 AI 注意力

**重點框：**
所有設計都在解決同一個問題：讓 AI 有限的工作記憶裡，永遠放著最重要的東西。

**講師筆記：** 核心概念。講慢。所有設計的底層邏輯。

---

## S05 — 三層設計

**標籤：** 架構
**標題：** 三層設計

**視覺：** 同心圓圖（正圓，不要橢圓）
- 外圈：自動化（紫色，穩定後開）
- 中圈：擴展（藍色，用到時加）
- 內圈：核心（terra cotta，今天建好）

**右側表格：**

| 層 | 內容 | Context 策略 |
|---|------|-------------|
| CLAUDE.md | 身份 | 每次自動載入，精煉 50 行 |
| MEMORY.md | 記憶 | 只載入相關的 |
| 進化規則 | 自我改善 | 寫在 CLAUDE.md 裡 |
| vault/ | 知識庫 | 按需搜尋，不預載 |
| skills/ | 專長 | 觸發才載入 |
| CLI | 外部工具 | 程式跑，零 token |
| routines/ | 排程 | 獨立執行 |

**重點框：**
不是一次建完。是用出來的。核心今天做好，其餘進化規則會帶你走到。

---

## S06 — Context 管理 Best Practice

**標籤：** 實戰技巧
**標題：** Context 管理

**六張卡片（2x3 或 3x2），每張有 icon：**
1. **不同任務開不同對話** — 上下文互相污染
2. **兩段式工作法** — 第一輪討論→產出文件。第二輪拿文件當指令執行。
3. **長對話會衰退** — 聊越久品質越差。重要任務開新對話。
4. **Agent-centric 寫法** — 寫給 AI 讀：結構清晰、規則明確、不要客氣話。
5. **Checkpoint 可回滾** — 做錯隨時退回上一步。
6. **.env 不要貼** — API key、密碼、token 不直接貼進對話。

---

## S07 — 不做的後果

**標籤：** 為什麼
**標題：** 不做的後果

**表格（每行左邊紅色 icon）：**

| 如果不建... | 會怎樣 |
|------------|--------|
| CLAUDE.md | 每次重新解釋你是誰。token 一半花在重複背景。 |
| MEMORY.md | 上週討論三小時的策略，今天全忘了。 |
| 進化規則 | 用三個月還跟第一天一樣。 |
| vault/ | 你的文件、會議紀錄都用不上。 |
| Git 備份 | 改壞沒法回滾。換電腦一切從零。 |

---

## S08 — Claude Code + CLI vs MCP

**標籤：** 工具選擇
**標題：** 為什麼是 Claude Code CLI

**說明：** Claude Code 是唯一能直接跑 CLI 指令的介面。Chat 和 Cowork 做不到。

**對比表格：**

| | CLI | MCP |
|---|-----|-----|
| 本質 | 程式直接執行，結果給 AI | AI 透過協議呼叫外部服務 |
| Token | 零 | 每次消耗 |
| 上手 | 一行指令 | 裝 server + 設定 |
| 透明 | 看得到在幹嘛 | 黑盒 |
| 維護 | 零 | server 要更新 |

**重點框：** CLI 先行，MCP 備用。兩者不衝突。

---

## S09 — 安裝包結構

**標籤：** 我們的設計
**標題：** 安裝包結構

**示意圖：** 資料夾樹狀圖，用色塊標示 context 策略

```
[你取的名字]/
├── CLAUDE.md          ← 每次自動載入（精煉 50 行）
├── MEMORY.md          ← 只載入相關的
├── vault/             ← 按需搜尋，不預載
│   ├── identity/         你是誰（CLAUDE.md）
│   ├── context/          公司背景（CLAUDE.md）
│   ├── company/          公司資料
│   ├── industry/         產業觀察
│   ├── meetings/         會議紀錄
│   ├── people/           聯絡人
│   └── personal/         個人思考
├── skills/            ← 觸發時才載入
├── guides/            ← Phase 2/3（成長觸發自動建議）
├── routines/          ← 穩定後開
├── tools/             ← 程式，零 token
├── milestones/        ← 進度追蹤
└── references/        ← 進化教科書
```

**重點框：** 什麼時候載入、載入多少、誰來處理 — 都是設計過的。每個 vault 子資料夾有自己的 CLAUDE.md，Agent 進去工作時會讀。

---

## S10 — 一鍵安裝

**標籤：** 安裝
**標題：** 一步完成

**大字展示：**
```
打開 Claude Code Desktop，貼這段：

讀 https://raw.githubusercontent.com/shifu-tw/ai-agent-lesson/main/install.md 然後幫我建一個 AI 夥伴
```

**流程圖（左到右）：**
Agent 讀劇本 → 裝工具 → 問你問題 → 建資料夾 → 生成 CLAUDE.md → symlink → Git 備份 → 完成

**說明：** Agent 自動跑完所有設定。你只需要回答問題。

---

## S11 — 匯入 ChatGPT

**標籤：** 匯入
**標題：** 把 ChatGPT 搬過來

**流程圖：**
匯出 JSON → 程式解析（0 token）→ 統計摘要 → AI 分類（1 次 token）

**程式碼：**
```
python3 tools/parse-chatgpt-export.py conversations.json -o vault/
```

**重點框：** 幾百個對話直接餵 AI = 燒 token + 污染 context。程式先壓縮，AI 最後讀一次。

**講師筆記：** Joey 事先匯出：ChatGPT Settings → Data Controls → Export Data。

---

## S12 — Onboarding → CLAUDE.md

**標籤：** 建造
**標題：** Onboarding → CLAUDE.md

**流程圖：**
Agent 問你問題 → 結合 ChatGPT 輪廓 → 生成 CLAUDE.md → git init + push

**四張卡片（2x2）：**
1. **你是誰** — 角色、公司。決定回答角度。
2. **你怎麼思考** — 決策框架。讓它用你的邏輯。
3. **溝通偏好** — 設一次，省每次改格式。
4. **紅線 + 協作方式** — 不幫做決定。什麼時候該挑戰你。

**重點框：** CLAUDE.md 控制在 50 行。精煉。寫給 AI 讀不是寫給人讀。每次對話都載入，太囉唆浪費 context。

**講師筆記：** 最長環節 20-25 min。建完後用同一個問題驗證差異。提醒完成後要關掉對話開新的。

---

## S13 — 記憶 + 進化規則

**標籤：** 建造
**標題：** 記憶 + 進化規則

**左欄 — MEMORY.md：**
- 自動：正常聊天就累積。零成本。
- 手動：「記住 ___」/「忘掉 ___」/「你記得什麼？」
- 透明：打開就看得到，跟 ChatGPT 黑箱不同。
- 邊界標記保護，重跑不覆蓋。

**右欄 — 進化規則（四張小卡）：**
- 講 3 次就學會 → 提議建 Skill
- 糾正就記住 → 不再犯
- 只進不退 → 更新前比對新舊
- 你批准才改 → 身份設定你控制

**示意圖：** 進化循環圖（日常對話 → 記憶累積 → 發現模式 → 建議升級 → 你批准 → 系統變好 → 回到日常對話）

---

## S14 — 成長觸發

**標籤：** 自動進化
**標題：** 系統會自己帶你升級

**說明：** 寫在 CLAUDE.md 裡的成長觸發規則。你不用記有哪些功能可以開，系統會在對的時間建議你。

**表格：**

| 條件 | Agent 會說 |
|------|----------|
| MEMORY.md > 30 條 | 「記憶累積不少了，要不要整理精華版？」 |
| 重要任務結束 | 「這個要不要記一下？」 |
| 用滿兩週 | 「要不要讓我有更完整的個性？」 |
| 對外文稿需求 | 「要不要建寫作風格規則？」 |
| 同一任務跑 5 次 | 「這可以自動化了」 |
| vault > 20 份 | 「知識庫長大了，要不要整理？」 |

**重點框：** Phase 2/3 全部零手動觸發。Joey 的體驗：Agent 越來越聰明。

---

## S15 — 裝 Skill

**標籤：** 建造
**標題：** 裝 Skill

**程式碼：**
```
# 從模板複製
cp -r references/nuwa-skill/examples/munger-perspective skills/
cp -r references/nuwa-skill/examples/naval-perspective skills/
```

**三張預建 Skill 卡片：**
1. **insight-finder** — 「找 insight」→ 整理脈絡 + 挖洞察
2. **content-drafter** — 「幫我寫」→ 用你的口吻起草
3. **git-sync** — /commit → 一鍵備份

**講師筆記：** 芒格 + Naval。當場用真問題試。最後 /commit 備份。

---

## S16 — 實戰：讀信 + 行事曆

**標籤：** 實戰
**標題：** 今天最該注意什麼

**Prompt 範例：**
```
"讀我今天的信跟行事曆。
按重要性排，不是按時間排。
需要準備的會議列出來。"
```

**兩欄對比（示意圖：程式層 vs AI 層）：**
- CLI 做：gws +triage 讀信 / gws +agenda 看行事曆 → 零 token
- AI 做：結合 CLAUDE.md 判斷優先順序 → 為你量身排序

**重點框：** 注意它怎麼排。是按「它知道你在意什麼」排的。這就是 CLAUDE.md 在起作用。

**講師筆記：** 用 Joey 當天真實的信件和行事曆。

---

## S17 — 實戰：挖 Insight + 芒格模式

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

## S18 — 實戰：起草 + 糾正

**標籤：** 實戰
**標題：** 用你的方式起草

**Prompt 範例：**
```
"幫我針對 [主題] 起草一封回覆。"
```

**兩欄：**
- 寫得好：直接用或微調。60% 不用大改。
- 不太對：「太正式了。」→ 它記住 → 下次不用再說。進化規則運作中。

---

## S19 — 作業

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

## S20 — 驗收

**標籤：** 驗收
**標題：** 一週後
**說明：** 跟 Agent 說「跑 review」。下次上課看結果。

**Checklist（打勾框）：**
- MEMORY.md ≥ 15 條記憶
- vault/ ≥ 5 份文件
- 起草 3+ 內容、整理 3+ 會議
- gws 至少用 10 次
- 問「你了解我什麼？」準確 10+ 點
- 它寫的 60%+ 不用大改
- 糾正 3+ 次且沒再犯
- 能說出「它最懂我的一件事」

---

## S21 — Skill 的本質

**標籤：** 深入
**標題：** Skill 的本質
**說明：** Skill = 一份 SKILL.md。寫給 AI 讀的 SOP。你教過一次，不用每次重新教。

**三張卡片：**
1. 觸發條件 — 什麼時候啟動
2. 執行步驟 — 做什麼、怎麼做
3. 品質標準 — 好的產出長什麼樣

**重點框：** Context 策略：Skill 不會一直佔 context。50 個 Skill 只載用到的那幾個。

---

## S22 — 女媧.skill

**標籤：** Skill 展開
**標題：** 女媧.skill — 蒸餾名人思維
**說明：** 輸入人名 → 6 個平行 Agent 深度調研 → 提煉思維框架 → 生成可運行 Skill

**資料夾結構圖：**
```
munger-perspective/
├── SKILL.md              ← 芒格思維框架本體
│   ├── 5 個核心心智模型
│   ├── 8 條決策啟發式
│   └── 表達 DNA
└── references/
    ├── 25-biases.md      ← 25 種心理偏誤
    └── 深度調研報告.md    ← 50+ 來源
```

**已蒸餾 13 位：** 芒格、Naval、Jobs、費曼、Musk、Paul Graham、張一鳴、Taleb、Karpathy...

---

## S23 — 同事.skill

**標籤：** Skill 展開
**標題：** 同事.skill — 蒸餾真實的人
**說明：** 把真實的人（同事、夥伴、顧問）的思維方式變成 AI Skill。GitHub 5000+ 星。

**重點框：** 女媧蒸餾名人（公開資料多）。同事.skill 蒸餾你身邊的人（你提供素材）。結合 = 名人顧問團 + 人脈智囊。

---

## S24 — 達爾文.skill

**標籤：** Skill 展開
**標題：** 達爾文.skill — Skill 自動進化
**說明：** 靈感來自 Karpathy autoresearch。讓 Skill 自動越來越好。

**三張卡片：**
1. **8 維評估** — 多角度評分 Skill 品質
2. **棘輪機制** — 只保留進步。退步回滾。
3. **雙 Agent 評分** — 兩個 AI 獨立評，防偏見

**重點框：** 你不用手動優化 Skill。達爾文自動測試、評估、迭代。

---

## S25 — 雷蒙的 Skill 結構對比

**標籤：** Skill 展開
**標題：** 雷蒙的 Skill — 三種複雜度

**三欄對比：**

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

**重點框：** Skill 的複雜度看需求。簡單的只要一個 SKILL.md。

---

## S26 — 雷蒙的 Agent 架構

**標籤：** 參考架構
**標題：** 雷蒙的 Agent 架構

**資料夾樹狀圖：**
```
Raymond-Agent/                  ← iCloud 同步
├── 000_Agent/                  ← 核心（symlink 到 .claude/）
│   ├── CLAUDE.md                  身份 + 規則
│   ├── skills/                    可重用 Skill
│   ├── workflows/                 多步驟工作流
│   ├── memory/                    記憶檔案
│   └── hooks/                     自動化觸發
├── pro-kit/                    ← 引導式安裝包
└── docs/                       ← 13 篇漸進教學
```

**重點框：** 把 .claude/ 搬到 iCloud 可同步路徑，用 symlink 連回去。多機同步不失憶。可攜性設計：換 AI 大腦時資料跟著走。

---

## S27 — Vault for Founders 架構

**標籤：** 參考架構
**標題：** Vault for Founders 架構

**資料夾樹狀圖：**
```
Your-Vault/                     ← Obsidian + Git
├── README.md                   ← Agent 的入口
├── agent-persona.md            ← 三層人格（Identity/Soul/Persona）
├── memory-summary.md           ← 長期記憶精華
├── identity/                   ← 你是誰
├── context/                    ← 公司背景
├── memory/                     ← 決策紀錄
├── sop/                        ← 操作流程
├── projects/                   ← 進行中專案
├── people/                     ← 重要聯絡人
└── skills/                     ← AI 技能
```

**重點框：** Agent-centric 寫法。persona 不能填空 template，要跟 AI 對話後產生。Agent 是合夥人不是工具 — 定義了什麼時候該挑戰創辦人。

---

## S28 — 預覽未來

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

**references/ 的角色：**
不是搜尋資料庫，是進化教科書。Agent 升級時從這裡找方法論。

---

## S29 — 結語

**大標（置中）：**
最好的 AI 夥伴
不是最聰明的
是最懂你的

---

## 講師筆記匯總

| Slide | 筆記 |
|-------|------|
| S01 | 第一件事貼 Homebrew。15-20 分鐘。邊裝邊講。 |
| S04 | 核心概念。講慢。 |
| S10 | Homebrew 應該裝好了。 |
| S11 | Joey 事先匯出 ChatGPT。 |
| S12 | 最長 20-25 min。建完用同一個問題驗證。完成後關掉開新的。 |
| S15 | 芒格 + Naval。當場用真問題試。最後 /commit。 |
| S16-18 | 用 Joey 當天真實的工作。不用假資料。 |

---

## 一鍵安裝（給學員的）

```
打開 Claude Code Desktop，貼這段：

讀 https://raw.githubusercontent.com/shifu-tw/ai-agent-lesson/main/install.md 然後幫我建一個 AI 夥伴
```
