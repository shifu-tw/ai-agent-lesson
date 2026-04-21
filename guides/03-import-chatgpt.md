# 匯入 ChatGPT 資料

## 這是什麼？

把你在 ChatGPT 累積的對話搬過來。程式先處理（零 token），AI 最後分類（一次 token）。

## 事前準備

去 ChatGPT → Settings → Data Controls → Export Data → 收到 email 後下載 ZIP。

---
<!-- 以下是給 Claude 讀的執行指令 -->

## 執行規則

- 先確認使用者有 conversations.json 或 export ZIP
- 用 Bash 執行 Python 腳本，不要用 AI 讀原始對話
- 如果 Python 沒裝，引導安裝：`brew install python3`

## Section A：執行解析器

```bash
python3 tools/parse-chatgpt-export.py [使用者提供的檔案路徑] -o vault/
```

等待執行完成。告訴使用者產出了哪些檔案。

## Section B：看結果

1. 讀 vault/chatgpt-import/raw-summary.md → 跟使用者分享有趣的統計
   - 「你一共有 XX 個對話，最常聊的主題是 XX」
   - 「你的訊息平均長度是 XX，偏向 [探索型/執行型]」
2. 讀 vault/chatgpt-import/user-profile.md → 跟使用者確認推斷是否準確

## Section C：AI 分類

1. 讀 vault/chatgpt-import/classify-prompt.md
2. 根據 prompt 的指示，分析使用者的主題領域和偏好
3. 建議哪些 insight 值得放進：
   - CLAUDE.md（偏好、思考模式）
   - vault/ 的對應資料夾（知識類內容）
   - MEMORY.md（重要決策或轉折點）
4. 所有建議讓使用者確認後才寫入

## Section D：完成

告訴使用者：
- 「你過去在 ChatGPT 的積累已經搬過來了」
- 「接下來跑 onboarding 時，我會參考這些資料，不是從零認識你」
