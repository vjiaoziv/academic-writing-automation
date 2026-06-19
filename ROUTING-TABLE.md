# 学术研究技能清单与路由表（Academic Research Route Table）

> 最后更新：2026-06-19 | 维护者：Agent

本文件列出所有与学术研究、论文写作、文献管理相关的技能和工具，并提供路由决策表，指导在不同场景下如何选择和组合使用。

---

## 核心规则

### 去AI味
所有去AI味/人性化改写任务统一使用 `avoid-ai-writing` 作为首选技能。支持 detect（仅标注不修改）和 rewrite（自动改写）两种模式，6种上下文配置（academic/technical-blog/linkedin/investor-email/docs/casual），覆盖30+ AI-ism 模式检测与修复。**不再使用** `humanizer` 技能。

### 写论文铁律
所有论文写作任务，默认必须基于真实参考文献原文句子佐证。具体由 `citation-grounded-writing` 技能执行：先完整阅读参考文献全文（mineru/MCP sciverse/cnki），再逐句嵌入正文。未经读取原文的引用视为违规，最终稿中会强制删除。中文文献首选cnki，英文文献首选sciverse+arxiv，不依赖百度学术。

### Word批注
审核论文时优先在Word文档内插入真实批注（Comments），使用 `add-docx-comments` 独立技能（`scripts/add_docx_comments.py`），而非生成HTML报告。

---

## 一、论文写作（核心）

| 技能名称 | 版本 | 用途 | 关键特性 |
|---------|------|------|---------|
| `citation-grounded-writing` | v1.1.0 | ✅ **首选：写任何论文（中/英/思政/ML）** | 6阶段全流程，基于真实参考文献原文句子佐证，双路搜索（cnki中文 + sciverse英文），dense citation workflow |
| `ars-academic-paper` | v3.2.0 | 备用：12-agent全自动论文写作 | 11种模式（苏格拉底规划/经典/结构/思辨等），研究成熟度门控 |
| `cn-academic-writing` | - | 中文思政类论文格式规范 | 《马克思主义研究》期刊格式，GB/T 7714-2015 |
| `marxist-report-word` | - | 思政论文/docx自动排版 | python-docx生成，含封面/声明/摘要/正文/参考文献格式 |
| `ml-paper-writing` | - | ML/AI顶会论文 | NeurIPS/ICML/ICLR格式，实验+图表+相关工作 |
| `scau-thesis-template` | - | 华南农业大学本科毕业论文模板 | 页面设置/字体/封面/声明等完整模板 |

## 二、文献检索（入口）

| 技能/MCP | 用途 | 特点 |
|---------|------|------|
| `mcp_sciverse` (MCP) | **首选**：英文论文检索 | 10000+论文，支持DOI/作者/期刊/年份/学科过滤，semantic search精准段落匹配 |
| `cnki` | **首选**：中文知网检索 | Playwright自动化，8子命令（search/detail/download/export），机构IP授权免登录 |
| `arxiv` | 备用：arXiv英文论文 | 按关键词/作者/分类搜索 |

## 三、文献阅读与引用

| 技能/MCP | 用途 | 特点 |
|---------|------|------|
| `mcp_sciverse` `read_content` | 英文论文全文阅读 | Open Access论文直接读内容段，按offset分页获取 |
| `mineru` | 中英文PDF/Word → Markdown解析 | API v4，支持公式/表格/OCR，已配置MINERU_TOKEN |
| `academic-citation-manager` | 6种引用格式管理 | CrossRef API，GB/T 7714/APA/MLA/Chicago/Vancouver/Harvard |
| `reference-management` | GB/T 7714格式格式化 | 含 `scripts/insert_cite_word.py`（docx内插入引用标记） |

## 四、论文评审与修改

| 技能 | 用途 | 特点 |
|-----|------|------|
| `paper-revision-sop` | **首选**：审稿意见回复/论文润色 | 5阶段（审稿解析→全息诊断→Word批注→分级改写→终审），含add_docx_comments.py批注工具 |
| `avoid-ai-writing` | 去AI味检测与改写 | detect模式（标注）+ rewrite模式（改写），academic配置，30+ AI-ism模式 |
| `ars-academic-paper-reviewer` | 多审稿人模拟评审 | 7-agent评审面板，6种模式（含魔鬼代言人/编辑综合） |
| `data-integrity-audit` | 实验数据一致性验证 | CSV/Excel原始数据交叉引用审计 |
| `jiaozhen-factcheck` | 事实查证 | 对具体说法/资讯/事件查证 |

## 五、论文配图与排版

| 技能 | 用途 | 特点 |
|-----|------|------|
| `academic-figures` | 论文配图生成 | 14种学术图表，6套配色（含Okabe-Ito色盲安全），Kaplan-Meier等 |
| `minimax-docx` | Word文档生成 | 专业排版 |
| `docx-punctuation-normalizer` | 英文标点→中文标点 | 自动保留参考文献区域 |
| `docx-table-merge` | docx表格插入 | 结构化表格生成 |

