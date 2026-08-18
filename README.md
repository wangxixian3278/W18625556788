# 我的研究（My Research）

**我的研究（My Research）** (`my-research`) 是 我的研究 系列中的跨平台社交研究 Skill。

它面向**所有赛道**：不是 AI 专用，也不是固定行业模板。它通过动态发现社交数据工具，研究任意行业、品类、品牌、产品、创作者、人物或话题，并把公开数据转成可执行的趋势、竞品、用户需求和内容机会判断。

## 功能总览

### 1. 赛道发现
从宽关键词开始，根据真实平台结果扩展子赛道、相关概念、代表账号和内容形态。

### 2. 趋势扫描
识别近期高频、快速增长、突然出现或异常高表现的话题和内容。

### 3. 竞品 / 对标账号发现
寻找真正值得研究的账号，而不只按粉丝数排序。

### 4. 账号审计
分析账号的内容结构、发布节奏、常见主题、近期基线和异常高表现内容。

### 5. 爆款拆解
结合绝对表现、互动率、粉丝规模与账号自身基线识别“异常表现”，再分析标题、开头、主题、形式和用户反馈。

### 6. 评论需求挖掘
聚合高频问题、购买顾虑、反对点、教程需求、未回答问题和下一步内容需求。

### 7. 内容空白发现
综合需求、趋势、供给密度、相对表现、可复制性与目标匹配度寻找高价值机会。

### 8. 跨平台比较
比较同一主题在抖音、小红书、TikTok、Instagram、YouTube、B站、微博、Reddit 等平台上的不同表达与需求。

### 9. 品牌 / 产品研究
整理公开社媒中的产品表现、用户反馈、竞品对比和内容机会。

### 10. 数据驱动选题
生成选题时附带数据依据、用户需求、竞争判断和证据置信度，不把无证据创意包装成“趋势”。

## 数据连接方式

默认使用 TikHub 官方 MCP 服务作为公共社交数据基础设施。它通过平台级 MCP Server 暴露当前可用工具，因此 我的研究（My Research） 不需要把数百个 endpoint 固定写死。

### 准备 API Key

```bash
export TIKHUB_API_KEY="YOUR_API_KEY"
```

### 检查服务

```bash
python3 scripts/tikhub_mcp.py health
python3 scripts/tikhub_mcp.py platforms
```

### 发现当前工具

```bash
python3 scripts/tikhub_mcp.py discover \
  --platform douyin \
  --query "search video keyword"
```

```bash
python3 scripts/tikhub_mcp.py discover \
  --platform xiaohongshu \
  --query "comment note"
```

### 调用工具

先通过 `discover` / `list-tools` 获取当前真实的 tool name 和 input schema，再调用：

```bash
python3 scripts/tikhub_mcp.py call \
  --platform douyin \
  --tool CURRENT_TOOL_NAME \
  --args '{"keyword":"摄影"}' \
  --out research-output/raw/douyin/search.json
```

## 使用示例

### 任意赛道

```text
调用 my-research。
研究最近 30 天抖音和小红书的露营赛道。
先画出子赛道地图，再找 20 个代表账号，识别异常高表现内容，抓评论需求，最后给出 10 个仍有空间的内容方向。
先小样本验证，扩大请求前告诉我预计请求量。
```

### 跨平台趋势

```text
调用 my-research。
研究法国市场跑鞋内容，比较 TikTok、Instagram 和 YouTube 最近 60 天的主题差异。
不要直接比较跨平台绝对播放量；使用平台内相对表现和评论主题。
```

### 品牌 / 产品

```text
调用 my-research。
研究一个相机产品在小红书、抖音和 YouTube 上的公开讨论。
总结高频优点、吐槽、购买顾虑、竞品比较和未被充分回答的问题。
```

## 为什么使用动态 MCP 工具发现

TikHub 的平台工具目录会变化。如果把 endpoint、工具名和参数写死，Skill 很容易过时。我的研究（My Research） 先初始化 MCP，再 `tools/list`，根据当前 schema 选择工具。

## 成本

本 Skill 本身是 MIT 开源。TikHub API / MCP 使用量由 TikHub 账户单独计费；价格可能随 endpoint 和账户变化。

`scripts/estimate_cost.py` 仅用于粗略规划，不代替 TikHub 当前定价页面或账户账单。

## 安全

- 只处理公开数据
- 不绕过访问控制
- 不上传 API Key
- 不做敏感个人画像或去匿名化
- 原始数据和模型推断分开保存

## License

MIT. See the repository root `LICENSE`.
