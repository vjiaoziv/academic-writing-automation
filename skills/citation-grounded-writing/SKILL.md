---
name: citation-grounded-writing
version: 1.1.3
description: "全自动化论文写作——自动搜索、下载、解析、阅读参考文献全文，提取真实句子嵌入正文写作。集成：MCP sciverse（首选，中英文4.65亿记录+原文段落）/ cnki（备用，知网下载PDF）/ mineru（备用，PDF解析）/ academic-citation-manager / avoid-ai-writing。强制规则：每条引用必须有原文佐证，禁止虚构引用。"
tags: [academic, writing, citation, grounded, evidence-based, full-automation]
author: "Hermes Agent"
---

# Citation-Grounded Writing — 全自动基于真实引用的论文写作

## 核心原则

**写论文时，从参考文献搜索到最终引用，全流程自动化，且每条引用必须能在原文中找到对应的真实句子。**

```
用户提供论文主题
    ↓
自动搜索 → 自动下载PDF → 解析全文 → 提取关键句
    ↓                       ↑
按大纲逐节写作 ──────────────┘（匹配同主题句子嵌入正文）
    ↓
引用合规检查（验证每条引用真实存在）
    ↓
去AI味润色 → 输出完稿
```

---

## 完整工作流（6 阶段）

### Phase 0：配置阶段

**输入**：
- 论文题目 / 研究方向描述
- 设定引用数量（默认 8-15 篇，可根据论文字数调整）
- 引用格式偏好：GB/T 7714-2015（默认）| APA 7 | MLA 9 | IEEE | Chicago
- 学科领域（中英文、社会科学/理工/医学等）
- 论文大纲（可选，若无则自动生成）

**需确认项**：
1. 论文语言（中文/英文/中英混合）
2. 是否需要中文文献（默认需要，首选 sciverse 中英文搜索，cnki 备用）
3. 是否需要英文文献（默认需要，走 sciverse + arXiv + Semantic Scholar）

**输出**：Paper Configuration Record（配置记录）

---

### Phase 1：自动搜索并获取参考文献全文

#### 1.1 文献搜索策略（三路并发）

| 路径 | 目标 | 工具 | 搜索策略 |
|------|------|------|----------|
| **A. 中文学术** | CSSCI/北大核心/知网期刊 | `mcp_sciverse`（首选）+ `cnki`（备用） | sciverse 4.65亿中英双语检索，cnki 知网深度补充 |
| **B. 英文学术** | 国际期刊/顶会论文 | `mcp_sciverse_search_papers`（结构化过滤）<br>`arxiv`（预印本补充） | 搜索核心关键词，限定年份+学科，按引用数/相关性降序 |
| **C. 语义补充** | 找到高相关段落备用 | `mcp_sciverse_semantic_search` | 用自然语言描述研究问题，找到精准匹配的文献 |

**执行细则**：
- 每条路径搜索至少 2 轮（不同关键词组合）
- 搜索结果去重（按 DOI / title 去重）
- 优先选择：近3年（`freshness_boost=STRONG`）> 高被引（`citation_normalized_percentile.is_in_top_10_percent`）> 核心期刊 > 方法/综述类论文
- **重要**：`freshness_boost` 与 `sort_by_year` 互斥，不能同时使用
- 初选 15-20 篇候选文献，最终精选 8-15 篇

#### 1.2 下载并解析全文

确认文献列表后，逐篇获取全文：

| 来源 | 获取方式 | 解析方式 |
|------|----------|----------|
| 知网（cnki） | `cnki` Playwright → PDF下载（机构IP授权，**备用**） | `mineru` PDF→Markdown（**备用**） |
| arXiv | 直接获取 arXiv PDF URL | `mineru` PDF→Markdown |
| sciverse 已索引 | `mcp_sciverse_read_content`（字节级读取） | 直接返回文本 |
| 其他开放获取 | 搜索 free PDF + 下载 | `mineru` 或 `web_extract` |
| 付费/受限 | 获取DOI + 摘要（无法获取全文则标记为"仅摘要"） | 降级使用摘要 |

**所有解析结果统一保存为 Markdown**，便于后续句子提取。

**输出**：`refs/` 目录，每篇文献一个 .md 文件

---

### Phase 2：完整阅读全文 + 提取关键句子

#### 2.1 精读每篇文献的全文

对每个 .md 文件逐篇阅读，理解：
- 研究问题 / 目标
- 方法论 / 实验设计
- 核心发现 / 数据结果
- 局限性与未来工作

#### 2.2 提取关键句子

按以下维度提取句子，每个维度至少 2-5 句：

