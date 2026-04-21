# AI 夥伴安裝劇本

> **給 Agent 的指示：** 這是完整的安裝劇本。讀完後直接執行，不要跟使用者解釋技術細節。
> 使用者只需要回答問題，其他全部你做。隱藏所有 bash 指令的細節，只顯示友善的狀態訊息。
> 如果使用者只給你 URL 而你還沒拿到完整內容，用 `curl -sL [URL] -o /tmp/install.md` 下載後讀取。

---

## 總覽

你要幫使用者從零建立一個完整的 AI 夥伴。整個流程不中斷，依序執行以下階段：

1. **環境檢查 + 安裝工具**
2. **選資料夾位置 + 建結構**
3. **匯入 ChatGPT 資料**（如果有）
4. **訪談 → 生成 CLAUDE.md**
5. **建 MEMORY.md**
6. **建 vault 基礎文件**
7. **安裝 Skills + symlink**
8. **Git 初始化 + GitHub 備份**
9. **複製 Phase 2/3 引導到成品資料夾**
10. **完成提醒**

全程用 AskUserQuestion 收集輸入。選擇題為主，開放題為輔。
語氣親切但不囉唆。你是在幫一個忙碌的人快速建好設定。

---

## 三個絕對不能破壞的原則

1. **每一個欄位都要來自使用者的回答。** 不能用 AI 生成的空泛描述填空。
2. **CLAUDE.md 用邊界標記 `<!-- AI-PARTNER-CONFIG:START/END -->`。** 疊加不覆蓋。
3. **CLAUDE.md 控制在 50 行內。** 精煉。每一行都有用。

---

## 階段 1：環境檢查 + 安裝工具

### 1-1. 檢查 Homebrew

```bash
brew --version
```

沒有 → 告訴使用者：「需要先裝 Homebrew，這會花 15-20 分鐘。我先跑安裝，我們邊裝邊聊。」

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 1-2. 裝工具

等 Homebrew 好後：

```bash
brew install gh                  # GitHub CLI — 版本控制 + 備份
brew install googleworkspace-cli # Google Workspace — 讀信/行事曆/Drive
```

better-rm（安全刪除）單獨裝，可能被權限擋：
```bash
git clone https://github.com/doggy8088/better-rm.git ~/.better-rm 2>/dev/null
```
如果成功，加 alias：
```bash
echo 'alias rm="~/.better-rm/better-rm"' >> ~/.zshrc && source ~/.zshrc
```
**如果被擋住 → 跳過。** 告訴使用者：「安全刪除工具晚點再裝，不影響使用。」不要卡在這裡。

每個工具簡短說一句為什麼裝。不要顯示 bash 指令細節。

### 1-3. 認證

```bash
# GitHub
gh auth login
# 選 GitHub.com → HTTPS → Login with web browser
# 如果沒帳號，引導 https://github.com/signup

# Google Workspace
gws auth login -s gmail,calendar,drive
# 瀏覽器會彈出授權頁
```

如果 GWS 認證失敗（沒有 gcloud），走手動路線：
1. 開 https://console.cloud.google.com/
2. 建專案 → OAuth 同意畫面 → External → 加自己為測試者
3. 建憑證 → Desktop app → 下載 JSON → 存到 `~/.config/gws/client_secret.json`
4. 重新 `gws auth login -s gmail,calendar,drive`

### 1-4. 驗證

```bash
gh --version && gws gmail +triage && gws calendar +agenda
```

全過才進下一步。

---

## 階段 2：選位置 + 建結構

### 2-1. 問位置

```
AskUserQuestion:
header: "資料夾位置"
question: "你的 AI 夥伴的家要放哪裡？"
options:
  - label: "iCloud（推薦）"
    description: "多裝置同步 + 雲端備份"
  - label: "Documents"
    description: "單機穩定"
  - label: "其他路徑"
```

### 2-2. 問名字

```
AskUserQuestion:
header: "名字"
question: "這個資料夾叫什麼名字？"
（開放題）
```

### 2-3. 拉模板 + 建結構

先從 GitHub 拉模板到暫存區（不要告訴使用者技術細節）：

```bash
REPO_TMP="/tmp/ai-agent-lesson"
rm -rf "$REPO_TMP"
git clone https://github.com/shifu-tw/ai-agent-lesson.git "$REPO_TMP" 2>/dev/null
```

建資料夾結構：

```bash
BASE="[選的路徑]/[名字]"
mkdir -p "$BASE"/{vault/{identity,context,company,industry,meetings,people,personal},skills,guides,tools,milestones,references,routines}
```

從模板複製檔案：

