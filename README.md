# 📚 学术论文写作自动化工具包

> **从文献搜索 → 全文阅读 → 句子提取 → 自动写作 → 引用检查 → 去AI味润色 → Word批注审稿的完整管线**

> ⚠️ **许可证注意：** 本仓库集成了 ARS (Academic Research Skills) 套件，其许可证为 **CC-BY-NC-4.0（非商业使用）**。如果您的使用场景涉及商业活动（如付费服务、企业内部使用），请在路由决策表中优先选择标注「📦 自创 MIT」的技能，或获取 ARS 原作者的商业授权后再使用 ARS 套件。

---

## 🏗️ 系统架构

```
用户需求
    │
    ▼
┌─────────────────────────────────────────────────────┐
│            🗺️ 路由决策表 (ROUTING-TABLE.md)          │
│   根据场景自动选择最佳技能组合                          │
└──────┬──────────┬──────────┬──────────┬────────────┘
       │          │          │          │
       ▼          ▼          ▼          ▼
 ┌──────────┐ ┌────────┐ ┌────────┐ ┌──────────┐
 │ 📖写作    │ │🔍检索  │ │✏️修改  │ │📊配图    │
 │          │ │        │ │        │ │          │
 │citation- │ │sciverse│ │paper-  │ │academic- │
 │grounded- │ │  (MCP) │ │revision│ │figures   │
 │writing   │ │        │ │-sop    │ │          │
 │          │ │cnki    │ │        │ │minimax-  │
 │ars-      │ │        │ │avoid-  │ │docx      │
 │academic  │ │arxiv   │ │ai-     │ │          │
 │-paper    │ │        │ │writing │ │docx-     │
 └──────────┘ └────────┘ └────────┘ └──────────┘
       │          │          │          │
       └──────────┴──────────┴──────────┘
                     │
                     ▼
          ┌─────────────────────┐
          │  🔧 基础工具层       │
          │  • mineru (PDF解析)  │
          │  • academic-citation │
          │    manager (引用管理) │
          │  • reference-        │
          │    management (GB/T) │
          │  • add-docx-comments │
          │    (Word批注)        │
          └─────────────────────┘
```

---

## 🎯 核心技能（本仓库包含）

### 1. `citation-grounded-writing` — 全自动论文写作（v1.1.0）

**6阶段全自动化工作流，每条引用必须有原文佐证：**

| 阶段 | 描述 | 工具 |
|------|------|------|
| Phase 0 配置 | 自动确定中英文范围、引用数量、写作风格 | - |
| Phase 1 三路并发搜索 | 中文cnki + 英文sciverse + arxiv | cnki + sciverse + arxiv |
| Phase 2 下载解析 | PDF/全文下载 → Markdown解析 | mineru + sciverse |
| Phase 3 全文精读 | 逐篇完整阅读，按主题分类 | read_content |
| Phase 4 自动大纲 | 生成论文结构，预分配引用位置 | AI生成 |
| Phase 5 逐节写作 | 嵌入原文句子 + 四道合规门禁 | avoid-ai-writing |
| Phase 6 润色交付 | 去AI味 + 格式化引用列表 | avoid-ai-writing |

**安装：** 将 `skills/citation-grounded-writing/` 复制到 `~/.hermes/skills/`

---

### 2. `add-docx-comments` — Word文档批注工具（v1.0.0）

**在 `.docx` 文件中插入真实的 Word 批注**（不是 HTML 报告）

**在论文写作全流程中的位置：**

```
paper-revision-sop 5阶段流程：
Phase 0 审稿意见解析  →  提取可执行修改项
Phase 1 论文全息诊断  →  AI味/结构/可读性问题定位
Phase 2 可视化批注 ⭐  ←  add-docx-comments 在这里
Phase 3 分级改写      →  按批注逐条修改论文
Phase 4 终审自检      →  二次验证
```

Phase 2 的作用是**把诊断结果转化为 Word 文档里的真实批注**，让作者在 Word 中打开就能直接看到"第3段AI味过重"、"第7段缺引用来源"等问题标注，然后按批注逐条修改。这比生成独立的 HTML 报告更直观——修改时对照批注即可，不用在两个文档间来回切换。

**典型使用场景：**
- **论文润色**：诊断完成后，将 AI味、结构、可读性等问题以 Word 批注插入，作者逐条对照修改
- **审稿回复**：把审稿意见映射到论文对应段落，形成"审稿意见 → Word批注"的一一对应
- **自查标注**：检测完 AI 痕迹后，直接在原文档中用批注标出需要改写的段落

```bash
# 命令行用法
python scripts/add_docx_comments.py 输入.docx 输出.docx 批注清单.json

# 批注清单格式
[{"para_idx": 3, "comment": "这段AI味过重，建议改写"}, ...]
```

**安装：** 将 `skills/add-docx-comments/` 复制到 `~/.hermes/skills/`

---

## 📋 完整工具一览（路由表）

详见 **[ROUTING-TABLE.md](ROUTING-TABLE.md)** — 包含全部 20+ 工具的详细说明、路由决策表和使用场景。

**快速路由速查：**

