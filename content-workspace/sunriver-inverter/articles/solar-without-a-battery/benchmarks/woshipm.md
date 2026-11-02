[![](https://image.woshipm.com/2023/06/14/57e3c074-0aae-11ee-a1ce-00163e0b5ff3.jpg?x-oss-process=image/quality,q_80/format,webp)](https://ke.qidianla.com/courses/bcpm)
##  劝退：n8n等 AI工作流不要学了，已经过时了
[![](https://static.woshipm.com/APP_U_202108_20210823113945_8828.jpeg?imageView2/1/w/72/h/72/q/100)](https://www.woshipm.com/u/1211103)
[饼干哥哥](https://www.woshipm.com/u/1211103) ![](https://static.woshipm.com/tag/1101_1@2x.png%20) 关注
2025-10-17
2 评论 18 分钟
[ 企业都想把AI落到业务里，缺的不是会聊天的人，而是懂需求、懂场景、能把AI做成产品的人，现在学正好抢位。](https://ke.qidianla.com/courses/aipmtc)
> AI生成工作流不是“玩具”，而是“工业级自动化”的新起点。本文将系统解析n8n工作流的演进逻辑，从Claude Code辅助到上下文工程的实践路径，揭示AI如何重构自动化流程的设计范式，并构建一套可落地的工作流生成框架，帮助产品人理解“AI工作流”的新边界。
![](https://image.woshipm.com/2024/05/11/bf6c8bc2-0f67-11ef-b3fd-00163e142b65.png)
因为我已经可以用AI纯自动生成复杂n8n工作流了。
注意，不是那种生成一行几个节点的“玩具”，而是工业级别的复杂工作流。
例如下图 Reddit平台的DJi舆情监控工作流，就是我用AI生成的：
![](https://image.woshipm.com/2025/10/17/dbee444a-aac8-11f0-bc91-00163e4b86a1.png)
我发誓没有新建一个节点，包括里面的备注说明全是AI自己生成的，而且整个流程90%的节点可用，剩下的可能花不到 10 分钟就 ok 了！！！
还有一个更劲爆的消息就是n8n官方下场做这种 AI生成工作流了，很快我们就能在n8n里完成自动工作流的生成。
这是个很重大的二战转折点。所以你理解为什么我起这个标题了吧？
![](https://image.woshipm.com/2025/10/17/dcbbbeac-aac8-11f0-bc91-00163e4b86a1.png)
但官方生成的效果如何、以及什么时候才能用得上我们不知道。
接下来，可以先看下我探索出来的AI 生成n8n工作流的最佳实践。
## 青铜：n8n-mcp
开始前，先吐槽一下网上很多博主推荐的 n8n-mcp
它确实很不错，能自动去搜索最新的节点、n8n规则，但也只限于拿来做玩具、生成简单流程。
不信？我们来试试。
想直接看我终极方案的直接跳到文章下半部分。
![](https://image.woshipm.com/2025/10/17/dd81ff0e-aac8-11f0-bc91-00163e4b86a1.png)
项目地址：https://github.com/czlonkowski/n8n-mcp
以下是配置 MCP的模板：
> {
> “mcpServers”:{
> “n8n-mcp”:{
> “command”:“npx”,
> “args”:[“n8n-mcp”],
> “env”:{
> “MCP_MODE”:“stdio”,
> “LOG_LEVEL”:“error”,
> “DISABLE_CONSOLE_OUTPUT”:“true”,
> “N8N_API_URL”:“https://your-n8n-instance.com”,
> “N8N_API_KEY”:“your-api-key”
> }
> }}}
其中，N8N_API_KEY需要到n8n控制台的设置-n8n API的位置
按如下操作来获取。
![](https://image.woshipm.com/2025/10/17/de31407c-aac8-11f0-bc91-00163e4b86a1.png)
这里我用 Trae 来试下，添加 MCP后，让他创建一个文章开头那样的 Reddit 舆情监控流程：
简单的流程我就不测了哈，意义不大，感兴趣可以自己去试下。
![](https://image.woshipm.com/2025/10/17/dece6bf4-aac8-11f0-bc91-00163e4b86a1.png)
![](https://image.woshipm.com/2025/10/17/df6d4abc-aac8-11f0-bc91-00163e4b86a1.png)
整个过程它会不断的去查找节点，干的事还是蛮多的，然后在你n8n 空间中创建一个工作流
![](https://image.woshipm.com/2025/10/17/e0172b72-aac8-11f0-bc91-00163e4b86a1.png)
![](https://image.woshipm.com/2025/10/17/e0bc4c1a-aac8-11f0-bc91-00163e4b86a1.png)
![](https://image.woshipm.com/2025/10/17/e176179e-aac8-11f0-bc91-00163e4b86a1.png)
回到n8n工作台刷新一下就有了：
![](https://image.woshipm.com/2025/10/17/e2260b54-aac8-11f0-bc91-00163e4b86a1.png)
但点进去看才知道有多离谱：
1 是没有用 n8n 中的Reddit 的节点，光想通过 code 和 http请求获取Reddit 的数据，想吃屁呢？
![](https://image.woshipm.com/2025/10/17/e2bb7c84-aac8-11f0-bc91-00163e4b86a1.png)
2 是后面OpenAI 分析啥都没定义啊
![](https://image.woshipm.com/2025/10/17/e33f03ce-aac8-11f0-bc91-00163e4b86a1.png)
3 是运行一下 code 啥的都报错
总而言之就是80% 的节点无法直接用，跑不起来。
思考一下，为什么会这样呢？
n8n-mcp的逻辑是根据用户需求去n8n库里查找节点，然后再按自己的逻辑去把节点连起来。
问题恰恰就在整个过程都是AI 自己的判断，并没有业务逻辑
它可能会是最理性的，用最短路径来完成。
但实际上业务逻辑是很多合并、循环之类的操作，才能完成复杂需求。
所以最佳方案是让 AI去学习已有的复杂工作流的逻辑，来模仿完成新的需求。
也就是把「提示工程」转成「上下文工程」
## 黄金：Claude Code辅助
所以现在的问题就变成了，如何让 AI 根据你的需求，自动找到合适的几个n8n工作流，然后参考他们来搭建你的工作流需求？
这是核心逻辑。
来看下我是怎么做的。
正好我AI海外营销业务要给客户搭建Reddit舆情监控工作流，就拿这个场景试下
### Step1：找到需求相关的json
让 AI去搜索网上已有的工作流 json，尤其是官方的模板库里面有 6000 多个模板，绝对有跟你需求接近的几个。💡
> 我准备搭建一个reddit 监控的n8n 工作流， 用于品牌竞品、负面舆情、用户痛点洞察等需求：
> “`
> 你的方案
> “`
> 请你帮我到官方模板库（https://n8n.io/workflows/）、x 推特 、YouTube 等地方查找最合适的、现成的n8n 工作流模板给我参考，给我找 10 个，都要附上来源链接。
不得不说，ChatGPT5 Thinking 的搜索能力是我用过最强的。
![](https://image.woshipm.com/2025/10/17/e3d6c59c-aac8-11f0-bc91-00163e4b86a1.png)
但打开这些官方的模板才发现，有点麻烦，需要点两次复制 json 内容，再到本地手动新建 json 文件才行。
![](https://image.woshipm.com/2025/10/17/e4698ed6-aac8-11f0-bc91-00163e4b86a1.png)
### Step2：一键批量下载 json
所以第二步，我们让 claude code出手
参考我之前的案例：两句话，让Claude Code+Kimi K2 跑了3小时爬完17个竞品网站、做了一份深度市场数据分析报告
用 Playwright 去完成这个无脑的操作：💡
> 调用 playwright mcp 工具，逐个访问以下的8个N8N模板链接，在每个链接的页面，找到use for free 按钮点击，在弹窗点Copy template to clipboard[JSON] 然后 在本地文件夹创建一个 json 文件把复制的内容黏贴进去。也就是总共生成 8 个 json
> “`
> 这里把前面 ChatGPT的搜索结果放这里
> “`
对了，本次案例用的模型都是GLM-4.6效果很丝滑。
此时，Claude Code会自动调用浏览器，完成任务
于是你就得到了多个跟你需求类似的n8n工作流json 文件。
![](https://image.woshipm.com/2025/10/17/e5060504-aac8-11f0-bc91-00163e4b86a1.png)
### Step3：生成工作流
最后，还是在 Claude Code 里，参考以下提示词，让AI 生成工作流文件即可：
> 当前文件夹是Reddit 相关的n8n工作流json 文件，你务必要每个文件都完整浏览一遍后，完成以下需求：
> “`
> 大疆（DJI）Reddit舆情监控流程
> 目标：自动监控Reddit上关于大疆及其竞品的讨论，及时发现问题和机会。
> 第一步：设定监控指令 (Inputs)
> 您需要提供两份清单：
> 关键词列表 (Keywords)：
> – 品牌词：DJI, 大疆
> – 产品词：Mavic, Air, Mini, Inspire, Phantom, Avata, Osmo, Ronin
> – 痛点词：flyaway（炸机）, GPS lost, battery drain, firmware update, no signal, customer service, gimbal issue, app crash, no-fly zone
> – 竞品词：Autel, Parrot, Skydio, Yuneec, Hubsan, PowerVision
> 社区列表 (Subreddits)：
> – r/dji
> – r/drones
> – r/Multicopter
> – r/UAV
> – r/Quadcopter
> – r/DronePhotography
> 第二步：N8N自动化流程 (Workflow)
> 定时启动：
> 系统周自动运行一次。
> 抓取内容：
> 自动抓取上述社区中，包含上述关键词的最新帖子和评论。
> AI分析：
> AI阅读每一条内容，并打上标签：
> – 情感：好评 / 差评 / 中性
> – 主题：飞行表现 / 硬件问题 / 软件/App / 客户服务 / 售后服务 / 法规合规
> – 是否紧急：是 / 否
> 自动处理：
> – 紧急情况（如严重负面）：立刻通过谷歌邮件发警报。
> – 所有情况：将分析结果自动存入一张Google表格中。
> 第三步：最终成果 (Output)
> 您会得到一个实时更新的在线报告，包含：
> – 数据看板：过去7 天总提及量、差评占比。
> – 竞品对比图：大疆 vs Autel vs Parrot等每日讨论量。
> – 痛点排行榜：用户抱怨最多的是什么（如炸机、固件问题等）。
> – 最新差评列表：包含原文链接，方便您快速处理。
> “`
> 最终给我新建一个n8n工作流json 文件，其中，注意 AI相关任务通过 AI Agent 的节点搭配 openai 的model 来完成。
静候一会，就看到文件夹新增好了json，并且提醒我们要去做一些节点的配置。
![](https://image.woshipm.com/2025/10/17/e59d3a96-aac8-11f0-bc91-00163e4b86a1.png)
接着把 json 文件导入n8n：
![](https://image.woshipm.com/2025/10/17/e63771b0-aac8-11f0-bc91-00163e4b86a1.png)
我敲！！！这真的不是 magic 吗？？
生成的工作流已经跟我想象中的非常接近了，要知道，从第一步到现在才过去 15 分钟
![](https://image.woshipm.com/2025/10/17/e6c971e6-aac8-11f0-bc91-00163e4b86a1.png)
如果我手动操作的话，下面第二步这么多个 Reddit 节点都要花不少时间。
而且都给我写好了每一步的备注了，太感人了。
### Step4：工作流验证
但它到底能不能用？
我们逐步来看下
**第一步**
没什么问题，我们要求写的就是按周监控。
![](https://image.woshipm.com/2025/10/17/e754d9d4-aac8-11f0-bc91-00163e4b86a1.png)
**第 2 步**
卧槽！！我发誓，我一步都没改，只是双击 Reddit 节点做认证，然后全！跑！通！了！
![](https://image.woshipm.com/2025/10/17/e7ec4a94-aac8-11f0-bc91-00163e4b86a1.png)
每个节点都有设置好对应哪个 subreddit、什么关键词
![](https://image.woshipm.com/2025/10/17/e8837324-aac8-11f0-bc91-00163e4b86a1.png)
不过问题也是有的，但不在技术，而在业务，就是可以看到有几个节点是没有结果的
不是报错了，而是对应社区的关键词可能不对，并没有搜索出结果
所以问题是在前面的方案没生成好，后续可以让 ai 再去调研一下哪些社区搭配什么关键词比较合适。
![](https://image.woshipm.com/2025/10/17/e922f2e6-aac8-11f0-bc91-00163e4b86a1.png)
问题不大，继续走。
第三步也跑通了你敢信？
![](https://image.woshipm.com/2025/10/17/e9b7e374-aac8-11f0-bc91-00163e4b86a1.png)
AI Agent 节点，提示词都给写好了
![](https://image.woshipm.com/2025/10/17/ea4c5428-aac8-11f0-bc91-00163e4b86a1.png)
美中不足的是，最后用的是Code 节点来把 AI 的结果做解析
![](https://image.woshipm.com/2025/10/17/eae5e728-aac8-11f0-bc91-00163e4b86a1.png)
实际上在 AI Agent 下用Output Paser就可以了。
但问题不大，毕竟code 都写好能正常解析了，我就原谅它了。
最后两步一起看：
![](https://image.woshipm.com/2025/10/17/eb9e209a-aac8-11f0-bc91-00163e4b86a1.png)
Google Sheets的部分需要自己新建好对应的文档加好列才行
![](https://image.woshipm.com/2025/10/17/ec371df4-aac8-11f0-bc91-00163e4b86a1.png)
不想麻烦的，可以搭配 AI浏览器 例如 Comet，自动帮我们搭建好
对了，Comet 的教程在路上了，感兴趣的可以评论区催更
![](https://image.woshipm.com/2025/10/17/ecdf39d0-aac8-11f0-bc91-00163e4b86a1.png)
运行节点就能给丝滑存进去了：
![](https://image.woshipm.com/2025/10/17/ed6e750a-aac8-11f0-bc91-00163e4b86a1.png)
比较头大的问题是在发邮件的 Gmail节点 上
节点配置是错的，算是这个AI 生成工作流的败笔
![](https://image.woshipm.com/2025/10/17/edf960fc-aac8-11f0-bc91-00163e4b86a1.png)
不过说实话，手动配置一下邮件内容啥的的，问题也不是很大。
至此，整个工作流就跑通了。
现在小红书上给公司搭建一个工作流多数是2k到4k
现在用这套方案，赚💰效率怕是能提升10倍，你懂我意思吧🐶
## 写在最后
经常会有朋友问我：
现在都能用AI生成工作流了，是不是学习没有必要了？
很多工作流的场景，Claude code 这种 Agentic Code 都能完成，是不是没必要搞n8n了？
![](https://image.woshipm.com/2025/10/17/ee81468e-aac8-11f0-bc91-00163e4b86a1.jpg)
最近，n8n向英伟达在内的知名机构融资1.8 亿美元，估值飙升到了 25 亿。
答案很明显了，AI 需要一个稳定、可靠的底层框架来执行任务，而 n8n 正是这个框架的最佳选择之一。
得益于 AI 发展，现在n8n大部分繁琐可以自动化，但永远有最后一公里需要人去探索和打磨。
所以，我们不再需要学习的，是过去那种逐个节点拖拽、配置、连线的“体力活”。
而我们必须开始学习的，是一种全新的、更高维度的业务架构能力。
对了，如果你能找到比这个更好的方案，欢迎评论区挑战！！
我们一起用AI把复杂繁琐的动手搭建过程给干掉！
本文由人人都是产品经理作者【饼干哥哥】，微信公众号：【饼干哥哥AGI】，原创/授权 发布于人人都是产品经理，未经许可，禁止转载。
题图来自Unsplash，基于 CC0 协议。
