# 安裝引導

## 這是什麼？

這份引導會幫你安裝 Claude Code 和 Google Workspace CLI。
跟 Claude 說「幫我跑 01-setup」，它會帶你完成。

---
<!-- 以下是給 Claude 讀的執行指令 -->

## 執行規則

- 所有需要使用者輸入的地方用 AskUserQuestion 工具
- 每一步完成後確認再進下一步
- 如果某步失敗，提供排錯建議，不要跳過

## Section A：確認環境

1. 確認作業系統是 macOS
2. 確認有 Homebrew（如果沒有，引導安裝：`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`)
3. 確認已登入 Claude Pro 帳號

## Section B：建立工作資料夾

1. 問使用者：「你想叫這個資料夾什麼名字？這會是你的 AI 夥伴的家。」
2. 問使用者存放位置：
   - A) iCloud（推薦）→ `~/Library/Mobile Documents/com~apple~CloudDocs/[名字]`
     - 多台 Apple 裝置自動同步（iPhone、iPad、其他 Mac）
     - 自帶雲端備份
   - B) Documents → `~/Documents/[名字]`
     - 單機使用，穩定不會被動到
   - 不建議放桌面：桌面是暫存區，容易被雜物淹沒，macOS Stacks 可能收起來
3. 在選定位置建立資料夾
4. 把安裝包的所有內容複製進去

## Section C：安裝工具

依序安裝，每個說明為什麼：

### gh（GitHub CLI）
```bash
brew install gh
```
為什麼：讓 Agent 幫你建 repo、備份、版本控制。不用開瀏覽器。

### gws（Google Workspace CLI）
```bash
brew install googleworkspace-cli
```
為什麼：讓 Agent 讀你的信、行事曆、Drive。一個工具打通 Google 全家桶。CLI 取資料零 token。

### better-rm（安全刪除）
```bash
curl -sSL https://raw.githubusercontent.com/doggy8088/better-rm/main/install.sh | bash
source ~/.zshrc
```
為什麼：Agent 會用 rm 刪檔案。裝了這個，刪除改成移到垃圾桶，誤刪可以救回來。

確認都裝好：
```bash
gh --version
gws --version
rm --version  # 應該顯示 better-rm
```

## Section D：GitHub 認證

```bash
gh auth login
```
- 選 GitHub.com
- 選 HTTPS
- 選 Login with a web browser
- 如果使用者沒有 GitHub 帳號，引導到 https://github.com/signup 先建

## Section E：GWS 認證

### 路線 1：有 gcloud CLI
```bash
gws auth setup
```

### 路線 2：沒有 gcloud（手動）
1. 引導使用者開 https://console.cloud.google.com/
2. 建新專案（或選現有的）
3. OAuth 同意畫面 → External → 加自己 email 為測試者
4. 建立憑證 → OAuth client → Desktop app → 下載 JSON
5. 存到 `~/.config/gws/client_secret.json`
6. 執行 `gws auth login -s gmail,calendar,drive`
7. 瀏覽器彈出授權頁面 → 核准

### 如果遇到「Access blocked」
- 回到 OAuth 同意畫面，確認有加自己為測試者
- 確認 Gmail API、Calendar API、Drive API 有啟用

## Section F：驗證

依序執行，每個都要成功：
```bash
gws gmail +triage        # 看到信件摘要
gws calendar +agenda     # 看到今天行程
gws drive files list --params '{"pageSize": 3}'  # 看到檔案
```

全部成功後告訴使用者：「安裝完成。你的 AI 夥伴現在能讀你的信和行事曆了。」

## Section F：安全提醒

告訴使用者：
- API key、密碼、token（.env 裡的東西）不要直接貼進對話
- 其他工作內容都可以正常使用