| 维度 | 提取标记 | 用途 |
|------|----------|------|
| **核心结论** | "结果表明""研究发现""therefore""We conclude" | 用于论文"结果与讨论"章节 |
| **方法论描述** | "We propose""Our method""采用"/算法描述 | 用于"方法/模型"章节 |
| **数据/证据** | 具体数字、统计结果、评估指标 | 支撑论点的硬证据 |
| **定义/概念** | "定义为""refers to""是一种" | 用于背景/理论章节 |
| **对比/争议** | "不同于""Unlike""然而" | 用于文献综述/讨论 |
| **理论/框架** | "基于""Building on" | 用于理论基础章节 |

#### 2.3 句子分类标注

每条提取的句子需要标注：
- `ref_id`（对应参考文献序号）
- `section_hint`（建议放在论文章章节：背景/方法/结果/讨论/结论）
- `topic`（主题标签，如"transformer architecture"、"policy analysis"）
- `page`（原文页码，尽量标注）
- `usage_type`（data_evidence / definition / methodology / conclusion / contrast）

**输出**：`extracted_sentences.json`（结构化关键句库）

---

### Phase 3：自动化大纲生成

基于阅读理解 + 提取的句子，生成论文大纲：

1. 总结所有文献的核心论点和关键发现
2. 确定论文的研究缺口/研究问题
3. 生成章节结构（IMRaD 或社科适用格式）
4. 为每个章节分配关键句子（作为写作的"证据素材包"）

**输出**：论文大纲 + 每章节的已分配句子列表（evidence map）

---

### Phase 4：逐节写作，嵌入真实原文句子

#### 4.1 写作规则

每写一个章节时：

```
1. 确定该章节的论点和结构
2. 从 extracted_sentences.json 中匹配同主题句子
3. 写正文时，每个引用点必须嵌入原文的具体内容（数字、定义、结论），不能只是「文献[1]指出……」
4. 引用嵌入方式：
   - ✅ 直接引用："……'LLMs achieve 45.2 ROUGE-L'（Wang, 2024, p.5）"
   - ✅ 转述引用：……研究证实，LLMs 在文本摘要任务上表现出色，
     平均 ROUGE-L 达到 45.2（Wang et al., 2024）
   - ✅ 数据引用：准确率提升至 92.3%（Zhang, 2024）
   - ❌ 空泛引用：Smith (2022) 研究了该问题
```

#### 4.2 写作质量控制

- 每段落至少嵌入 1 条真实原文句子
- 不允许出现引用标记后跟空泛描述
- 多条引用并列时必须指明各自支撑的具体观点
- 每个章节完成后，检查该章节引用的句子是否都来自 extracted_sentences.json

**输出**：Markdown 格式论文初稿（含全文引用标记）

---

### Phase 5：引用合规检查（四道门禁）

| # | 检查项 | 工具/方法 | 违规后果 |
|---|--------|-----------|---------|
| 1 | **正文引用 → 参考文献** | 提取全文引用标记，核对参考文献列表完整性 | 每缺失一条，自动补充；无法补充则删除该引用 |
| 2 | **引用句子 → 原文存在性** | 逐条对照 extracted_sentences.json + ref_*.md | 无法追溯到原文具体位置的引用，强制删除 |
| 3 | **孤立引用** | 引用标记后跟空泛描述的段落 | 补充原文句子或改写 |
| 4 | **引用格式一致性** | 检查格式化是否符合选定标准（GB/T 7714 / APA） | 批量修正 |

**输出**：Citation Compliance Report（通过 / 待修复问题列表）

---

### Phase 6：终审 & 输出

1. **去AI味**：使用 `avoid-ai-writing`（academic 配置）全文润色，保留学术语域
2. **最终人工确认**（可选）：输出 HTML/DOCX/PDF/LaTeX 格式
3. **参考文献列表**：按选定格式生成完整的 References 章节

---

## 调用示例

### 场景 1：给定主题，无任何参考文献

```
⟫ 用户：写一篇关于"人工智能对高等教育质量保障的影响"的论文
⟫ 我（citation-grounded-writing）：
   Phase 0: 论文主题确认、引用格式=GB/T 7714、语言=中文+英文
   Phase 1:
     ├─ 路径A（中文）：sciverse 搜"人工智能 高等教育 质量保障" → read_content 读原文（首选）
     │                fallback：cnki 搜 → 下载PDF → mineru 解析
     ├─ 路径B（英文）：mcp_sciverse_search_papers "AI higher education quality assurance"
     │                + arXiv 补充 → MCP read_content 读全文
     └─ 路径C（语义）：mcp_sciverse_semantic_search "how AI affects higher education quality"
   
   Phase 2: 读取8-15篇全文，提取关键句按主题分类
   
   Phase 3-4: 生成大纲 → 逐节写作，每段嵌入真实句子
   
   Phase 5: 引用合规检查（确认所有引用真实）
   
   Phase 6: avoid-ai-writing 润色 → 输出含完整引用的论文
```

