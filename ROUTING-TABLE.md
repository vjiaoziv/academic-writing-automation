# 学术研究技能清单与路由表（Academic Research Route Table）

> 最后更新：2026-06-19 | 维护者：Agent

本文件列出所有与学术研究、论文写作、文献管理相关的技能和工具，并提供路由决策表。

---

## ⚠️ 版权声明与来源说明

本路由表涉及的技能和工具来自多个来源，使用前请遵守各自的许可证要求：

📦 **本仓库自创（MIT License）**
- `citation-grounded-writing` v1.1.0 — Hermes Agent (JIAOZI)
- `add-docx-comments` v1.0.0 — Hermes Agent (JIAOZI)
- `arxiv` — Hermes Agent (JIAOZI) — **独立实现**的 curl REST API 版，与 SkillHub ractorrr 版不同
- `marxist-report-word` — 霁弦 (Hermes Agent)
- `docx-punctuation-normalizer` v1.0.0 — 霁弦 (Hermes Agent)

🔸 **ARS 套件（CC-BY-NC-4.0，非商业使用）**
- 原作者：Cheng-I Wu / Imbad0202
- GitHub：https://github.com/Imbad0202/academic-research-skills
- 包含：ars-academic-paper / ars-deep-research / ars-academic-paper-reviewer / ars-academic-pipeline / ars-hub / ars-commands

🔵 **Hermes 平台内置（Nous Research）**
- `mcp_sciverse` 系列 MCP 工具

🔶 **ClawHub / SkillHub 社区技能（从社区下载安装，保留原作者版权）**
- `academic-figures` — docsor1212 (ClawHub)
- `academic-citation-manager` — YouStudyeveryday, MIT (ClawHub/GitHub)
- `paper-revision-sop` — liuwenqi123123 (ClawHub) — **纠错：之前误标为自创，实际来自 ClawHub**
- `data-integrity-audit` — user_8e810118 (SkillHub)
- `jiaozhen-factcheck` — 较真查真假 (SkillHub，企业认证)

