# References

Agent 遇到深入問題時搜尋用的知識後盾。以下資料不包含在 repo 中，請自行 clone 或下載。

## 參考資料連結

| 資料 | 用途 | 連結 |
|------|------|------|
| **Claude Code 官方文件** | Claude Code 所有功能的完整文件 | https://code.claude.com/docs/en/overview |
| **雷蒙 Claude Code 課** | Agent 架構參考、引導式 onboarding、Skill 設計 | https://github.com/lifehacker-tw/claude-code-mini-course |
| **Vault for Founders** | 創業家 AI 知識庫框架、Agent-centric 寫法 | https://github.com/cwlin0131/Vault-for-Founders |
| **女媧.skill** | 蒸餾名人思維框架（芒格、Naval、Jobs 等 13 位） | https://github.com/alchaincyf/nuwa-skill |
| **同事.skill** | 蒸餾真實的人（同事、夥伴）成 AI Skill | https://github.com/titanwings/colleague-skill |
| **達爾文.skill** | Skill 自動進化系統（8 維評估 + 棘輪機制） | https://github.com/alchaincyf/darwin-skill |
| **Google Workspace CLI** | GWS CLI 完整文件，打通 Gmail/Calendar/Drive | https://github.com/googleworkspace/cli |
| **Hermes Agent** | 自主 Agent 架構參考（進階） | https://github.com/NousResearch/hermes-agent |
| **OpenClaw** | 多通道 Agent + 做夢/沉澱機制（進階） | https://github.com/openclaw/openclaw |
| **QMD** | 本地知識搜尋引擎（進階） | https://github.com/tobi/qmd |
| **Karpathy LLM Wiki** | LLM 運作原理、限制、最佳實踐 | https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f |
| **better-rm** | 安全刪除工具，rm 改成移到垃圾桶 | https://github.com/doggy8088/better-rm |

## 本地使用

如果需要讓 Agent 能搜尋這些資料，clone 到本地 references/ 資料夾：

```bash
cd references/
git clone https://github.com/lifehacker-tw/claude-code-mini-course.git
git clone https://github.com/cwlin0131/Vault-for-Founders.git
git clone https://github.com/alchaincyf/nuwa-skill.git
git clone https://github.com/titanwings/colleague-skill.git
git clone https://github.com/alchaincyf/darwin-skill.git
git clone https://github.com/googleworkspace/cli.git gws-cli
git clone https://github.com/NousResearch/hermes-agent.git
git clone https://github.com/openclaw/openclaw.git
git clone https://github.com/tobi/qmd.git
```

> 這些 repo 已在 .gitignore 中排除，不會被推到 GitHub。