```bash
# Skills
cp -r "$REPO_TMP/skills/insight-finder" "$BASE/skills/"
cp -r "$REPO_TMP/skills/content-drafter" "$BASE/skills/"
cp -r "$REPO_TMP/skills/git-sync" "$BASE/skills/"

# 工具
cp "$REPO_TMP/tools/parse-chatgpt-export.py" "$BASE/tools/"

# Phase 2/3 引導
cp "$REPO_TMP/guides/10-after-action.md" "$BASE/guides/"
cp "$REPO_TMP/guides/11-soul-layer.md" "$BASE/guides/"
cp "$REPO_TMP/guides/12-memory-summary.md" "$BASE/guides/"
cp "$REPO_TMP/guides/13-voice-and-tone.md" "$BASE/guides/"
cp "$REPO_TMP/guides/14-update-identity.md" "$BASE/guides/"
cp "$REPO_TMP/guides/20-routines.md" "$BASE/guides/"
cp "$REPO_TMP/guides/21-vault-audit.md" "$BASE/guides/"

# Milestones
cp "$REPO_TMP/milestones/week-1.md" "$BASE/milestones/"
cp "$REPO_TMP/milestones/review-template.md" "$BASE/milestones/"

# Routines 範例
cp "$REPO_TMP/routines/daily-briefing.md" "$BASE/routines/"
cp "$REPO_TMP/routines/weekly-evolution.md" "$BASE/routines/"

# References 索引
cp "$REPO_TMP/references/README.md" "$BASE/references/"

# CLAUDE.md 模板（稍後用來生成）
cp "$REPO_TMP/templates/CLAUDE.md.template" "$BASE/.CLAUDE.md.template"

# 清理暫存
rm -rf "$REPO_TMP"
```

在每個 vault 子資料夾建 CLAUDE.md（給 Agent 在這個目錄工作時讀，人也能看）：

- **identity/CLAUDE.md** — 「這裡放你的價值觀、決策風格、表達方式。起草內容或分析問題時先讀這裡。第一天建。」
- **context/CLAUDE.md** — 「這裡放公司背景、產品策略、商業模式。回答公司相關問題前先讀這裡。第一天建。」
- **company/CLAUDE.md** — 「這裡放公司策略文件、產品規劃、團隊資訊。有了就丟進來。」
- **industry/CLAUDE.md** — 「這裡放產業觀察、競品分析、市場趨勢。有了就丟進來。」
- **meetings/CLAUDE.md** — 「這裡放會議紀錄。格式：YYYY-MM-DD-主題.md。開完會跟我說剛聊了什麼，我整理後存這裡。」
- **people/CLAUDE.md** — 「這裡放重要聯絡人的背景和互動紀錄。提到某人時先查這裡。人脈複雜時才建。」
- **personal/CLAUDE.md** — 「這裡放個人思考、靈感、筆記。想到什麼就丟進來。」

### 2-4. cd 進去

```bash
cd "$BASE"
```

之後所有操作都在這個目錄。

---

## 階段 3：匯入 ChatGPT（可選）

```
AskUserQuestion:
header: "ChatGPT 匯出"
question: "你有 ChatGPT 的匯出資料嗎？（Settings → Data Controls → Export）"
options:
  - label: "有，我已經下載了"
  - label: "沒有，跳過這步"
```

如果有：

```bash
python3 tools/parse-chatgpt-export.py [使用者提供的路徑] -o vault/
```

跑完後簡短告訴使用者統計結果（對話數、高頻主題）。
讀 vault/chatgpt-import/classify-prompt.md，做分類，建議歸檔到 vault/ 各資料夾。
所有建議讓使用者確認。

---

## 階段 4：訪談 → CLAUDE.md

### 4-1. 基本（一次 3 題）

```
Q1 — "你想怎麼稱呼我？"（開放）
Q2 — "你的角色？" [CEO/創辦人 | 主管 | 自由工作者 | 其他]
Q3 — "你的公司做什麼？一句話。"（開放。如果有 ChatGPT 輪廓，先列出讓使用者確認。）
```

### 4-2. 你的世界（一次 3 題）

```
Q4 — "現在最在意的 1-3 件事？"（開放）
Q5 — "做決策時通常怎麼想？"（開放）
Q6 — "AI 給建議時你希望怎麼做？" [直接給結論 | 列選項比較 | 先問再給]
```

### 4-3. 溝通（一次 2 題）

```
Q7 — "喜歡的回覆風格？" [條列式 | 結論先行 | 簡短直接 | 附推理 | 繁中]（多選）
Q8 — "什麼格式或語氣你不喜歡？"（開放）
```

### 4-4. 協作方式（一次 2 題）

```
Q9 — "什麼時候你希望 AI 挑戰你？" [跟過去矛盾時 | 有數據補充時 | 假設有問題時 | 都可以但委婉 | 不要挑戰]（多選）
Q10 — "預設紅線要調嗎？還有其他不要做的事？"（開放）
預設：(1)不幫做決定 (2)不確定就說 (3)數字附來源 (4)發現盲點要提
```

### 4-5. 組裝 CLAUDE.md

在對話中組裝，所有 [] 替換完才寫入。用 `<!-- AI-PARTNER-CONFIG:START/END -->` 包住。