🌐 **外部 API/平台**
- `mineru` — OpenDataLab (https://github.com/opendatalab/MinerU, AGPL-3.0)
- CNKI — 中国知网 (https://cnki.net/)
- arXiv — Cornell University (https://arxiv.org/)

🔄 **同名不同实现的本地技能（下面的技能名称与 SkillHub 同名，但本地是修改版或独立实现，代码不同）**
- `avoid-ai-writing` — 本地版是含中文路由表的修改版（原版：conorbrondon v3.10.0）
- `cnki` — 本地版是 Python Playwright 实现（原版：jirboy 的 MCP Chrome DevTools 版）
- `deep-research` — 本地版是实事求是为原则的 Phases 阶段版（原版：user_8e810118 的问题优先 Steps 版）
- `ml-paper-writing` — 本地版标注 Orchestra Research MIT（需确认是否为原版）
- `cn-academic-writing` — 来源待确认
- `scau-thesis-template` — 来源待确认
- `reference-management` — 来源待确认
- `academic-paper-literature-analyzer` — 来源待确认
- `docx-table-merge` — 来源待确认

**核心建议：** 不要在路由表中将上述同名技能直接归为社区原作者的版权，标注为"本地修改版/独立实现"即可。

---

## 核心规则

**去AI味：** 统一使用 `avoid-ai-writing`（detect/rewrite 模式，academic 配置）

**写论文铁律：** 所有论文写作必须基于真实参考文献原文句子佐证，由 `citation-grounded-writing` 执行。中文文献走 cnki，英文文献走 sciverse+arxiv

**Word批注：** 审核论文时优先使用 `add-docx-comments` 在 .docx 中插入真实批注

---

## 一、论文写作（核心）

📦 `citation-grounded-writing` v1.1.0 — 首选：写任何论文
- 来源：本仓库自创 | 许可证：MIT
- 6阶段全流程，基于真实参考文献原文句子佐证，双路搜索（cnki中文 + sciverse英文）

🔸 `ars-academic-paper` v3.2.0 — 备用：12-agent全自动论文写作
- 来源：ARS (Cheng-I Wu / Imbad0202) | 许可证：CC-BY-NC-4.0 ⚠️非商业
- 11种模式（苏格拉底规划/经典/结构/思辨等）

🔶 `cn-academic-writing` — 中文思政类论文格式规范
- 来源：SkillHub 社区（作者待确认）| 《马克思主义研究》期刊格式，GB/T 7714-2015

📦 `marxist-report-word` — 思政论文/docx自动排版
- 来源：霁弦 (Hermes Agent) | 许可证：MIT | python-docx生成，含封面/声明/摘要/正文/参考文献

🔶 `ml-paper-writing` — ML/AI顶会论文
- 来源：Orchestra Research via SkillHub（需确认是否原版） | 许可证：MIT | NeurIPS/ICML/ICLR格式

🔶 `scau-thesis-template` — 华南农业大学本科毕业论文模板
- 来源：SkillHub 社区（作者待确认） | 页面设置/字体/封面/声明等

## 二、文献检索（入口）

🔵 `mcp_sciverse` (MCP) — 首选：英文论文检索
- 来源：Hermes 平台内置（Nous Research）
- 10000+论文，支持DOI/作者/期刊/年份/学科过滤

🔄 `cnki` — 首选：中文知网检索（**本地版为 Playwright 独立实现**，与 jirboy 的 MCP 版不同）
- 来源：本地独立实现 | Playwright自动化，8子命令，机构IP授权免登录

📦 `arxiv` — arXiv英文论文（**本地版为 curl REST API 独立实现**，与 ractorrr 版不同）
- 来源：本仓库自创 | 许可证：MIT | 基于 curl REST API

## 三、文献阅读与引用

🔵 `mcp_sciverse read_content` — 英文论文全文阅读
- 来源：Hermes 平台内置 | Open Access论文直接读内容段

🌐 `mineru` — 中英文PDF/Word → Markdown解析
- 来源：OpenDataLab | 许可证：AGPL-3.0 | https://github.com/opendatalab/MinerU
- API v4，支持公式/表格/OCR

🔶 `academic-citation-manager` — 6种引用格式管理
- 来源：YouStudyeveryday via SkillHub | 许可证：MIT
- https://github.com/YouStudyeveryday/academic-citation-manager

🔶 `reference-management` — GB/T 7714格式格式化
- 来源：SkillHub 社区（作者待确认）

## 四、论文评审与修改

🔶 `paper-revision-sop` — 首选：审稿意见回复/论文润色
- 来源：liuwenqi123123 (ClawHub) | ⚠️ **纠错：来自 ClawHub，非本仓库自创**
- 5阶段（审稿解析→全息诊断→Word批注→分级改写→终审）

🔄 `avoid-ai-writing` — 去AI味检测与改写
- 来源：本地修改版（原版：conorbrondon / ClawHub v3.10.0）
- 本地版含中文路由表，去掉了 Voice Profiles 功能

🔸 `ars-academic-paper-reviewer` — 多审稿人模拟评审
- 来源：ARS (Cheng-I Wu / Imbad0202) | 许可证：CC-BY-NC-4.0 ⚠️非商业
- 7-agent评审面板，6种模式

🔶 `data-integrity-audit` — 实验数据一致性验证
- 来源：user_8e810118 (SkillHub)

🔶 `jiaozhen-factcheck` — 事实查证
- 来源：较真查真假（企业认证，SkillHub）| 需 API Key

## 五、论文配图与排版

🔶 `academic-figures` v1.5.0 — 论文配图生成
- 来源：docsor1212 (ClawHub/SkillHub) | 14种学术图表，6套配色

📦 `docx-punctuation-normalizer` v1.0.0 — 英文标点→中文标点
- 来源：霁弦 (Hermes Agent) | 许可证：MIT | 自动保留参考文献区域

🔶 `docx-table-merge` — docx表格插入
- 来源：SkillHub 社区（作者待确认）

## 六、深度研究（辅助）

🔄 `deep-research` — 轻量级快速调研
- 来源：本地独立实现（原版：user_8e810118 的 SkillHub 版）
- 本地版以实事求是为原则，Phases 阶段式工作流

🔸 `ars-deep-research` — 结构化深度研究
- 来源：ARS (Cheng-I Wu / Imbad0202) | 许可证：CC-BY-NC-4.0 ⚠️非商业 | 13-agent团队

🔸 `ars-academic-pipeline` — 从研究到发表全流程
- 来源：ARS (Cheng-I Wu / Imbad0202) | 许可证：CC-BY-NC-4.0 ⚠️非商业 | 10阶段编排器

🔶 `academic-paper-literature-analyzer` — 文献分析与论文框架建立
- 来源：SkillHub 社区（作者待确认）

## 七、ARS 快捷命令集（ars-commands）

来源：ARS v3.13.0 (Cheng-I Wu / Imbad0202) | 许可证：CC-BY-NC-4.0 ⚠️非商业

- `/ars-full` → 端到端完整工作流 → ars-academic-pipeline
- `/ars-plan` → 苏格拉底式逐章规划 → ars-academic-paper (plan)
- `/ars-outline` → 详细大纲 + 证据地图 → ars-academic-paper (outline-only)
- `/ars-abstract` → 双语摘要 + 关键词 → ars-academic-paper (abstract-only)
- `/ars-lit-review` → 文献综述 → ars-academic-paper / ars-deep-research
- `/ars-reviewer` → 同行评审面板 → ars-academic-paper-reviewer
- `/ars-revision` → 修订稿 + 逐条修改说明 → ars-academic-paper (revision)
- `/ars-revision-coach` → 修订路线图 + 回复函骨架 → ars-academic-paper (revision-coach)
- `/ars-citation-check` → 引用错误报告 → ars-academic-paper (citation-check)
- `/ars-format-convert` → 格式转换 → ars-academic-paper (format-convert)
- `/ars-3w` → WHY/HOW/WHAT 三路扫描 → ars-deep-research (three-way-scan)
- `/ars-rebuttal-audit` → 审计回复草稿 → ars-academic-paper (rebuttal-audit)
- `/ars-disclosure` → AI使用声明 → ars-academic-paper (disclosure)
- `/ars-mark-read` / `/ars-unmark-read` / `/ars-cache-invalidate` → CLI脚本

## 八、ARS Hub — 路由入口

来源：ARS v3.13.0 (Cheng-I Wu / Imbad0202) | 许可证：CC-BY-NC-4.0 ⚠️非商业
本地仓库：`C:/Users/JIAOZI/projects/academic-research-skills/`

- 做研究/文献综述 → ars-deep-research
- 写论文/修改/检查引用 → ars-academic-paper
- 评审论文/同行评审模拟 → ars-academic-paper-reviewer
- 从研究到发表全流程 → ars-academic-pipeline
- 不确定研究方向 → ars-deep-research (Socratic模式)

---

## 九、路由决策表（含来源标注）

| 需求场景 | 首选技能/工具 | 备份 | 说明 |
|---------|-------------|------|------|
| 研究一个主题 | `ars-deep-research` 🔸 | `deep-research` 🔄 | ARS 13-agent vs 本地独立版 |
| 不确定研究方向 | `brainstorming` + `deep-research` 🔄 | `ars-hub` 🔸 | |
| **写一篇论文** | `citation-grounded-writing` 📦 | `ars-academic-paper` 🔸 | **首选基于真实文献的自创 MIT 技能** |
| 写中文思政论文 | `citation-grounded-writing` 📦 | `cn-academic-writing` 🔶 | |
| 评审论文（同行评审） | `ars-academic-paper-reviewer` 🔸 | - | CC-BY-NC-4.0 ⚠️非商业 |
| 审核论文（检查质量） | `paper-revision-sop` 🔶 | `ars-academic-paper-reviewer` 🔸 | 来自 ClawHub liuwenqi123123 |
| 回复审稿意见 | `paper-revision-sop` 🔶 | `ars-academic-paper` 🔸 | |
| AIGC检测 | `avoid-ai-writing` 🔄 (detect模式) | - | 本地修改版 |
| 批注Word文档 | `add-docx-comments` 📦 | `paper-revision-sop` 🔶 | 自创 MIT |
| 从研究到发表全流程 | `ars-academic-pipeline` 🔸 | - | CC-BY-NC-4.0 ⚠️非商业 |
| 搜英文论文 | `mcp_sciverse` 🔵 | `arxiv` 📦 | sciverse 是 Hermes 内置 MCP |
| 搜中文论文 | `cnki` 🔄 | - | 本地 Playwright 独立实现 |
| 读论文全文 | `mineru` 🌐 | `mcp_sciverse read_content` 🔵 | AGPL-3.0 |
| 引用管理 | `academic-citation-manager` 🔶 | `reference-management` 🔶 | YouStudyeveryday MIT |
| 论文配图 | `academic-figures` 🔶 | - | docsor1212 |
| 润色/去AI味 | `avoid-ai-writing` 🔄 (rewrite, academic) | `paper-revision-sop` 🔶 | |
| 毕业论文排版（scau） | `scau-thesis-template` 🔶 | - | |
| 验证数据一致性 | `data-integrity-audit` 🔶 | - | user_8e810118 |
| 事实查证 | `jiaozhen-factcheck` 🔶 | `web_search` | 较真查真假（需 API Key） |
| ML/AI顶会投稿 | `ml-paper-writing` 🔶 | `citation-grounded-writing` 📦 | Orchestra Research MIT |
| 格式转换 | `ars-academic-paper` 🔸 | - | CC-BY-NC-4.0 ⚠️非商业 |
| 审计回复草稿 | `ars-academic-paper` 🔸 | - | CC-BY-NC-4.0 ⚠️非商业 |
| 生成AI使用声明 | `ars-academic-paper` 🔸 | - | CC-BY-NC-4.0 ⚠️非商业 |

> 📦 = 本仓库自创（MIT）| 🔸 = ARS 套件（CC-BY-NC-4.0，非商业）| 🔵 = Hermes 内置 MCP | 🔶 = SkillHub 社区 | 🌐 = 外部 API | 🔄 = 同名不同实现（代码与 SkillHub 不同）

---

## 十、工具概览：Hermes MCP Sciverse

来源：Hermes 平台内置 MCP 工具（Nous Research）

- `mcp_sciverse_search_papers` — 结构化论文搜索
- `mcp_sciverse_semantic_search` — 自然语言语义搜索
- `mcp_sciverse_read_content` — 全文内容读取
- `mcp_sciverse_get_resource` — 获取图表/图片
- `mcp_sciverse_list_catalog` — 查询schema

## 十一、工具概览：CNKI 知网自动化（本地 Playwright 独立实现）

来源：本地独立实现（与 jirboy 的 MCP Chrome DevTools 版本不同）

```bash
cd ~/.hermes/skills/cnki/scripts && python cnki_auto.py <子命令>
```

- `search` — 关键词搜索
- `detail` — 论文详情
- `download` — PDF下载（校园网授权）
- `export` — 导出参考文献
- `journal-search` / `journal-detail` / `journal-toc` — 期刊操作

## 十二、工具概览：MinerU PDF解析

来源：OpenDataLab (AGPL-3.0) | https://github.com/opendatalab/MinerU
官网：https://mineru.net/

```
POST https://mineru.net/api/v4/extract/task
→ 获取 task_id → 轮询 state=done → 下载 full_zip_url
```

---

## 十三、已知问题

1. **同名技能混淆**（本文件已标记🔄）：`avoid-ai-writing`、`cnki`、`arxiv`、`deep-research` 的本地实现与 SkillHub 同名版代码不同
2. **cnki PDF下载有bug**：input() 阻塞 + .brief 选择器超时。使用 auto-download 模式或手动复制URL
3. **Closed Access论文**：sciverse read_content 返回404。解法：通过cnki下载PDF→用mineru解析
4. **citation-grounded-writing v1.1.0**：新建技能，尚未经过真人实战测试
5. **SkillHub发布**：需用户完成实名认证后才可发布
6. **待确认作者**：`cn-academic-writing`、`scau-thesis-template`、`reference-management`、`academic-paper-literature-analyzer`、`docx-table-merge` 的来源和作者尚待确认
7. `paper-revision-sop` 已从本仓库自创（MIT）更正为 ClawHub 社区技能（liuwenqi123123）

---

## 维护记录

- 2026-06-19: 新增 citation-grounded-writing 作为论文写作首选
- 2026-06-19: 所有去AI味路由转向 avoid-ai-writing，不再路由 humanizer
- 2026-06-19: 补充 ars-hub、ars-commands 到路由表
- 2026-06-19: 全面标注所有技能来源与许可证
- **2026-06-19: 【版权纠错】**
  - `paper-revision-sop` 从「自创 MIT」更正为「ClawHub liuwenqi123123」
  - `arxiv` 从「ractorrr 社区技能」更正为「本仓库自创 MIT」（独立 curl 实现）
  - `cnki`、`avoid-ai-writing`、`deep-research` 标记为🔄同名不同实现
  - 路由决策表每行增加来源图标前缀
  - 新增「同名不同实现」分类说明
