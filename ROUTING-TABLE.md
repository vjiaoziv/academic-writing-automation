# 学术研究技能清单与路由表（Academic Research Route Table）

> 最后更新：2026-06-19 | 维护者：Agent

本文件列出所有与学术研究、论文写作、文献管理相关的技能和工具，并提供路由决策表。

---

## ⚠️ 版权声明与来源说明

本路由表涉及的技能和工具来自多个来源，使用前请遵守各自的许可证要求：

📦 **本仓库自创（MIT License）**
- `citation-grounded-writing` v1.1.0 — 由 Hermes Agent 创建
- `add-docx-comments` v1.0.0 — 由 Hermes Agent 创建
- `paper-revision-sop` — 由 Hermes Agent 创建
- `marxist-report-word` — 由霁弦 (Hermes Agent) 创建
- `docx-punctuation-normalizer` v1.0.0 — 由霁弦 (Hermes Agent) 创建

🔸 **ARS 套件（CC-BY-NC-4.0，非商业使用）**
- 原作者：Cheng-I Wu / Imbad0202
- GitHub：https://github.com/Imbad0202/academic-research-skills
- Hermes 适配层由 Hermes adaptation 完成
- 包含：ars-academic-paper / ars-deep-research / ars-academic-paper-reviewer / ars-academic-pipeline / ars-hub / ars-commands

🔵 **Hermes 平台内置（Nous Research）**
- `mcp_sciverse` 系列 MCP 工具

🔶 **ClawHub / SkillHub 社区技能（各技能保留原作者版权）**
- `cnki` (jirboy) / `arxiv` (ractorrr) / `avoid-ai-writing` (conorbrondon) / `academic-figures` (docsor1212) / `academic-citation-manager` (YouStudyeveryday, MIT) / `ml-paper-writing` (Orchestra Research, MIT) / `deep-research` (user_8e810118) / `data-integrity-audit` (user_8e810118) / `jiaozhen-factcheck` (较真查真假)

