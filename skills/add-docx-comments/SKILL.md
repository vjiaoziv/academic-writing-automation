---
name: add-docx-comments
version: 1.0.0
description: "在 Word (.docx) 文档中插入真实批注（Comments）。使用 lxml 直接操作 OOXML，支持按段落索引插入批注，生成带 commentRangeStart/commentReference/commentRangeEnd 标记的标准 Word 批注。触发词：插入批注、Word批注、docx批注、批注论文、add comments。"
tags: [word, docx, comment, annotation, review, academic]
author: "Hermes Agent"
---

# Add DOCX Comments — Word 文档批注工具

## 功能

在 `.docx` 文件中插入**真实的 Word 批注**（不是 HTML 报告，是 Word 里右键能看到的 Comments）。

## 依赖

- Python 3.8+
- `lxml`（`pip install lxml`）

## 用法

### 命令行

```bash
python scripts/add_docx_comments.py <输入.docx> <输出.docx> <批注清单.json>
```

### 批注清单 JSON 格式

```json
[
    {
        "para_idx": 3,
        "comment": "这段AI味过重，建议改写",
        "author": "Reviewer"
    },
    {
        "para_idx": 7,
        "comment": "数据来源未标注，请补充参考文献",
        "author": "Editor"
    }
]
```

字段说明：
- `para_idx`（int，必需）：段落索引，从 0 开始
- `comment`（str，必需）：批注内容
- `author`（str，可选）：批注作者，默认 "Hermes Agent"

### Python 调用

```python
from add_docx_comments import add_comments_to_docx

annotations = [
    {"para_idx": 0, "comment": "建议补充研究背景"},
    {"para_idx": 2, "comment": "此处逻辑跳跃，需要过渡"},
]
add_comments_to_docx("input.docx", "output.docx", annotations)
```

## 实现原理

直接操作 `.docx` 的 OOXML（ZIP 内的 XML 文件）：

1. 修改 `word/comments.xml` — 添加 `<w:comment>` 元素
2. 修改 `word/document.xml` — 在目标段落插入：
   - `<w:commentRangeStart w:id="N"/>`（段落开头）
   - `<w:commentRangeEnd w:id="N"/>`（段落末尾）
   - `<w:r><w:commentReference w:id="N"/></w:r>`（段落末尾，可见标记）
3. 修改 `[Content_Types].xml` — 确保 comments.xml 的 content type 已声明

## 注意事项

- 段落索引从 0 开始，按 `document.xml` 中 `<w:p>` 元素的顺序
- 如果段落没有 `<w:r>`（空段落），会跳过
- 如果文档已有批注，自动递增 ID，不会覆盖
- 输出文件是新文件，不修改原文件

## 与其他技能的配合

本工具通常被 `paper-revision-sop` 调用，用于在论文修改阶段生成带批注的 Word 文档。也可以独立使用。
