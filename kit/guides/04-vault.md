# 知識庫設定

## 這是什麼？

vault/ 是你的 AI 夥伴的知識庫。丟文件進去，它就能搜尋和引用。
不需要一次填滿。用的時候自然會長。

---
<!-- 以下是給 Claude 讀的執行指令 -->

## 資料夾結構

```
vault/
├── company/     — 公司策略、產品、團隊
├── industry/    — 產業觀察、競品、趨勢
├── meetings/    — 會議紀錄
└── personal/    — 個人思考、靈感、筆記
```

## 怎麼餵資料

### 直接丟檔案
把 .md、.txt、.pdf 丟進對應資料夾就好。

### 從 Google Drive 拉
```bash
gws drive files list --params '{"q": "name contains \"關鍵字\""}'
gws drive files export [fileId] --mimeType text/plain > vault/company/檔名.md
```

### 從網頁抓
```bash
curl -s [URL] | 讓 Agent 整理成 markdown 存進 vault/
```

### 口述
直接跟 Agent 說你在想什麼，讓它整理後存進 vault/personal/。

## Context 策略

vault/ 裡的資料不會每次對話都載入。
Agent 會在需要時搜尋，只拉相關的內容進 context。
這是為了保持 context 乾淨。
