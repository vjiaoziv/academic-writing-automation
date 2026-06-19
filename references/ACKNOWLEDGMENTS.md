# 致谢与来源说明（Acknowledgments & Sources）

本仓库的学术写作工具链整合了多个开源社区和第三方服务，特此致谢。

---

## 本仓库自创技能（MIT License）

| 技能 | 作者 | 许可证 | 说明 |
|------|------|--------|------|
| `citation-grounded-writing` v1.1.0 | Hermes Agent (JIAOZI) | MIT | 全自动论文写作技能 |
| `add-docx-comments` v1.0.0 | Hermes Agent (JIAOZI) | MIT | Word文档批注工具 |
| `arxiv` | Hermes Agent (JIAOZI) | MIT | 基于 curl REST API 的 arXiv 搜索（独立实现，与 ractorrr 的版本不同） |
| `marxist-report-word` | 霁弦 (Hermes Agent) | MIT | 思政论文docx排版 |
| `docx-punctuation-normalizer` v1.0.0 | 霁弦 (Hermes Agent) | MIT | 英文标点→中文标点 |

你可以自由使用、修改和分发上述技能。

> ⚠️ **特别说明**：`arxiv` 是本仓库独立实现的 curl 版本，与 SkillHub 上 ractorrr 的 arXiv Research Assistant（含 MongoDB）不是同一个代码。`cnki` 也是本地独立实现的 Playwright 版本，与 jirboy 的 MCP Chrome DevTools 版本不同。

---

## ARS (Academic Research Skills) 套件

ARS 由 **Cheng-I Wu / Imbad0202** 开发并维护。

| 技能 | 版本 | 作者 |
|------|------|------|
| `ars-hub` | v3.13.0 | Cheng-I Wu / Imbad0202 |
| `ars-commands` | v3.13.0 | Cheng-I Wu / Imbad0202 |
| `ars-academic-paper` | v3.2.0 | Cheng-I Wu / Imbad0202 |
| `ars-academic-paper-reviewer` | - | Cheng-I Wu / Imbad0202 |
| `ars-academic-pipeline` | - | Cheng-I Wu / Imbad0202 |
| `ars-deep-research` | - | Cheng-I Wu / Imbad0202 |

- **许可证：** CC-BY-NC-4.0（**非商业使用**）
- **GitHub 仓库：** https://github.com/Imbad0202/academic-research-skills
- **注意：** 商业使用前必须获取授权。

---

## ClawHub 社区技能（与本地安装版本一致）

以下技能来自 [ClawHub](https://clawhub.com/)，本地安装即为原作者的版本：

| 技能 | 作者 | ClawHub 链接 | 许可证 |
|------|------|-------------|--------|
| `academic-figures` v1.5.0 | docsor1212 | https://clawhub.com/skills/academic-figures | 见原作者 |
| `academic-citation-manager` v1.0.0 | YouStudyeveryday | https://github.com/YouStudyeveryday/academic-citation-manager | MIT |
| `paper-revision-sop` | liuwenqi123123 | https://clawhub.ai/liuwenqi123123/paper-revision-sop | 见原作者 |

> ⚠️ **修正**：`paper-revision-sop` 来自 ClawHub 作者 liuwenqi123123，之前误标为本仓库自创，现已更正。本仓库不拥有其版权。

---

## 同名但不同实现的本地技能

以下技能的**名称**与 SkillHub/ClawHub 同名，但本地安装的代码是独立实现，内容不同：

| 本地技能名称 | 本地实现特点 | SkillHub 同名版本 | 差异说明 |
|-------------|-------------|-------------------|----------|
| `avoid-ai-writing` | 含中文路由表、子技能引用，结构不同 | conorbrondon v3.10.0 英文原版，含 Voice Profiles | 本地版是修改/精简版，去掉了 Voice Profiles |
| `cnki` | Python Playwright 自动化（`cnki_auto.py`） | jirboy 的 MCP Chrome DevTools 版本 | 架构完全不同（Playwright vs MCP） |
| `deep-research` | 实事求是/科学客观原则，Phases 阶段 | user_8e810118 的问题优先/深度优先，Steps 步骤 | 核心原则和工作流不同 |

本地版本的版权归属于各自的修改者。使用时请注意区分，不要混淆为 SkillHub 原版。

---

## Hermes 平台内置工具

| 工具 | 提供方 | 说明 |
|------|--------|------|
| MCP `mcp_sciverse`（含5个子工具） | OpenDataLab | 学术论文语义搜索引擎 | https://sciverse.opendatalab.com/ |
| `send_message`, `terminal`, `write_file`, `web_search` 等 | Nous Research / Hermes 平台 | Hermes Agent 基础工具集 |

---

## 外部 API 与平台服务

| 服务 | 提供方 | 用途 | 相关链接 |
|------|--------|------|----------|
| MinerU API | OpenDataLab | PDF/Word → Markdown 解析 | https://mineru.net/ / https://github.com/opendatalab/MinerU (AGPL-3.0) |
| CNKI 知网 | 中国知网 (清华同方) | 中文论文搜索与下载 | https://cnki.net/ |
| arXiv | Cornell University | 预印本论文搜索 | https://arxiv.org/ |
| CrossRef | Crossref | DOI元数据查询 | https://www.crossref.org/ |
| Sciverse | OpenDataLab | 学术论文语义搜索 | https://sciverse.opendatalab.com/ |

使用上述服务时，请遵守各平台的服务条款和 API 使用规范。

---

## 报告版权问题

如果你认为本仓库的某个技能或资源侵犯了你的版权，请通过 GitHub Issues 联系，我们会及时处理。
