# Citation-Grounded Writing — 操作笔记与实测记录

## 2026-06-19 全流程验证测试

### 测试结果

| 阶段 | 工具 | 结果 | 备注 |
|------|------|------|------|
| 英文文献搜索 | `mcp_sciverse_search_papers` | ✅ | 10,000+结果，413ms，DOI/年份/学科过滤 |
| 语义搜索 | `mcp_sciverse_semantic_search` | ✅ | quality模式，返回精准段落+score |
| 全文读取 | `mcp_sciverse_read_content` | ⚠️ | Open Access ✅ / Closed Access ❌ (404) |
| 高级搜索 | `search_papers` + `freshness_boost` | ✅ | `freshness_boost=STRONG` 返回近3年论文；注意与 `sort_by_year` 互斥 |
| OA过滤 | `filters_advanced` | ✅ | `access_oa_status IN [gold,green,hybrid,diamond]` 精确过滤OA论文避免404 |
| 高被引过滤 | `filters_advanced` | ✅ | `citation_normalized_percentile.is_in_top_10_percent=true` |
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