### 场景 2：给定参考文献搜索关键词

```
⟫ 用户：写一篇论文，帮我搜索关于"联邦学习在医疗影像中的应用"的最新文献
⟫ 我：
   用 mcp_sciverse_search_papers + cnki + arXiv 多路搜索
   筛选近3年高被引论文 → 下载PDF/读全文 → 提取句子 → 写作
```

---

## 操作笔记与实测记录

> 完整流程验证测试结果、已知限制、Workarounds、最佳实践速查 → 见 `references/operational-notes.md`

## 依赖技能列表

| 技能 | 阶段 | 角色 |
|------|------|------|
| `cnki` | Phase 1 | 中国知网检索 + PDF/CAJ 下载（机构IP授权） |
| MCP `mcp_sciverse_search_papers` | Phase 1 | 结构化文献过滤搜索（50+字段） |
| MCP `mcp_sciverse_semantic_search` | Phase 1 | 语义搜索（补足概念性匹配） |
| MCP `mcp_sciverse_read_content` | Phase 1 | 字节级读取论文全文 |
| `mineru` | Phase 1 | PDF/Word/PPT → Markdown（公式+表格+OCR） |
| `academic-citation-manager` | Phase 4/5 | 引用格式验证 + 6格式生成 + DOCX插入 |
| `avoid-ai-writing` | Phase 6 | 去AI味润色 |

---

## 已验证的 Pitfalls（2026-06-19）

### Closed Access 论文无法读取全文
`mcp_sciverse_read_content` 对 Closed Access 论文返回 `CONTENT_NOT_FOUND`（即使 search_papers 返回了结果）。
**应对**：
1. 优先选 Open Access 论文（`access_oa_status` = `gold`/`green`/`hybrid` 且 `is_oa="true"`）
2. 通过 `cnki` Playwright 下载 PDF（校园网内机构IP自动授权）→ `mineru` 解析为 Markdown
3. 退而求其次：仅用摘要（摘要+参考文献列表足以提供引用佐证）

### MINERU_TOKEN 写入 .env 需用 Python
Token 含 JWT 特殊字符（`==`、`+`、`/`），heredoc 和 echo 均会导致重复行或写入失败。
正确方式：Python 读取 .env → 过滤已有 MINERU_TOKEN 行 → 追加新行 → 写回。详见 `mineru/references/env-setup.md`。

### execute_code 在 cron 模式下被安全策略限制
Agent 在 cron 模式运行时，`execute_code` 可能被阻断。主会话中正常使用不受影响。
**应对**：核心写作逻辑直接在主会话中调用工具完成，不依赖 execute_code。

### CNKI Playwright 已知 Bug
`cnki_auto.py` 的 `download_paper()` 有 `input()` 阻塞问题，`search` 命令可正常工作。
## IRON RULES（强制规则，不可违反）

1. ⚠️ **Phase 1 不可跳过** — 必须先搜索获取并阅读全文，才能进入写作阶段
2. ⚠️ **每条引用必须有原文句子佐证** — 无法在 extracted_sentences.json 中找到对应句子的引用标记，必须在终稿中删除
3. ⚠️ **不得虚构** — 严禁编造任何作者、标题、年份、DOI、页码、原文语句
4. ⚠️ **Phase 5 不可跳过** — 引用合规检查未通过，禁止输出终稿
5. ⚠️ **引用内容必须来自实际读取的原文** — 不得用摘要信息冒充全文内容
6. **双路搜索** — 中文文献走 cnki，英文文献走 sciverse + arxiv，确保覆盖面
7. **引用格式** — 默认 GB/T 7714-2015，用户指定其他格式则依标准转换
8. **去AI味** — 所有润色/去AI味步骤统一使用 `avoid-ai-writing`（rewrite模式，academic配置），不使用 `humanizer`

## 搜索策略（双路并发）

| 路径 | 目标 | 工具 |
|------|------|------|
| 中文学术 | CSSCI/北大核心/知网期刊 | `cnki`（Playwright 脚本，机构IP授权） |
| 英文学术 | 国际期刊/顶会论文 | `mcp_sciverse_search_papers` + `arxiv` |
| 语义补充 | 精准段落匹配 | `mcp_sciverse_semantic_search` |

---