🌐 **外部 API/平台**
- `minerU` — OpenDataLab (https://github.com/opendatalab/MinerU, AGPL-3.0)
- CNKI — 中国知网 (https://cnki.net/)
- arXiv — Cornell University (https://arxiv.org/)

**使用建议：**
- 本仓库自创技能可自由使用、修改和分发（MIT）
- ARS 套件为 CC-BY-NC-4.0，**不可用于商业用途**
- SkillHub 社区技能请遵守各原作者的许可证
- 外部 API 的使用受各自服务条款约束
- 商业使用任何第三方技能前，需获取相应授权

---

## 核心规则

**去AI味：** 统一使用 `avoid-ai-writing`（detect/rewrite 模式，academic 配置），不再使用 `humanizer`

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
- 来源：SkillHub 社区 | 许可证：见原作者 | 《马克思主义研究》期刊格式，GB/T 7714-2015

📦 `marxist-report-word` — 思政论文/docx自动排版
- 来源：霁弦 (Hermes Agent) | python-docx生成，含封面/声明/摘要/正文/参考文献

🔶 `ml-paper-writing` — ML/AI顶会论文
- 来源：Orchestra Research via SkillHub | 许可证：MIT | NeurIPS/ICML/ICLR格式

🔶 `scau-thesis-template` — 华南农业大学本科毕业论文模板
- 来源：SkillHub 社区 | 许可证：见原作者 | 页面设置/字体/封面/声明等

## 二、文献检索（入口）

🔵 `mcp_sciverse` (MCP) — 首选：英文论文检索
- 来源：Hermes 平台内置（Nous Research）
- 10000+论文，支持DOI/作者/期刊/年份/学科过滤

🔶 `cnki` — 首选：中文知网检索
- 来源：jirboy (ClawHub/SkillHub) | Playwright自动化，8子命令，机构IP授权免登录

🔶 `arxiv` — 备用：arXiv英文论文
- 来源：ractorrr / Ractor (ClawHub/SkillHub) | 按关键词/作者/分类搜索

## 三、文献阅读与引用

🔵 `mcp_sciverse read_content` — 英文论文全文阅读
- 来源：Hermes 平台内置 | Open Access论文直接读内容段，按offset分页获取

🌐 `mineru` — 中英文PDF/Word → Markdown解析
- 来源：OpenDataLab | 许可证：AGPL-3.0 | https://github.com/opendatalab/MinerU
- API v4，支持公式/表格/OCR

🔶 `academic-citation-manager` — 6种引用格式管理
- 来源：YouStudyeveryday via SkillHub | 许可证：MIT
- https://github.com/YouStudyeveryday/academic-citation-manager
- CrossRef API，GB/T 7714/APA/MLA/Chicago/Vancouver/Harvard

🔶 `reference-management` — GB/T 7714格式格式化
- 来源：SkillHub 社区 | 许可证：见原作者 | 含 docx 内插入引用标记脚本

## 四、论文评审与修改

📦 `paper-revision-sop` — 首选：审稿意见回复/论文润色
- 来源：本仓库自创 | 许可证：MIT
- 5阶段（审稿解析→全息诊断→Word批注→分级改写→终审）

🔶 `avoid-ai-writing` — 去AI味检测与改写
- 来源：conorbrondon (ClawHub/SkillHub) | detect模式（标注）+ rewrite模式（改写），30+ AI-ism模式

🔸 `ars-academic-paper-reviewer` — 多审稿人模拟评审
- 来源：ARS (Cheng-I Wu / Imbad0202) | 许可证：CC-BY-NC-4.0 ⚠️非商业
- 7-agent评审面板，6种模式（含魔鬼代言人/编辑综合）

🔶 `data-integrity-audit` — 实验数据一致性验证
- 来源：user_8e810118 (SkillHub) | CSV/Excel原始数据交叉引用审计

🔶 `jiaozhen-factcheck` — 事实查证
- 来源：较真查真假（企业认证，SkillHub）| 需 API Key | 对具体说法/资讯/事件查证

## 五、论文配图与排版

🔶 `academic-figures` v1.5.0 — 论文配图生成
- 来源：docsor1212 (ClawHub/SkillHub) | 14种学术图表，6套配色（含Okabe-Ito色盲安全）

📦 `docx-punctuation-normalizer` v1.0.0 — 英文标点→中文标点
- 来源：霁弦 (Hermes Agent) | 自动保留参考文献区域

🔶 `docx-table-merge` — docx表格插入
- 来源：SkillHub 社区 | 许可证：见原作者 | 结构化表格生成

## 六、深度研究（辅助）

🔶 `deep-research` — 轻量级快速调研
- 来源：user_8e810118 (SkillHub) | 多渠道搜索 + 内容分析 + 思维导图

🔸 `ars-deep-research` — 结构化深度研究
- 来源：ARS (Cheng-I Wu / Imbad0202) | 许可证：CC-BY-NC-4.0 ⚠️非商业 | 13-agent团队

🔸 `ars-academic-pipeline` — 从研究到发表全流程
- 来源：ARS (Cheng-I Wu / Imbad0202) | 许可证：CC-BY-NC-4.0 ⚠️非商业 | 10阶段编排器

🔶 `academic-paper-literature-analyzer` — 文献分析与论文框架建立
- 来源：SkillHub 社区 | 许可证：见原作者

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

## 九、路由决策表

**研究一个主题（深度了解）**
- 首选：ars-deep-research 🔸（CC-BY-NC-4.0 ⚠️非商业）
- 备份：deep-research 🔶

**不确定研究方向（构思）**
- 首选：brainstorming + deep-research 🔶
- 备份：ars-hub 🔸

**写一篇论文**
- 首选：citation-grounded-writing 📦（基于真实文献原文句子，MIT）
- 备份：ars-academic-paper 🔸（12-agent管线，CC-BY-NC-4.0 ⚠️非商业）

**写中文思政论文**
- 首选：citation-grounded-writing 📦
- 备份：cn-academic-writing 🔶

**评审论文（同行评审模拟）**
- 首选：ars-academic-paper-reviewer 🔸（CC-BY-NC-4.0 ⚠️非商业）

**审核论文（检查质量）**
- 首选：paper-revision-sop 📦（MIT）
- 备份：ars-academic-paper-reviewer 🔸

**回复审稿意见**
- 首选：paper-revision-sop 📦（MIT）
- 备份：ars-academic-paper 🔸 (revision模式)

**AIGC检测**
- 首选：avoid-ai-writing 🔶 (detect模式)

**批注论文**
- 首选：add-docx-comments 📦（MIT）
- 备份：paper-revision-sop 📦

**从研究到发表全流程**
- 首选：ars-academic-pipeline 🔸（CC-BY-NC-4.0 ⚠️非商业）

**找论文/搜文献**
- 首选：mcp_sciverse 🔵 (英文) / cnki 🔶 (中文)
- 备份：arxiv 🔶

**读论文全文（PDF/Word）**
- 首选：mineru 🌐（AGPL-3.0）
- 备份：mcp_sciverse read_content 🔵

**分析已有文献（综述/框架）**
- 首选：academic-paper-literature-analyzer 🔶
- 备 backup：ars-deep-research 🔸

**引用管理/插入参考文献**
- 首选：academic-citation-manager 🔸（MIT, YouStudyeveryday）
- 备份：reference-management 🔶

**论文配图**
- 首选：academic-figures 🔶（docsor1212）

**润色/去AI味**
- 首选：avoid-ai-writing 🔶 (rewrite, academic, conorbrondon)
- 备份：paper-revision-sop 📦

**毕业论文排版（scau）**
- 首选：scau-thesis-template 🔶

**验证数据一致性**
- 首选：data-integrity-audit 🔶 (user_8e810118)

**快速查证一个事实**
- 首选：jiaozhen-factcheck 🔶 (较真查真假)
- 备份：web_search

**ML/AI顶会投稿**
- 首选：ml-paper-writing 🔶 (Orchestra Research, MIT)
- 备份：citation-grounded-writing 📦

**格式转换（LaTeX/DOCX/PDF）**
- 首选：ars-academic-paper 🔸

**审计回复草稿**
- 首选：ars-academic-paper 🔸

**生成AI使用声明**
- 首选：ars-academic-paper 🔸

> 📦 = 本仓库自创（MIT）| 🔸 = ARS 套件（CC-BY-NC-4.0，非商业）| 🔵 = Hermes 内置 MCP | 🔶 = SkillHub 社区 | 🌐 = 外部 API

---

## 十、工具概览：Hermes MCP Sciverse

来源：Hermes 平台内置 MCP 工具（Nous Research）

- `mcp_sciverse_search_papers` — 结构化论文搜索
- `mcp_sciverse_semantic_search` — 自然语言语义搜索
- `mcp_sciverse_read_content` — 全文内容读取
- `mcp_sciverse_get_resource` — 获取图表/图片
- `mcp_sciverse_list_catalog` — 查询schema

## 十一、工具概览：CNKI 知网自动化

来源：jirboy (ClawHub/SkillHub) | 目标平台：中国知网 (https://cnki.net/)
注意：CNKI 内容受知网版权保护，使用需遵守知网服务条款

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
官网：https://mineru.net/ | API文档：https://mineru.net/apiManage/docs

```
POST https://mineru.net/api/v4/extract/task
→ 获取 task_id → 轮询 state=done → 下载 full_zip_url
```

---

## 十三、已知问题

1. **cnki PDF下载有bug**：input() 阻塞 + .brief 选择器超时。解决：使用 auto-download 模式或手动复制URL
2. **Closed Access论文**：sciverse read_content 返回404。解法：通过cnki下载PDF→用mineru解析
3. **citation-grounded-writing v1.1.0**：新建技能，尚未经过真人实战测试
4. **thesis-assistant**：技能存在但未纳入路由表（功能与ars-hub重叠）
5. **SkillHub发布**：需用户完成实名认证后才可发布

---

## 维护记录

- 2026-06-19: 新增 citation-grounded-writing 作为论文写作首选，移除 multi-academic-search
- 2026-06-19: 确认用户偏好——所有去AI味使用 avoid-ai-writing，humanizer 不再路由
- 2026-06-19: 更新 paper-revision-sop 内部替换 humanizer → avoid-ai-writing
- 2026-06-19: 新增 Word文档批注（add_docx_comments.py）为论文批注首选方式
- 2026-06-19: add-docx-comments 独立发布为独立skill
- 2026-06-19: 补充 ars-hub、ars-commands 到路由表
- 2026-06-19: **全面标注所有技能和工具的来源与许可证**
- 2026-06-19: **通过 SkillHub 查证每个社区技能的真实作者（conorbrondon/jirboy/ractorrr/docsor1212/YouStudyeveryday/user_8e810118/较真查真假）**
