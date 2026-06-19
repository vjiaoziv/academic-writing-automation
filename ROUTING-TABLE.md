# 学术研究技能清单与路由表（Academic Research Route Table）

> 最后更新：2026-06-19 | 维护者：Agent

本文件列出所有与学术研究、论文写作、文献管理相关的技能和工具，并提供路由决策表。

---

## ⚠️ 版权声明与来源说明

本路由表涉及的技能和工具来自多个来源，使用前请遵守各自的许可证要求：

📦 **本仓库自创（MIT License）**
- `citation-grounded-writing` v1.2.0 — Hermes Agent (JIAOZI)
- `add-docx-comments` v1.0.0 — Hermes Agent (JIAOZI)
- `arxiv` — Hermes Agent (JIAOZI) — **独立实现**的 curl REST API 版，与 SkillHub ractorrr 版不同
- `marxist-report-word` — 霁弦 (Hermes Agent)
- `docx-punctuation-normalizer` v1.0.0 — 霁弦 (Hermes Agent)

🔸 **ARS 套件（CC-BY-NC-4.0，非商业使用）**
- 原作者：Cheng-I Wu / Imbad0202
- GitHub：https://github.com/Imbad0202/academic-research-skills
- 包含：ars-academic-paper / ars-deep-research / ars-academic-paper-reviewer / ars-academic-pipeline / ars-hub / ars-commands

