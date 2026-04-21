# Skills 引導

## 什麼是 Skill？

Skill 是一份 SKILL.md 檔案。它定義了 AI 在特定場景下該怎麼做。

**本質上就是一份 SOP。** 差別在於這份 SOP 不是給人讀的，是給 AI 讀的。

### 為什麼需要 Skill？

你跟 AI 說了十次「幫我整理會議紀錄，要列出決策、待辦、隱藏 insight」。
每次都要重新解釋。第三次你就會想：**能不能教一次就好？**

Skill 就是那個「教一次就好」。

### Skill 的 Context 策略

Skill 不會一直佔著 context。只有被觸發時才載入。
所以你可以有 50 個 Skill，但每次對話只載入用到的那幾個。

## Skill 的結構

```markdown
---
name: skill-name
description: 什麼時候觸發、做什麼
---

# Skill 標題

## 觸發條件
什麼情況下啟動這個 Skill

## 執行步驟
1. 做什麼
2. 做什麼
3. 產出什麼

## 品質標準
好的產出長什麼樣
```

## 現在有什麼好用的 Skill？

### 女媧.skill — 蒸餾名人思維

把名人的思考框架變成 AI 可用的 Skill。13 位名人已蒸餾好：

- **芒格** — 逆向思考、認知偏誤、跨學科分析
- **Naval** — 槓桿、特定知識、財富定義
- **費曼** — 第一性原理拆解
- **Jobs** — 產品思維、簡化
- **Paul Graham** — 創業策略
- Musk、張一鳴、Taleb、Karpathy 等

安裝方式：把 examples/ 裡的資料夾複製到 skills/

### 同事.skill — 蒸餾真實的人

把真實的人（同事、夥伴、朋友）的思維方式蒸餾成 Skill。
GitHub 上爆紅 5000 星。證明了蒸餾一個人是完全可行的。

### 達爾文.skill — 讓 Skill 自動進化

8 維評估 + 棘輪機制。只保留進步，退步就回滾。
裝了之後，你的所有 Skill 會自動越來越好。

---
<!-- 以下是給 Claude 讀的執行指令 -->

## 執行規則

- 問使用者想裝哪些 Skill
- 從 references/nuwa-skill/examples/ 複製到 skills/
- 裝完後用使用者的真實問題試一次
- 展示怎麼切換 Skill（例：「用芒格的視角看這件事」）

## Section A：選擇 Skill

列出可用的 Skill，讓使用者選 2-3 個最想要的。
建議 CEO 先裝：芒格 + Naval + 費曼

## Section B：安裝

```bash
cp -r references/nuwa-skill/examples/munger-perspective skills/
cp -r references/nuwa-skill/examples/naval-perspective skills/
# 其他按使用者選擇
```

## Section C：試用

讓使用者提一個真正在想的問題，用剛裝的 Skill 回答。
展示切換不同 Skill 看同一個問題的效果。

完成後告訴使用者：「你現在有一個顧問團了。隨時可以切換不同的思維框架。」