- 写一篇论文（全自动） → `citation-grounded-writing` 📦
- 去AI味/润色 → `avoid-ai-writing` (rewrite模式) 🔶
- 检查AI痕迹 → `avoid-ai-writing` (detect模式) 🔶
- 搜英文论文 → MCP `mcp_sciverse` 🔵
- 搜中文论文 → `cnki` 🔶
- 读PDF全文 → `mineru` 🌐
- 插入参考文献 → `academic-citation-manager` 🔸
- 论文配图 → `academic-figures` 🔶
- 批注Word文档 → `add-docx-comments` 📦
- 审稿意见修改 → `paper-revision-sop` 📦
- 模拟同行评审 → `ars-academic-paper-reviewer` 🔸
- 深度研究一个主题 → `ars-deep-research` 🔸
- 从研究到发表全流程 → `ars-academic-pipeline` 🔸
- 格式转换（LaTeX/DOCX/PDF） → `/ars-format-convert` 🔸
- 审计回复草稿 → `/ars-rebuttal-audit` 🔸
- 生成AI使用声明 → `/ars-disclosure` 🔸
- 文献综述 → `/ars-lit-review` 🔸
- 论文大纲 → `/ars-outline` 🔸
- 论文摘要 → `/ars-abstract` 🔸
- 引用检查 → `/ars-citation-check` 🔸
- 三路扫描（比较论文） → `/ars-3w` 🔸

> 📦 = 本仓库自创（MIT）| 🔸 = ARS 套件（CC-BY-NC-4.0，非商业）| 🔵 = Hermes 内置 MCP | 🔶 = SkillHub 社区 | 🌐 = 外部 API

---

## 🛠️ 外部工具依赖（需单独安装）

