---
name: git-sync
description: |
  快速同步到 GitHub。觸發：說「/commit」「同步」「備份」「push」。
  自動 git add → 用 AI 生成 commit message → commit → push。
---

# Git Sync

## 觸發條件

使用者說以下任一：
- `/commit`
- `同步一下`
- `備份`
- `push`
- `幫我 commit`

## 執行步驟

### 1. 檢查狀態
```bash
git status
```
如果沒有任何變更，告訴使用者「沒有需要同步的變更」，結束。

### 2. 看 diff
```bash
git diff --stat
git diff --staged --stat
```

### 3. Stage 變更
```bash
git add -A
```

注意：不要 add .env 或包含密碼的檔案。如果發現敏感檔案，提醒使用者加進 .gitignore。

### 4. 生成 commit message

根據 diff 內容，生成簡短的 commit message：
- 繁體中文
- 一行，說明做了什麼
- 格式：`類型：描述`（例：`更新：CLAUDE.md 加入溝通偏好`）

### 5. Commit + Push
```bash
git commit -m "生成的 message"
git push
```

### 6. 回報
告訴使用者同步完成，列出這次包含的變更摘要。
