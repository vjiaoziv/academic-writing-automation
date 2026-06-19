# Academic Writing Automation

> **全自动化学术论文写作工具套件** — 从文献搜索、下载、阅读、提取句子到写作、引用合规检查、去AI味润色的完整管线。

## 项目结构

```
academic-writing-automation/
├── skills/
│   ├── citation-grounded-writing/   # 📖 基于真实引用的论文写作（核心技能）
│   │   ├── SKILL.md
│   │   └── references/
│   └── add-docx-comments/           # 📝 Word 文档批注工具
│       ├── SKILL.md
│       ├── scripts/
│       │   └── add_docx_comments.py
│       └── references/
└── README.md
```

## 技能介绍

### 1. `citation-grounded-writing` — 基于真实引用的全自动论文写作

6 阶段全自动化工作流，**每条引用必须有原文佐证**：

| 阶段 | 描述 | 使用的工具 |
|------|------|-----------|
| **Phase 0** 配置 | 确定主题、语言、风格、引用格式 | — |
| **Phase 1** 搜索与获取全文 | 三路并发搜索，下载PDF并解析 | cnki / sciverse / arxiv / mineru |
| **Phase 2** 精读与提取句子 | 读完每篇全文，提取关键句分类 | — |
| **Phase 3** 自动大纲 | 基于阅读生成论文大纲 + 证据图 | — |
| **Phase 4** 逐节写作 | 嵌入真实原文句子，禁止空泛引用 | — |
| **Phase 5** 引用合规检查 | 四道门禁验证每条引用真实存在 | reference-management |
| **Phase 6** 润色输出 | 去AI味 + 格式输出 | avoid-ai-writing |

**适用场景**：
- 给定论文题目，从零开始写出含完整引用的论文
- 已有文献关键词，需要自动搜索整理并写作
- 学术课程论文、期刊稿件、毕业论文初稿

**依赖的外部技能 / 工具**：
- [cnki](https://skillhub.cn/skills/cnki) — 中国知网检索 + PDF下载
- [mineru](https://skillhub.cn/skills/mineru) — PDF/Word/PPT → Markdown 解析
- MCP sciverse — 英文学术文献搜索 + 全文读取
- [reference-management](https://skillhub.cn/skills/reference-management) — 引用格式验证
- [avoid-ai-writing](https://skillhub.cn/skills/avoid-ai-writing) — 去AI味润色

### 2. `add-docx-comments` — Word 文档批注工具

在 `.docx` 文件中插入**真实的 Word 批注**（Comments），使用 lxml 直接操作 OOXML。

```bash
python add_docx_comments.py 输入.docx 输出.docx 批注清单.json
```

**典型用途**：
- 论文审稿时在 Word 中标注问题段落
- AI 润色后标注修改过的区域
- 批量插入审稿意见

## 安装

### 作为 Hermes Skills 安装

每个 skill 是一个标准 SKILL.md 包，放入 `~/.hermes/skills/` 即可：

```bash
# 方法 1：从 SkillHub 安装
skillhub install citation-grounded-writing
skillhub install add-docx-comments

# 方法 2：手动安装（克隆此仓库后）
cp -r skills/* ~/.hermes/skills/
```

### 独立使用

`add-docx-comments` 的 Python 脚本可独立运行，不依赖 Hermes：

```bash
pip install lxml
python skills/add-docx-comments/scripts/add_docx_comments.py input.docx output.docx annotations.json
```

## 核心原则

1. **每条引用必须有原文句子佐证** — 无法在 extracted_sentences.json 中找到的引用标记，不得留在终稿中
2. **禁止虚构引用** — 不得编造任何作者、标题、年份、DOI、页码、原文语句
3. **Phase 1 和 Phase 5 不可跳过** — 必须先阅读全文才能写作，写完必须验证引用真实性
4. **双路搜索** — 中文文献走 cnki，英文文献走 sciverse + arxiv
5. **去AI味** — 统一使用 avoid-ai-writing（rewrite 模式，academic 配置）

## 技术栈

- **运行环境**：Hermes Agent / OpenClaw / 任何兼容 SKILL.md 的 Agent 框架
- **关键依赖**：Python 3.8+, python-docx, lxml
- **MCP 工具**：sciverse（文献搜索/全文读取）
- **外部 API**：cnki（知网脚本）、mineru（PDF解析）

## License

MIT