| 工具 | 安装方式 | 用途 | 来源 | 许可证 |
|------|---------|------|------|--------|
| `cnki` | `~/.hermes/skills/cnki/` | 知网论文搜索下载（需校园网） | 本地 Playwright 独立实现（与 jirboy MCP 版不同） | 见说明 |
| `mineru` | 配置 `MINERU_TOKEN` 到 `.env` | PDF/Word → Markdown 解析 | [OpenDataLab](https://github.com/opendatalab/MinerU) | AGPL-3.0 |
| `avoid-ai-writing` | SkillHub | 去AI味检测与改写 | 本地修改版（原版：conorbrondon v3.10.0） | 见原作者 |
| `paper-revision-sop` | ClawHub | 论文润色5阶段SOP | [liuwenqi123123](https://clawhub.ai/liuwenqi123123/paper-revision-sop) | 见原作者 |
| `academic-figures` | SkillHub | 14种学术图表 | [docsor1212](https://clawhub.com/skills/academic-figures) via SkillHub | 见原作者 |
| `academic-citation-manager` | SkillHub | 6种引用格式 | [YouStudyeveryday](https://github.com/YouStudyeveryday/academic-citation-manager) | MIT |
| `ars-hub` | SkillHub / 本地仓库 | ARS路由入口 | [ARS](https://github.com/Imbad0202/academic-research-skills) (Cheng-I Wu) | CC-BY-NC-4.0 |
| `ars-commands` | SkillHub / 本地仓库 | 16个`/ars-*`快捷命令 | [ARS](https://github.com/Imbad0202/academic-research-skills) (Cheng-I Wu) | CC-BY-NC-4.0 |
| `ars-academic-paper` | SkillHub / 本地仓库 | 12-agent论文写作 | [ARS](https://github.com/Imbad0202/academic-research-skills) (Cheng-I Wu) | CC-BY-NC-4.0 |
| `ars-academic-paper-reviewer` | SkillHub / 本地仓库 | 7-agent同行评审 | [ARS](https://github.com/Imbad0202/academic-research-skills) (Cheng-I Wu) | CC-BY-NC-4.0 |
| `ars-deep-research` | SkillHub / 本地仓库 | 13-agent深度研究 | [ARS](https://github.com/Imbad0202/academic-research-skills) (Cheng-I Wu) | CC-BY-NC-4.0 |
| `ars-academic-pipeline` | SkillHub / 本地仓库 | 研究到发表全流程 | [ARS](https://github.com/Imbad0202/academic-research-skills) (Cheng-I Wu) | CC-BY-NC-4.0 |

---

## 🚀 快速开始

### 场景1：写一篇论文（全流程）

```
用户：帮我写一篇关于"AI在高等教育质量保障中的应用"的论文
→ 系统自动调用 citation-grounded-writing
→ 搜索 → 下载 → 阅读全文 → 提取句子 → 自动写作 → 合规检查 → 去AI味
→ 交付：完整论文.md + 引用列表.md + 合规报告
```

### 场景2：润色已有论文

```
用户：帮我润色这篇论文，去AI味
→ 系统调用 avoid-ai-writing (rewrite, academic)
→ 输出：改写后文本 + 修改说明
```

### 场景3：审稿意见回复

```
用户：根据这些审稿意见修改论文
→ 系统调用 paper-revision-sop
→ Phase 0：解析审稿意见 → Phase 2：Word批注 → Phase 3：分级改写
→ 输出：修改稿.docx + 批注版.docx + 终审报告
```

---

## 📂 仓库结构

```
academic-writing-automation/
├── README.md                           # 本文档
├── ROUTING-TABLE.md                    # 完整路由表（20+工具决策指南）
├── LICENSE                             # MIT License
├── skills/
│   ├── citation-grounded-writing/      # 核心：全自动论文写作技能
│   │   ├── SKILL.md                    # 技能定义（6阶段工作流）
│   │   └── references/
│   │       └── operational-notes.md    # 运行操作指南
│   └── add-docx-comments/             # Word文档批注工具
│       ├── SKILL.md                    # 技能定义
│       └── scripts/
│           └── add_docx_comments.py    # 批注插入脚本（lxml + OOXML）
└── references/                         # 补充文档
    └── ACKNOWLEDGMENTS.md              # 致谢与来源说明
```

---

## 🤝 配合使用的技能包

| 类别 | 技能 | 来源 | 许可证 |
|------|------|------|--------|
| ARS路由入口 | `ars-hub` | [ARS](https://github.com/Imbad0202/academic-research-skills) (Cheng-I Wu) | CC-BY-NC-4.0 |
| ARS快捷命令 | `ars-commands` | [ARS](https://github.com/Imbad0202/academic-research-skills) (Cheng-I Wu) | CC-BY-NC-4.0 |
| 文献检索 | `cnki`（本地独立实现）, `arxiv`（本地独立实现）, MCP `mcp_sciverse` | 本地/Hermes内置 | 见各来源 |
| PDF解析 | `mineru` | [OpenDataLab](https://github.com/opendatalab/MinerU) | AGPL-3.0 |
| 去AI味 | `avoid-ai-writing` | 本地修改版（原版：conorbrondon） | 见原作者 |
| 论文润色 | `paper-revision-sop` | [liuwenqi123123](https://clawhub.ai/liuwenqi123123/paper-revision-sop) (ClawHub) | 见原作者 |
| 图表生成 | `academic-figures` | [docsor1212](https://clawhub.com/skills/academic-figures) via SkillHub | 见原作者 |
| 引用管理 | `academic-citation-manager` | [YouStudyeveryday](https://github.com/YouStudyeveryday/academic-citation-manager) | MIT |
| 模拟评审 | `ars-academic-paper-reviewer` | [ARS](https://github.com/Imbad0202/academic-research-skills) (Cheng-I Wu) | CC-BY-NC-4.0 |
| 深度研究 | `ars-deep-research`, `deep-research` | [ARS](https://github.com/Imbad0202/academic-research-skills) / SkillHub | CC-BY-NC-4.0 / 见原作者 |

---

## 📜 许可证与版权声明

**本仓库自创技能**（`citation-grounded-writing`、`add-docx-comments`、`arxiv`、`marxist-report-word`、`docx-punctuation-normalizer`）采用 **MIT License** — 自由使用、修改和分发。

> ⚠️ **关于 `arxiv`**：本仓库的 `arxiv` 技能是基于 curl REST API 的独立实现，与 SkillHub 上 ractorrr 的 arXiv Research Assistant（含 MongoDB 功能）不是同一个代码，不归属于 ractorrr。

**第三方技能和工具**的版权归属于各自的作者和组织：
- **ARS 套件**（ars-hub, ars-commands, ars-academic-paper 等）— Cheng-I Wu / Imbad0202，**CC-BY-NC-4.0（非商业使用）**
- **paper-revision-sop** — liuwenqi123123 via ClawHub（⚠️ 之前误标为自创，已更正）
- **academic-citation-manager** — YouStudyeveryday，MIT License
- **academic-figures** — docsor1212 via SkillHub
- **avoid-ai-writing** — 本地修改版，原版作者 conorbrondon via ClawHub
- **MinerU** — OpenDataLab，AGPL-3.0
- **MCP sciverse** — Nous Research / Hermes 平台内置
- **其他 SkillHub 社区技能** — 各自原作者

> ⚠️ **关于同名不同实现的技能**：`cnki`、`avoid-ai-writing`、`deep-research` 的本地安装版本与 SkillHub 上同名技能的代码不同（架构、功能、工作流均有差异）。这些本地版本的版权不属于 SkillHub 原作者，但也不属于本仓库自创——它们是独立的修改/重实现版本。使用前请注意区分。

使用前请遵守各自的许可证条款。本仓库不拥有第三方技能的版权。商业使用 ARS 套件或 SkillHub 社区技能前需获取相应授权。

详细的来源说明和致谢 → 见 [references/ACKNOWLEDGMENTS.md](references/ACKNOWLEDGMENTS.md)

---

## 🔗 相关链接

- **SkillHub 发布包：** `citation-grounded-writing.zip` + `add-docx-comments.zip`（需实名认证后发布）
- **SkillHub 安装：** `skillhub install <skill-name>`
- **本地安装：** 复制 `skills/` 目录到 `~/.hermes/skills/`
- **完整来源说明：** [references/ACKNOWLEDGMENTS.md](references/ACKNOWLEDGMENTS.md)