內容包含（50 行內）：
1. 你服務的人（3-5 行）
2. 思考框架（3-5 行）
3. 溝通偏好（3 行）
4. 協作方式：何時挑戰 / 何時以我為主（5 行）
5. 紅線（3-5 行）
6. 進化規則（5 行固定內容）
7. 輸出規則（3 行固定：草稿寫檔案不貼對話）
8. 行為規則（什麼情境讀什麼檔案，固定內容）
9. 路由表（固定內容）
10. 記憶管理（固定內容）
11. 成長觸發表（固定內容，Phase 2/3 的自動建議條件）

### 4-6. 驗證

```bash
grep -c '\[' CLAUDE.md  # 應為 0
wc -l CLAUDE.md         # 約 50 行
```

讓使用者讀一遍確認。

---

## 階段 5：MEMORY.md

用 `<!-- MEMORY:START/END -->` 邊界標記。

```markdown
<!-- MEMORY:START -->

# [名字] 的記憶

## 用戶偏好
（隨對話自動長出來）

## Feedback
（隨糾正累積）

## 環境
| 項目 | 值 |
|------|---|
| 資料夾 | [路徑] |
| 日期 | [YYYY-MM-DD] |
| Skills symlink | [稍後] |

<!-- MEMORY:END -->
```

---

## 階段 6：vault 基礎文件

根據訪談內容建：

### vault/identity/me.md
```markdown
# [名字]
角色：[Q2]
公司：[Q3]
重心：[Q4]

## 決策風格
[Q5 展開]

## 溝通風格
[Q7+Q8]
```

### vault/context/company.md
```markdown
# [公司名]
[Q3 展開]
（後續加入產品策略、商業模式、競爭環境。有了就丟進來。）
```

---

## 階段 7：Skills Symlink

```bash
SKILLS_TARGET="$(pwd)/skills"
SKILLS_LINK="$HOME/.claude/skills"

if [ -L "$SKILLS_LINK" ]; then
  # 已是 symlink → 問使用者要不要改
  AskUserQuestion
elif [ -d "$SKILLS_LINK" ] && [ -n "$(ls -A "$SKILLS_LINK" 2>/dev/null)" ]; then
  # 有既有 skills → 問：搬過來 / 備份 / 跳過
  AskUserQuestion
elif [ -d "$SKILLS_LINK" ]; then
  rmdir "$SKILLS_LINK"
  mkdir -p "$(dirname "$SKILLS_LINK")"
  ln -s "$SKILLS_TARGET" "$SKILLS_LINK"
else
  mkdir -p "$(dirname "$SKILLS_LINK")"
  ln -s "$SKILLS_TARGET" "$SKILLS_LINK"
fi

# 驗證
ls -la "$HOME/.claude/skills"
```

更新 MEMORY.md 的 symlink 狀態。

---

## 階段 8：Git

```bash
# .gitignore
cat > .gitignore << 'EOF'
.env
*.key
*.pem
.DS_Store
vault/chatgpt-import/raw-*
EOF

# .gitattributes（防多機同步假 diff）
cat > .gitattributes << 'EOF'
* text=auto eol=lf
*.md text eol=lf
EOF

# 初始化 + 推到 private repo
git init
git add -A
git commit -m "初始化：AI 夥伴"
gh repo create [資料夾名] --private --source . --push
```

---

## 階段 9：複製 Phase 2/3 引導

確認以下檔案都在成品資料夾裡：

```bash
ls guides/10-after-action.md
ls guides/11-soul-layer.md
ls guides/12-memory-summary.md
ls guides/13-voice-and-tone.md
ls guides/14-update-identity.md
ls guides/20-routines.md
ls guides/21-vault-audit.md
ls milestones/week-1.md
ls milestones/review-template.md
```

這些是 CLAUDE.md 成長觸發表會引用的。使用者不需要知道它們存在。

---

## 階段 10：完成

告訴使用者：

> **你的 AI 夥伴建好了！**
>
> - CLAUDE.md — 它認識你了
> - MEMORY.md — 記憶系統啟動
> - vault/ — 知識庫基礎
> - Skills — insight-finder / content-drafter / git-sync 已就位
> - GitHub — 備份完成
>
> **現在關掉這個對話，開一個新的。**
> CLAUDE.md 要新 session 才會載入。
>
> 在新對話裡試試：
> - 問一個你真正在想的問題
> - 說「找 insight」丟一份資料
> - 說 /commit 備份
>
> 你不需要記任何指令。用就好，系統會在對的時間建議你升級。

---

## references/ 的角色

references/README.md 放在成品資料夾裡。裡面是進化教科書的連結：

- **想建新 Skill** → 參考女媧.skill 的方法論
- **想優化 Skill** → 參考達爾文.skill 的機制
- **想加沉澱機制** → 參考 OpenClaw 的做法
- **想改架構** → 參考雷蒙和 Vault 的設計
- **想懂 LLM 原理** → 讀 Karpathy LLM Wiki
- **想查 Claude Code 功能** → 看官方文件

Agent 在引導使用者進化時（Phase 2/3），會從這裡找方法論。

---

## 安全提醒

在整個流程的適當時機提醒使用者：
- API key、密碼、token（.env 裡的東西）不要貼進對話
- 其他工作內容都可以