## 六、深度研究（辅助）

| 技能 | 用途 | 特点 |
|-----|------|------|
| `deep-research` | 轻量级快速调研 | 多渠道搜索 + 内容分析 + 思维导图 |
| `ars-deep-research` | 结构化深度研究 | 13-agent团队，8种模式 |
| `ars-academic-pipeline` | 从研究到发表全流程 | 10阶段编排器，6个质量门 |
| `academic-paper-literature-analyzer` | 文献分析与论文框架建立 | 参考文献分析/观点提炼/框架关联 |

## 七、ARS 快捷命令集（ars-commands）

ARS 提供 16 个 `/ars-*` 快捷命令，覆盖论文写作全流程的常用操作：

| 命令 | 用途 | 调用技能 |
|------|------|---------|
| `/ars-full` | 端到端完整工作流（Stage 1→6） | `ars-academic-pipeline` |
| `/ars-plan` | 苏格拉底式逐章规划 | `ars-academic-paper` (plan模式) |
| `/ars-outline` | 详细大纲 + 证据地图 | `ars-academic-paper` (outline-only) |
| `/ars-abstract` | 双语摘要 + 关键词 | `ars-academic-paper` (abstract-only) |
| `/ars-lit-review` | 文献综述 | `ars-academic-paper` 或 `ars-deep-research` |
| `/ars-reviewer` | 同行评审面板 | `ars-academic-paper-reviewer` |
| `/ars-revision` | 修订稿 + 逐条修改说明 | `ars-academic-paper` (revision模式) |
| `/ars-revision-coach` | 修订路线图 + 回复函骨架 | `ars-academic-paper` (revision-coach) |
| `/ars-citation-check` | 引用错误报告 | `ars-academic-paper` (citation-check) |
| `/ars-format-convert` | 格式转换（LaTeX/DOCX/PDF/MD） | `ars-academic-paper` (format-convert) |
| `/ars-3w` | WHY/HOW/WHAT 三路扫描 | `ars-deep-research` (three-way-scan) |
| `/ars-rebuttal-audit` | 审计回复草稿质量 | `ars-academic-paper` (rebuttal-audit) |
| `/ars-disclosure` | AI使用声明生成 | `ars-academic-paper` (disclosure) |
| `/ars-mark-read` | 标记已读信号 | CLI脚本 |
| `/ars-unmark-read` | 取消已读标记 | CLI脚本 |
| `/ars-cache-invalidate` | 失效引用验证缓存 | CLI脚本 |

## 八、ARS Hub — 路由入口

`ars-hub` 是 ARS 套件的中心路由层，本身不执行任务，负责将用户需求路由到正确的子技能：

| 用户需求 | 路由到 |
|---------|--------|
| 做研究/文献综述/系统性回顾 | `ars-deep-research` |
| 写论文/论文修改/检查引用 | `ars-academic-paper` |
| 评审论文/同行评审模拟 | `ars-academic-paper-reviewer` |
| 从研究到发表全流程 | `ars-academic-pipeline` |
| 不确定研究方向 | `ars-deep-research` (Socratic模式) |

ARS 本地仓库路径：`C:/Users/JIAOZI/projects/academic-research-skills/`

---

## 九、路由决策表

