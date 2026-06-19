# Citation-Grounded Writing — 操作笔记与实测记录

## 2026-06-19 全流程验证测试

### 测试结果

| 阶段 | 工具 | 结果 | 备注 |
|------|------|------|------|
| 英文文献搜索 | `mcp_sciverse_search_papers` | ✅ | 10,000+结果，413ms，DOI/年份/学科过滤 |
| 中文文献搜索 | `search_papers` + language=zh | ✅ | 返回10,000条中文论文，含中文标题/摘要 |
| 类型过滤 | `search_papers` + type=Review/Article/Conference | ✅ | 20种类型枚举可用 |
| OA过滤 | `search_papers` + access_oa_status | ✅ | gold/green/bronze/hybrid/diamond/closed 过滤正确 |
| 期刊/会场过滤 | `search_papers` + publication_venue_type=conference | ✅ | 正确返回会议论文 |
| FWCI高影响力过滤 | `search_papers` + fwci>=5.0 | ✅ | 返回FWCI 9-1876的高被引论文 |
| 语义搜索 | `mcp_sciverse_semantic_search` | ✅ | quality模式，返回精准段落+score |
| 语义搜索 + source_types=["pdf"] | `semantic_search` + source_types | ✅ | 仅返回PDF全文来源论文 |
| 语义搜索 + source_types=["web"] | `semantic_search` + source_types | ✅ | 仅返回网页来源论文 |
| 全文读取 | `mcp_sciverse_read_content` | ⚠️ | Open Access ✅ / Closed Access ❌ (404) |
| 全文分页读取 | read_content offset=0→500→1000 | ✅ | offset+limit分段，more=true指示后续 |
| 高级搜索 | `search_papers` + `freshness_boost` | ✅ | `freshness_boost=STRONG` 返回近3年论文；注意与 `sort_by_year` 互斥 |
| 高被引过滤 | `filters_advanced` + `is_in_top_10_percent` | ✅ | Boolean 过滤正确 |
| topic域过滤 | `search_papers` + primary_topic.domain | ❌ | 返回空，nested字段需特殊格式 |
| PDF解析 | `mineru` API v4 | ✅ 备用 | sciverse read_content 首选，mineru PDF解析备用 |
| 中文文献搜索 | `cnki` Playwright | ✅ 备用 | sciverse 首选（4.65亿中英双语），cnki 知网深度补充 |
| 关键句提取 | 直接处理 | ✅ | 6维度分类标注，已验证5条真实句子 |
| 写作嵌入引用 | 直接处理 | ✅ | 5条引用均有原文佐证 |
| 合规检查 | 直接处理 | ✅ | 四道门禁逻辑完整 |
| 去AI味 | `avoid-ai-writing` | ✅ | rewrite模式，academic配置 |

### 关键发现
6. **Sciverse `freshness_boost` 与 `sort_by_year` 互斥**：同时传返回400错误，模糊搜索只能按相关性排序。
7. **`filters_advanced` operator 格式**：必须用 `FILTER_OP_IN`/`FILTER_OP_EQ`/`FILTER_OP_GT` 等大写格式，小写 `IN`/`EQ` 会400错误。
8. **专利搜索不可用**：Sciverse `type` 字段枚举值中无 `patent`，主要覆盖学术文献。
9. **15个官方场景案例已验证**：包括文献综述Agent、Citation Grounding、PRISMA初筛、趋势扫描等，详见 https://sciverse.opendatalab.com/

1. **sciverse read_content 对 Closed Access 返回 404**：即使 search_papers 返回了结果，read_content 对非 OA 论文返回 `CONTENT_NOT_FOUND`。应对：优先选 OA 论文；fallback：cnki 下载 PDF → mineru 解析。

2. **MINERU_TOKEN 已配置**：417字符 JWT，写入 `~/.hermes/.env`，API 验证通过。获取方式：用户提供。写入方式：Python（heredoc/echo 会因特殊字符出错）。

3. `academic-citation-manager` 在 `~/.hermes/skills/academic-citation-manager/`（独立目录，完整技能，是唯一实际使用的引用管理工具）

4. **multi-academic-search 实际路径**：`~/.hermes/skills/文献检索skill/multi-academic-search/`（中文目录名）

5. **execute_code 被安全策略限制**：cron 模式下 `execute_code` 返回 BLOCKED。主会话不受影响。

### 环境依赖

| 依赖 | 状态 | 获取方式 |
|------|------|----------|
| `MINERU_TOKEN` | ✅ 已配置 | 用户提供 → Python 写入 .env |
| `BAIDU_API_KEY` | ❌ 未配置 | 百度智能云千帆平台 |
| cnki 机构IP授权 | ⚠️ 需校园网 | 华南农业大学网内自动授权 |
| sciverse MCP | ✅ 可用 | 内置 MCP 工具 |
| mineru API | ✅ 可用 | OpenDataLab |

---

## 2026-06-19 Sciverse 全功能验证

### 验证方法
- 并行 5 组 `search_papers` 测试不同过滤器组合
- 3 组 `semantic_search` 测试 source_types + 模式
- 2 组 `read_content` 测试分页连续读取
- 1 组 `list_catalog` 拉取完整 schema + enum 取值

### 全功能验证结果

| 功能 | 状态 | 备注 |
|------|------|------|
| `search_papers` 基础搜索 | ✅ | 中英文均可，total_count=10,000+ |
| `search_papers` + `type` 过滤 | ✅ | Review/article/conference 等 20 种 |
| `search_papers` + `language` 过滤 | ✅ | zh/en/de/fr 等 20+ 语言 |
| `search_papers` + `access_oa_status` 过滤 | ✅ | gold/green/bronze/hybrid/diamond/closed |
| `search_papers` + `publication_venue_type` 过滤 | ✅ | journal/conference/repository 等 |
| `search_papers` + `fwci` 范围过滤 | ✅ | >=5.0 高影响力论文可筛 |
| `search_papers` + `primary_topic.domain` 过滤 | ❌ | 返回空，nested 字段需特定格式 |
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

### Sciverse 功能 → 写论文阶段映射

- **Phase 1 搜索**：search_papers(基础/freshness/type/language/fwci/citation_count/venue_type) + semantic_search(fast)
- **Phase 1.5 PRISMA**：search_papers(title_contains/OA过滤/page_size=50/ebook) + semantic_search(balanced/quality)
- **Phase 2 阅读**：read_content(分页) + read_content(提取句子) + get_resource(图表)
- **Phase 3 大纲**：search_papers(related_works/references) + semantic_search(quality)
- **Phase 4 写作**：read_content(精确offset) + search_papers(MATCH_PHRASE/doi)
- **Phase 5 合规**：search_papers(is_in_top_1%/fwci) + semantic_search(source_types=["pdf"])
- **Phase 6 验证**：semantic_search(quality) + read_content(全文) + get_resource(图表)
- **Phase 7 终审**：不依赖 Sciverse
