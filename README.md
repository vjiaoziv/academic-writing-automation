# 📚 学术论文写作自动化工具包

> **从文献搜索 → 全文阅读 → 句子提取 → 自动写作 → 引用检查 → 去AI味润色 → Word批注审稿的完整管线**

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

| 我想要... | 用这个 |
|-----------|--------|
| 写一篇论文（全自动） | `citation-grounded-writing` |
| 去AI味/润色 | `avoid-ai-writing` (rewrite模式) |
| 检查AI痕迹 | `avoid-ai-writing` (detect模式) |
| 搜英文论文 | MCP `mcp_sciverse` |
| 搜中文论文 | `cnki` |
| 读PDF全文 | `mineru` |
| 插入参考文献 | `academic-citation-manager` |
| 论文配图 | `academic-figures` |
| 批注Word文档 | `add-docx-comments` |
| 审稿意见修改 | `paper-revision-sop` |
| 模拟同行评审 | `ars-academic-paper-reviewer` |
| 深度研究一个主题 | `ars-deep-research` |

---

## 🛠️ 外部工具依赖（需单独安装）

| 工具 | 安装方式 | 用途 |
|------|---------|------|
| `cnki` | `~/.hermes/skills/cnki/` | 知网论文搜索下载（需校园网） |
| `mineru` | 配置 `MINERU_TOKEN` 到 `.env` | PDF/Word → Markdown 解析 |
| `avoid-ai-writing` | SkillHub `skillhub install avoid-ai-writing` | 去AI味检测与改写 |
| `paper-revision-sop` | SkillHub `skillhub install paper-revision-sop` | 论文润色5阶段SOP |
| `academic-figures` | SkillHub `skillhub install academic-figures` | 14种学术图表 |
| `academic-citation-manager` | SkillHub `skillhub install academic-citation-manager` | 6种引用格式 |
| `ars-academic-paper` | SkillHub `skillhub install ars-academic-paper` | 12-agent论文写作 |
| `ars-academic-paper-reviewer` | SkillHub | 7-agent同行评审 |
| `ars-deep-research` | SkillHub | 13-agent深度研究 |
| `ars-academic-pipeline` | SkillHub | 研究到发表全流程 |

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
    └── (扩展中)
```

---

## 🤝 配合使用的技能包

| 类别 | 技能 | 来源 |
|------|------|------|
| 文献检索 | `cnki`, `arxiv`, MCP `mcp_sciverse` | Hermes内置/SkillHub |
| PDF解析 | `mineru` | SkillHub |
| 去AI味 | `avoid-ai-writing` | SkillHub |
| 论文润色 | `paper-revision-sop` | SkillHub |
| 图表生成 | `academic-figures` | SkillHub |
| 引用管理 | `academic-citation-manager`, `reference-management` | SkillHub |
| 模拟评审 | `ars-academic-paper-reviewer` | SkillHub |
| 深度研究 | `ars-deep-research`, `deep-research` | SkillHub |

---

## 📜 许可证

MIT License — 自由使用、修改和分发。

---

## 🔗 相关链接

- **SkillHub 发布包：** `citation-grounded-writing.zip` + `add-docx-comments.zip`（需实名认证后发布）
- **SkillHub 安装：** `skillhub install <skill-name>`
- **本地安装：** 复制 `skills/` 目录到 `~/.hermes/skills/`