| 需求场景 | 首选技能/工具 | 备份技能 | 说明 |
|---------|-------------|---------|------|
| 研究一个主题（深度了解） | `ars-deep-research` | `deep-research` | 13-agent团队 vs 轻量级快速响应 |
| 不确定研究方向（构思） | `brainstorming` + `deep-research` | `ars-hub` | 创意发散+信息验证 |
| 写一篇论文 | `citation-grounded-writing` | `ars-academic-paper` | 首选基于真实文献原文句子的全流程写作；备用12-agent管线 |
| 写中文思政论文 | `citation-grounded-writing` | `cn-academic-writing` | 先用citation-grounded-writing全程自动化，再按cn-academic-writing格式规范调整 |
| 评审论文（同行评审模拟） | `ars-academic-paper-reviewer` | - | 7-agent，主编+3审稿人+魔鬼代言人 |
| 审核论文（检查质量） | `paper-revision-sop` | `ars-academic-paper-reviewer` | 5阶段诊断+分级修改，审稿意见回复也用此 |
| 回复审稿意见 | `paper-revision-sop` (Phase 0 + Phase 3) | `ars-academic-paper` (revision模式) | 提取可执行项+分类优先级+分级改写 |
| AIGC检测 | `avoid-ai-writing` (detect模式) | - | 30+ AI-ism模式检测，仅标注不修改 |
| 批注论文 | `add-docx-comments` | `paper-revision-sop` (Word批注) | 在paper-revision-sop的Phase 2使用，将诊断结果写入.docx批注，引导Phase 3逐条修改 |
| 从研究到发表全流程 | `ars-academic-pipeline` | - | 10阶段编排器，含质量门 |
| 找论文/搜文献 | `mcp_sciverse` (英文) / `cnki` (中文) | `arxiv` | 中文用cnki（知网Playwright），英文用sciverse MCP |
| 读论文全文（PDF/Word） | `mineru` | `mcp_sciverse read_content` | mineru解析PDF/Word→Markdown，含公式表格OCR |
| 分析已有文献（综述/框架） | `academic-paper-literature-analyzer` | `ars-deep-research` | 帮助建立论文框架与参考文献关联 |
| 引用管理/插入参考文献 | `academic-citation-manager` | `reference-management` | 前者6格式+CrossRef API，后者GB/T 7714精细化 |
| 论文配图 | `academic-figures` | - | 14种学术图表，6套配色 |
| 润色/去AI味 | `avoid-ai-writing` (rewrite, academic) | `paper-revision-sop` | 不用humanizer。paper-revision-sop内部也已替换为avoid-ai-writing |
| 毕业论文排版（scau） | `scau-thesis-template` | - | 华南农业大学本科毕业论文模板 |
| 验证数据一致性 | `data-integrity-audit` | - | CSV/Excel原始数据与论文数据交叉引用审计 |
| 快速查证一个事实 | `jiaozhen-factcheck` | `web_search` | 对具体说法/资讯/事件查证，优于通用搜索 |
| ML/AI顶会投稿 | `ml-paper-writing` | `citation-grounded-writing` | 特殊格式要求+实验图表 |
| 格式转换（LaTeX/DOCX/PDF） | `ars-academic-paper` (format-convert) | - | 支持LaTeX↔DOCX↔PDF↔Markdown |
| 审计回复草稿 | `ars-academic-paper` (rebuttal-audit) | - | 审计rebuttal/response草稿质量 |
| 生成AI使用声明 | `ars-academic-paper` (disclosure) | - | 支持ICLR/NeurIPS/Nature/Science/ACL/EMNLP |

---

## 十、工具概览：Hermes MCP Sciverse

学术论文语义搜索引擎，无需额外安装，Hermes 内置 MCP 工具。

| 工具 | 功能 | 参数示例 |
|------|------|---------|
| `mcp_sciverse_search_papers` | 结构化论文搜索 | query, authors, year_from/to, journals, subjects |
| `mcp_sciverse_semantic_search` | 自然语言语义搜索 | query="Transformer attention mechanism", top_k=10 |
| `mcp_sciverse_read_content` | 全文内容读取 | doc_id, offset, limit |
| `mcp_sciverse_get_resource` | 获取图表/图片 | file_name（来自read_content的Markdown图片引用） |
| `mcp_sciverse_list_catalog` | 查询schema | include_sample_values=true |

## 十一、工具概览：CNKI 知网自动化

Playwright 驱动的知网自动化脚本，校园网 IP 自动授权。

```bash
cd ~/.hermes/skills/cnki/scripts && python cnki_auto.py <子命令>
```

| 子命令 | 功能 |
|--------|------|
| `search` | 关键词搜索，返回标题/作者/摘要 |
| `detail` | 获取论文详细信息 |
| `download` | PDF下载（校园网授权） |
| `export` | 导出参考文献信息 |
| `journal-search` | 期刊搜索 |
| `journal-detail` | 期刊详细信息 |
| `journal-toc` | 期刊目录 |

## 十二、工具概览：MinerU PDF解析

MinerU API v4 将 PDF/Word/PPT 转换为 Markdown。

```
已配置 MINERU_TOKEN 在 .env
POST https://mineru.net/api/v4/extract/task
→ 获取 task_id → 轮询 state=done → 下载 full_zip_url
```

## 十三、已知问题

1. **cnki PDF下载有bug**：`download`子命令中 `input()` 阻塞 + `.brief` 选择器超时。解决方法：使用 `auto-download` 模式或手动复制URL
2. **Closed Access论文**：sciverse read_content 返回404。解法：通过cnki下载PDF→用mineru解析
3. **`citation-grounded-writing` (v1.1.0)**：新建技能，尚未经过真人实战测试。Phase 1.2（下载解析）依赖外部API可用性
4. **`thesis-assistant`**：技能存在但未纳入路由表（功能与ars-hub重叠）
5. **SkillHub发布**：需用户在 SkillHub 完成实名认证后才可发布

---

## 维护记录

- 2026-06-19: 新增 `citation-grounded-writing` 作为论文写作首选，移除 `multi-academic-search`
- 2026-06-19: 确认用户偏好——所有去AI味使用 `avoid-ai-writing`，`humanizer` 不再路由
- 2026-06-19: 更新 `paper-revision-sop` 内部替换 humanizer → avoid-ai-writing
- 2026-06-19: 新增 Word文档批注（add_docx_comments.py）为论文批注首选方式
- 2026-06-19: `add-docx-comments` 独立发布为独立skill
- 2026-06-19: 补充 ars-hub、ars-commands 到路由表，新增七/八/九章