🔵 **OpenDataLab 平台服务**
- `mcp_sciverse` 系列 MCP 工具 — (https://sciverse.opendatalab.com/)

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
- ~~`reference-management`~~ — 已移除（空壳技能，3个脚本死引用，功能由 academic-citation-manager 完全覆盖）
- `academic-paper-literature-analyzer` — 来源待确认
- `docx-table-merge` — 来源待确认

**核心建议：** 不要在路由表中将上述同名技能直接归为社区原作者的版权，标注为"本地修改版/独立实现"即可。

---

## 核心规则

**去AI味：** 统一使用 `avoid-ai-writing`（detect/rewrite 模式，academic 配置）

**写论文铁律：** 所有论文写作必须基于真实参考文献原文句子佐证，由 `citation-grounded-writing` 执行。首选 Sciverse（中英文+原文段落），fallback cnki（下载PDF）+ mineru（解析PDF），arxiv 补充预印本

**Word批注：** 审核论文时优先使用 `add-docx-comments` 在 .docx 中插入真实批注

---

## 一、论文写作（核心）

📦 `citation-grounded-writing` v1.2.0 — 首选：写任何论文
- 来源：本仓库自创 | 许可证：MIT
- 7阶段全流程（含PRISMA Phase 1.5），基于真实参考文献原文句子佐证，Sciverse 中英文首选 + cnki/mineru 备用

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

🔵 `mcp_sciverse` (MCP) — 首选：中英文论文检索
- 来源：OpenDataLab | 平台：https://sciverse.opendatalab.com/
- 4.65亿+记录，2832万AI-Ready全文，支持DOI/作者/期刊/年份/学科过滤
- semantic search 精准段落匹配，read_content 读取原文完整段落作为引用佐证

🔄 `cnki` — 备用：中文知网检索（**本地版为 Playwright 独立实现**，与 jirboy 的 MCP 版不同）
- 来源：本地独立实现 | Playwright自动化，8子命令，机构IP授权免登录

📦 `arxiv` — arXiv英文论文（**本地版为 curl REST API 独立实现**，与 ractorrr 版不同）
- 来源：本仓库自创 | 许可证：MIT | 基于 curl REST API

## 三、文献阅读与引用

🔵 `mcp_sciverse read_content` — 中英文论文全文阅读
- 来源：OpenDataLab | 平台：https://sciverse.opendatalab.com/
- 读取原文完整段落，按offset分页获取，可作为引用证据

🌐 `mineru` — 备用：中英文PDF/Word → Markdown解析（sciverse read_content 失败时回退）
- 来源：OpenDataLab | 许可证：AGPL-3.0 | https://github.com/opendatalab/MinerU
- API v4，支持公式/表格/OCR

🔶 `academic-citation-manager` — **唯一引用管理工具**，6种引用格式
- 来源：YouStudyeveryday via SkillHub | 许可证：MIT
- https://github.com/YouStudyeveryday/academic-citation-manager
- 覆盖 GB/T 7714/APA/MLA/Chicago/Vancouver/Harvard

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
| 验证论文每句话有文献来源 | `citation-grounding` 📦 | - | 自创 MIT，逐句→检索→验证→Evidence Pack |
| 系统综述PRISMA初筛 | `citation-grounded-writing` 📦 (Phase 1.5) | `ars-deep-research` 🔸 | 标题→摘要→全文三阶段筛选 |
| 写中文思政论文 | `citation-grounded-writing` 📦 | `cn-academic-writing` 🔶 | |
| 评审论文（同行评审） | `ars-academic-paper-reviewer` 🔸 | - | CC-BY-NC-4.0 ⚠️非商业 |
| 审核论文（检查质量） | `paper-revision-sop` 🔶 | `ars-academic-paper-reviewer` 🔸 | 来自 ClawHub liuwenqi123123 |
| 回复审稿意见 | `paper-revision-sop` 🔶 | `ars-academic-paper` 🔸 | |
| AIGC检测 | `avoid-ai-writing` 🔄 (detect模式) | - | 本地修改版 |
| 批注Word文档 | `add-docx-comments` 📦 | `paper-revision-sop` 🔶 | 自创 MIT |
| 从研究到发表全流程 | `ars-academic-pipeline` 🔸 | - | CC-BY-NC-4.0 ⚠️非商业 |
| 搜英文论文 | `mcp_sciverse` 🔵 | `arxiv` 📦 | OpenDataLab Sciverse，4.65亿记录中英双语检索+段落佐证 |
| 搜中文论文 | `mcp_sciverse` 🔵 首选 / `cnki` 🔄 备用 | - | sciverse 4.65亿覆盖中英文，cnki 知网深度补充 |
| 读论文全文 | `mcp_sciverse` 🔵 首选（read_content） | `mineru` 🌐 备用 | sciverse 段落级引用首选，mineru PDF解析备用 |
| 引用管理 | `academic-citation-manager` 🔶 | - | YouStudyeveryday MIT，唯一引用管理工具 |
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

## 十、工具概览：MCP Sciverse — OpenDataLab（**首选**）

来源：OpenDataLab (https://sciverse.opendatalab.com/) — 学术论文语义搜索引擎。

### 5 个 MCP 工具

| 工具 | 功能 | 实测状态 |
|------|------|----------|
| `search_papers` | 结构化论文搜索（作者/期刊/年份/学科/DOI过滤） | ✅ 10,000+结果 |
| `semantic_search` | 自然语言语义搜索（fast/balanced/quality三模式） | ✅ score 0.95 |
| `read_content` | 全文内容读取（按offset分页，段落级引用佐证） | ✅ 英文112KB + 中文41KB |
| `get_resource` | 获取论文图表/表格图片 | ✅ |
| `list_catalog` | 查询schema字段和运算符 | ✅ 60+字段 |

### 高级搜索能力（已验证）

| 功能 | 用法 | 验证结果 |
|------|------|----------|
| 新鲜度加权 | `freshness_boost="STRONG"`（近3年）/ `MILD`（近10年） | ✅ 返回2024-2025新论文 |
| OA状态过滤 | `filters_advanced=[{"field":"access_oa_status","operator":"FILTER_OP_IN","value":["gold","green","hybrid","diamond"]}]` | ✅ 正确过滤OA论文 |
| Top10%/1%被引 | `filters_advanced=[{"field":"citation_normalized_percentile.is_in_top_10_percent","operator":"FILTER_OP_EQ","value":true}]` | ✅ 返回FWCI 17.8高被引论文 |
| 被引百分位排序 | `sort_by_year="desc"` | ✅ |
| 语义搜索质量模式 | `semantic_search(query, mode="quality")` | ✅ LLM改写+混合检索 |

### Sciverse 功能 → 论文写作阶段映射

Sciverse MCP 覆盖 `citation-grounded-writing` 7 阶段管线的 Phase 1-6：

**Phase 1 — 搜索**（找到相关文献）
- `search_papers` 基础关键词搜索
- `search_papers` + `freshness_boost` — 最新论文优先
- `search_papers` + `language` — 中文/英文定向搜索
- `search_papers` + `type` — 指定 Review/Article/Conference
- `search_papers` + `citation_count` / `fwci` / `is_in_top_10%` — 高质量筛选
- `search_papers` + `publication_venue_type` — 只看期刊或只看会议
- `semantic_search` fast 模式 — 快速初筛

**Phase 1.5 — PRISMA 初筛**（标题→摘要→全文三阶段）
- `search_papers` + `title_contains` — 标题层筛选
- `semantic_search` balanced/quality 模式 — 摘要层语义匹配
- `search_papers` + `access_oa_status` — 排除 Closed Access（避免 read_content 404）
- `search_papers` + `page_size=50` — 批量拉取候选集
- `metadata_type=ebook` — 补充书籍类文献（教材/专著）

**Phase 2 — 阅读**（精读全文提取原文）
- `read_content` 分页读取 — 全文精读（offset+limit 循环拉取）
- `read_content` 提取原文句子 — 作为引用来源
- `get_resource` — 下载论文中的图表/数据（用于配图参考）

**Phase 3 — 大纲**（构建引用网络）
- `search_papers` + `related_works` — 关联论文发现，补全引用网络
- `search_papers` + `references` — 前向引用追踪
- `semantic_search` quality 模式 — 深度语义探索，发现潜在关联

**Phase 4 — 写作 + 引用**（逐句嵌入引用）
- `read_content` 精确 offset — 逐句提取原文（段落级定位）
- `search_papers` + `MATCH_PHRASE` — 精确短语匹配验证引用准确性
- `search_papers` + `doi` — DOI 精确定位某篇特定文献

**Phase 5 — 合规检查**（验证引用质量）
- `search_papers` + `is_in_top_1%` — 验证引用的论文是否为顶级期刊
- `search_papers` + `fwci` 范围 — 交叉验证引用影响力数据
- `semantic_search` + `source_types=["pdf"]` — 确认引用来自 PDF 全文而非网页摘要

**Phase 6 — Citation Grounding 验证**（逐句溯源）
- `semantic_search` quality 模式 — 逐句 claim 匹配检索
- `read_content` 全文验证 — 检查匹配到的原文是否支持 claim
- `get_resource` — 验证图表引用是否与原文一致

**Phase 7 — 去 AI 味 + Word 批注**（不依赖 Sciverse）
- 此阶段使用 `avoid-ai-writing` + `add-docx-comments`，不使用 Sciverse

> 核心链路：`search_papers` 找文献 → `semantic_search` 语义匹配 → `read_content` 全文精读 → `get_resource` 图表提取

### Sciverse 全功能验证报告（2026-06-19）

| 功能 | 状态 | 备注 |
|------|------|------|
| `search_papers` 基础搜索 | ✅ | 中英文均可，total_count=10,000+ |
| `search_papers` + `type` 过滤 | ✅ | Review/article/conference 等 20 种 |
| `search_papers` + `language` 过滤 | ✅ | zh/en/de/fr 等 20+ 语言 |
| `search_papers` + `access_oa_status` 过滤 | ✅ | gold/green/bronze/hybrid/diamond/closed |
| `search_papers` + `publication_venue_type` 过滤 | ✅ | journal/conference/repository 等 |
| `search_papers` + `fwci` 范围过滤 | ✅ | >=5.0 高影响力论文可筛 |
| `search_papers` + `primary_topic.domain` 过滤 | ❌ | 返回空，nested 字段需特定格式，建议用 `subjects` 替代 |
| `search_papers` + `freshness_boost` | ✅ | MILD/STRONG 可用，与 sort_by_year 互斥 |
| `search_papers` + `sort_by_year` | ✅ | asc/desc/none |
| `search_papers` + `citation_count` 范围 | ✅ | GT/GTE/LT/LTE 均可 |
| `search_papers` + `is_in_top_10_percent` | ✅ | Boolean 过滤 |
| `search_papers` + `MATCH_PHRASE` | ✅ | 精确短语匹配 |
| `search_papers` + `metadata_type=ebook` | ✅ | 图书搜索可用 |
| `semantic_search` fast 模式 | ✅ | ~200ms，score 0.91-0.95 |
| `semantic_search` balanced 模式 | ✅ | ~600ms，score 0.80-0.84 |
| `semantic_search` quality 模式 | ✅ | 2-4s，score 0.90+ |
| `semantic_search` + `source_types=["pdf"]` | ✅ | 仅 PDF 全文来源 |
| `semantic_search` + `source_types=["web"]` | ✅ | 仅网页来源 |
| `read_content` 分页读取 | ✅ | offset+limit 分段，more=true |
| `read_content` 中文论文 | ✅ | 41,367 字节 |
| `read_content` 英文论文 | ✅ | 112,594 字节 |
| `read_content` 无全文论文 | ❌ | 返回 404（Closed Access） |
| `get_resource` 图表下载 | ✅ | 需 read_content 中 image ref |
| `list_catalog` + sample_values | ✅ | 完整 schema + enum 取值 |
| `filters_advanced` FILTER_OP_IN | ✅ | 数组值匹配 |
| `filters_advanced` FILTER_OP_EQ | ✅ | 单值精确匹配 |
| `type=patent` 专利搜索 | ❌ | 不可用，无 patent 枚举值 |

### ⚠️ 使用注意事项（8 条）

1. **`freshness_boost` 与 `sort_by_year` 互斥**：不能同时使用，模糊搜索按相关性排序
2. **`filters_advanced` 运算符格式**：必须用 `FILTER_OP_IN`/`FILTER_OP_EQ`/`FILTER_OP_GT` 等，不能用 `IN`/`EQ`
3. **专利搜索不可用**：`type` 字段枚举值中无 `patent`，Sciverse 主要覆盖学术文献
4. **Closed Access 论文**：`read_content` 返回 404，需 fallback 到 cnki+mineru
5. **`primary_topic.domain` 过滤返回空**：nested 字段需特定格式，建议用 `subjects` 替代
6. **Phase 2 阅读前务必先过滤 OA**：加 `access_oa_status IN [gold,green,hybrid,diamond]` 避免 404
7. **Phase 5 合规检查用 `source_types=["pdf"]`**：确保引用来自 PDF 全文而非网页摘要
8. **Phase 6 Citation Grounding 用 `quality` 模式**：LLM 改写查询，提高 claim 匹配准确率

### 15 个官方场景案例

来源：https://sciverse.opendatalab.com/ 场景案例页（2026-06-19 验证）

| # | 场景 | 标签 | 难度 | 写论文可用性 |
|---|------|------|------|------------|
| 1 | 构建科研文献综述 Agent | Agent/RAG | 进阶 | ⭐⭐⭐ 文献综述核心流程 |
| 2 | 做科学 RAG 数据源 | RAG/Agent | 进阶 | ⭐⭐ 为LLM提供可信科学证据 |
| 3 | 查找论文全文证据 | RAG/检索 | 入门 | ⭐⭐⭐ **引用佐证核心场景** |
| 4 | 下载论文图表资源 | 多模态/检索 | 入门 | ⭐⭐ 获取论文图表 |
| 5 | 结构化论文筛选 | 检索/Agent | 进阶 | ⭐⭐⭐ **精确过滤OA论文** |
| 6 | 在Claude/Cursor/Codex接入Skill | Skill/Agent | 入门 | ⭐ 我们已在Hermes中接入 |
| 7 | 专利与文献语义探索 | 专利/检索 | 进阶 | ⚠️ 专利搜索不可用（已验证） |
| 8 | 科学问答Citation Grounding | RAG/Agent | 高级 | ⭐⭐⭐ **消除幻觉，为每句话找文献来源** |
| 9 | 论文图表提取与分析Demo | 多模态/检索 | 高级 | ⭐⭐ 图表分析辅助 |
| 10 | 论文标题相似度去重 | Agent/元数据 | 进阶 | ⭐⭐ 避免重复引用 |
| 11 | DOI/标题精确解析 | 元数据/检索 | 入门 | ⭐⭐⭐ **快速拉取元数据+全文** |
| 12 | 系统综述初筛助手 | 综述/Agent | 高级 | ⭐⭐⭐ **PRISMA-style初筛** |
| 13 | 论文可信引用包Evidence Pack | RAG/工具 | 进阶 | ⭐⭐⭐ **标准化引用格式模板** |
| 14 | 研究方向趋势扫描 | 元数据/检索 | 进阶 | ⭐⭐⭐ **近5年热度/头部期刊/高被引论文** |
| 15 | 论文阅读助手 | 工具/RAG | 入门 | ⭐⭐⭐ **分段读全文，抽取方法/数据/结论** |

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
3. **Closed Access论文**：sciverse read_content 返回404。优先选OA论文；fallback：cnki下载PDF→mineru解析
4. **SkillHub发布**：需用户完成实名认证后才可发布
5. **待确认作者**：`cn-academic-writing`、`scau-thesis-template`、`academic-paper-literature-analyzer`、`docx-table-merge` 的来源和作者尚待确认

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
- 2026-06-19: 移除 `reference-management`（空壳技能，功能由 academic-citation-manager 完全覆盖）
