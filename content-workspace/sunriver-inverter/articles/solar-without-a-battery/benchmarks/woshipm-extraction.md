# Benchmark Extraction — 饼干哥哥AGI / woshipm

## Article Metadata

- **Title:** 劝退：n8n等 AI工作流不要学了，已经过时了
- **URL:** https://www.woshipm.com/ (woshipm article by 饼干哥哥)
- **Author:** 饼干哥哥（微信公众号：饼干哥哥AGI）
- **Type:** Contrarian rant-with-lessons / live-demo tutorial
- **Role for Sunriver:** Voice-calibration benchmark for the first article *Solar Without a Battery: The Battery Industry Hopes You Never Read This*. Demonstrates how to open with a provocation, tear down a common assumption, walk through a real case, and land on a reframed lesson without becoming a generic explainer.

---

## 21 Success Formula Dimensions

### 1. Core Promise

The article promises that **manual node-dragging in n8n is already obsolete**, and the reader can leap directly to a higher-level skill: using AI (Claude Code + context engineering) to generate industrial-grade workflows in ~15 minutes. The practical promise is embedded in the title and first sentence: "因为我已经可以用AI纯自动生成复杂n8n工作流了。注意，不是那种生成一行几个节点的'玩具'，而是工业级别的复杂工作流。" The emotional promise is **speed + status** — the reader who adopts this method stops doing "体力活" and starts doing "业务架构能力."

### 2. Reader State

The reader arrives already interested in AI automation but is likely confused by the flood of "AI workflow" tutorials. They fear wasting time on a tool that will be replaced next quarter, or on methods that only work for toy demos. They want a **shortcut to credibility**: a way to build real workflows without becoming an n8n expert. The author assumes the reader has heard of n8n, MCP, and Claude Code, but has not yet seen them combined into a repeatable industrial pipeline.

### 3. Opening Tension

Tension is created by a **deliberate contradiction**: the title says "don't learn n8n, it's outdated," but the body immediately reveals the author is *not* abandoning n8n — he is automating it. The reader must keep reading to resolve the paradox. The opener stacks proof on top of the provocation: "例如下图 Reddit平台的DJi舆情监控工作流，就是我用AI生成的" + "我发誓没有新建一个节点…整个流程90%的节点可用." Then a second escalation: "n8n官方下场做这种AI生成工作流了…这是个很重大的二战转折点。" The reader is pulled forward by the need to see how the trick works before it becomes mainstream.

### 4. Angle

The angle is **first-person practitioner who has already crossed the gap**. The author is not reviewing a tool; he is reporting from the other side of a technique he discovered. The decision point is: *Should I keep learning n8n the old way, or switch to an AI-generated workflow strategy?* The perspective is contrarian-expert: he agrees with the title only if "learning" means manual configuration; he disagrees if it means higher-level architecture.

### 5. Question Ladder

The article answers a precise sequence:

1. Wait, is n8n really dead? → No, manual dragging is dead; AI generation is the new layer.
2. Can AI really generate a complex workflow? → Yes, here is a real Reddit/DJI screenshot.
3. What about the popular n8n-mcp approach? → It fails on real workflows; let me show you why.
4. What is the better method? → Claude Code + context engineering using existing JSON templates.
5. How do I actually do it? → Step 1 find JSONs, Step 2 batch download, Step 3 generate, Step 4 verify.
6. Does it actually run? → Mostly yes; some nodes need manual touch-up.
7. Should I still learn n8n at all? → Yes, but learn architecture, not clicking.

### 6. Information Progression

The article escalates in three acts:

- **Act 1 — Provocation + proof:** Title, claim, screenshot, official-news tease.
- **Act 2 — Debunk the common path:** The 青铜 section tests n8n-mcp and shows 80% failure.
- **Act 3 — Demonstrate the better path:** The 黄金 section walks through a real build in four numbered steps, ending in a live run.

Each act raises the stakes: from "look what I can do" → "your current method is broken" → "here is the industrial method." The density increases as the reader becomes more committed; the tutorial section is the longest because that is where the reader's trust has been earned.

### 7. Decision Framework

The implicit framework is **Bronze vs. Gold**: a two-tier model that lets the reader judge any AI-automation method by asking, "Does it rely on AI guessing from scratch, or does it learn from real existing workflows?" The author makes the judgment tool explicit near the end of the 青铜 section: "所以最佳方案是让 AI去学习已有的复杂工作流的逻辑，来模仿完成新的需求。也就是把「提示工程」转成「上下文工程」." For Sunriver, this maps cleanly to a Path A / Path B / Path C battery-or-no-battery decision framework.

### 8. Contrast

Contrast is the article's main engine. The title contrasts "劝退" with "现在学正好抢位." The body contrasts **toy vs. industrial** ("不是那种生成一行几个节点的'玩具'"), **AI guessing vs. context engineering**, **青铜 vs. 黄金**, and **manual effort vs. 15-minute generation**. Even within the demo, the author contrasts what works ("全！跑！通！了！") with what does not ("发邮件的Gmail节点…算是这个AI生成工作流的败笔"). The contrast is rarely abstract; it is shown through screenshots and specific failures.

### 9. Specificity

Specificity is high and screenshot-driven. The author names exact tools (n8n-mcp, Trae, ChatGPT5 Thinking, Claude Code, Playwright MCP, GLM-4.6, Comet), exact quantities ("6000多个模板," "找10个," "8个N8N模板链接," "90%的节点可用," "80%的节点无法直接用," "15分钟," "2k到4k," "10倍"), and exact failure modes ("没有用n8n中的Reddit的节点，光想通过code和http请求获取Reddit的数据，想吃屁呢？" / "OpenAI分析啥都没定义啊" / "code啥的都报错"). The protagonist-case is not generic: it is a DJI Reddit sentiment-monitoring workflow for an AI海外营销 client.

### 10. Information Density

Every paragraph advances either the argument, the proof, or the tutorial. There is almost no filler. Even transitional lines carry new information: "但官方生成的效果如何、以及什么时候才能用得上我们不知道" advances the timeline. The screenshot captions are functional, not decorative. The only low-density moment is the "写在最后" Q&A, which intentionally slows down to reframe the lesson — but even there, each sentence answers a specific objection.

### 11. Cognitive Load

Complexity is managed by **chunking and tiering**. The author splits the method into Bronze (simple/wrong) and Gold (advanced/right), then splits Gold into four numbered steps. Each step has a clear deliverable: find JSONs → download JSONs → generate workflow → verify. Technical details (MCP config, prompt text) are placed inside code blocks so the reader can skip them on first pass. The author also pre-announces shortcuts: "想直接看我终极方案的直接跳到文章下半部分." Screenshots reduce the need for long textual descriptions.

### 12. Rhythm

The rhythm alternates between **short punchy provocations** and **longer demo walkthroughs**. The opening uses single-sentence paragraphs ("因为我已经可以用AI纯自动生成复杂n8n工作流了。"). The 青铜 section accelerates through failure. The 黄金 section slows into step-by-step detail. Interjections ("卧槽！！", "我敲！！！", "太感人了", "问题不大") act as percussion. The article breathes at section boundaries and after major reveals, e.g., "至此，整个工作流就跑通了。" before the money paragraph.

### 13. Proof Strategy

Credibility is proven **through demonstration, not credentials**. The author does not say "I am an expert"; he shows a workflow he generated, the exact prompt, the imported JSON, and the running nodes. He also admits failure points (Gmail node misconfiguration, some subreddit/keyword pairs returning no data), which paradoxically strengthens trust. Social proof is introduced late and sparingly: "现在小红书上给公司搭建一个工作流多数是2k到4k." The only brand mention is a closing funding fact about n8n to justify why the tool still matters.

### 14. Human Texture

The author sounds like someone who has **actually burned time on broken workflows**. Phrases like "想吃屁呢？", "光想通过code和http请求获取Reddit的数据", "手动操作的话…第二步这么多个Reddit节点都要花不少时间", and "我就原谅它了" are the verbal residue of real frustration. The texture comes from complaint, not polish. Even the celebratory moments ("这真的不是magic吗？？") feel like a real person's surprise, not marketing copy.

### 15. Section Function

| Section | Job |
|---------|-----|
| Title + opener | Hook with contradiction; establish proof |
| "青铜：n8n-mcp" | Debunk the common shortcut; create problem tension |
| "黄金：Claude Code辅助" | Introduce the superior method; promise repeatability |
| Step 1: find JSONs | Show how to source existing context |
| Step 2: batch download | Remove the manual copy-paste friction |
| Step 3: generate workflow | Deliver the core "magic" moment |
| Step 4: verify workflow | Prove it runs; admit minor fixes |
| Money paragraph ("2k到4k…10倍") | Translate technical win into commercial value |
| "写在最后" | Reframe the lesson; answer the title's challenge |

### 16. (Not activated)

### 17. Actionability

Actionability is very high. The article gives **copy-paste prompts, MCP config JSON, exact tool names, and a four-step sequence** the reader can replicate. The prompts are literal templates: "我准备搭建一个reddit监控的n8n工作流…请你帮我到官方模板库…查找最合适的…给我找10个." Even the verification section tells the reader what to expect at each node. For Sunriver, the borrowable pattern is: give the reader a decision framework plus a "try this first" action, not just conceptual advice.

### 18. Friction Removal

The author explicitly removes friction at two points. First, he tells readers they can skip ahead: "想直接看我终极方案的直接跳到文章下半部分。" Second, he automates the most annoying step — downloading JSONs one-by-one from n8n's template library — by handing it to Claude Code with Playwright ("需要点两次复制json内容，再到本地手动新建json文件才行" → "所以第二步，我们让claude code出手"). For Sunriver, this translates to: identify the most annoying part of the buyer's decision (e.g., comparing inverter specs across pages) and offer a one-click shortcut or comparison table.

### 19. Editorial POV — Opinion, Thought Leadership

The POV is sharp and deliberately polarizing. The author takes a stance: "n8n等AI工作流不要学了，已经过时了" — then qualifies it. The opinion is not tacked on; it structures the entire piece. Thought leadership appears in the reframe: "我们不再需要学习的，是过去那种逐个节点拖拽、配置、连线的'体力活'。而我们必须开始学习的，是一种全新的、更高维度的业务架构能力。" For Sunriver, the equivalent stance is: "Battery-less solar is not a compromise; it is a deliberate hardware strategy."

### 20. Memorability

Memorable elements include:

- The contradictory title itself.
- The "二战转折点" metaphor for n8n's official AI move.
- The tiered headings **青铜 / 黄金**.
- The repeated failure line "想吃屁呢？"
- The surprised interjection "卧槽！！我发誓，我一步都没改…全！跑！通！了！"
- The closing challenge: "如果你能找到比这个更好的方案，欢迎评论区挑战！！"

These are not generic motivational phrases; they are **specific to the author's voice and the demo moment**.

### 21. Prose Craft / Linguistic DNA Card

This is the most important dimension for Sunriver because the target brand voice is "conversational, contrarian, rant-with-lessons."

#### Alternative Transitions

- Contradiction pivots: "但…", "但点进去看才知道有多离谱", "但官方生成的效果如何…我们不知道", "不过问题也是有的"
- Escalation pivots: "还有一个更劲爆的消息就是…", "所以…", "因此…", "也就是说…"
- Demonstration pivots: "不信？我们来试试。", "来看下我是怎么做的。", "我们逐步来看下"
- Lesson pivots: "思考一下，为什么会这样呢？", "答案很明显了", "所以，我们不再需要…而我们必须开始…"

#### Paragraph Openers

- First-person claim: "因为我已经可以用…"
- Direct command: "注意，不是那种…"
- Rhetorical challenge: "不信？我们来试试。"
- Reframing question: "所以现在的问题就变成了…"
- Justification opener: "不得不说，ChatGPT5 Thinking的搜索能力是我用过最强的。"
- Humble-confession opener: "美中不足的是…", "比较头大的问题是在…"

#### Exclamations and Emotional Markers

- Surprise: "卧槽！！", "我敲！！！", "这真的不是magic吗？？"
- Swearing-like emphasis: "想吃屁呢？"
- Gratitude/relief: "太感人了。", "问题不大。"
- Urgency: "现在学正好抢位。", "很快我们就能…"
- Status signal: "你懂我意思吧🐶"

#### Rhetorical Questions

- "所以你理解为什么我起这个标题了吧？"
- "但它到底能不能用？"
- "思考一下，为什么会这样呢？"
- "现在都能用AI生成工作流了，是不是学习没有必要了？"
- "Claude code这种Agentic Code都能完成，是不是没必要搞n8n了？"

#### Tiered Headings

- **青铜 / 黄金** — a gamified, skill-level framing. Bronze = beginner/common but flawed. Gold = advanced/right. This is highly borrowable for Sunriver as a "Wrong way / Right way" or "Basic path / Pro path" structure.

#### Metaphors and Domain Context

- "二战转折点" — historical metaphor for a technology shift.
- "玩具" vs. "工业级" — maturity metaphor.
- "体力活" — labor metaphor for manual configuration.
- "最后一公里" — logistics metaphor for final human polish.
- "magic" — English loanword used as colloquial amazement.
- "赚💰效率怕是能提升10倍" — money + emoji as proof of value.

#### Reasoning Trajectory

The author's default reasoning shape is:

1. **Bold claim** →
2. **Immediate proof or counter-example** →
3. **Walk through the wrong way** (with specific failures) →
4. **Introduce the right way** (numbered steps) →
5. **Show live results** (screenshots + honest caveats) →
6. **Reframe the lesson** in the conclusion.

For Sunriver, this becomes:

1. **Bold claim** (battery-less solar is a strategy, not a gap) →
2. **Proof/case** (real homeowner scenario or product evidence) →
3. **Wrong way** (buying a battery you do not need, or buying a non-battery-ready inverter) →
4. **Right way** (Path A / B / C framework) →
5. **Live results** (specs, ROI, compatibility) →
6. **Reframe** (the future-proofing lesson).

---

## Structural Blueprint Summary

### Borrowable Section Jobs (in order)

1. **Contradiction hook** — title promises one thing; opener reframes it.
2. **Proof before explanation** — show the end state first (screenshot / case / number).
3. **Industry-news escalation** — add a "this is bigger than you think" beat.
4. **Wrong-way teardown** — name a common method, demonstrate its failure with specifics, explain why it fails conceptually.
5. **Right-way introduction** — transition with "所以最佳方案是…" and introduce the superior framework.
6. **Step-by-step demonstration** — 3–4 numbered steps, each with a clear deliverable.
7. **Live verification** — show what worked and what needed a small manual fix.
8. **Commercial translation** — convert the technical result into money/time value.
9. **Lesson reframe** — answer the title's challenge and leave the reader with a higher-level principle.
10. **Open challenge / CTA** — invite disagreement or next action.

### Pacing

- **0–15%:** Hook + proof (fast, high energy).
- **15–35%:** Teardown of the common approach (moderate, diagnostic).
- **35–80%:** Live method walkthrough (slowest, most detailed).
- **80–90%:** Verification + commercial value (energy returns).
- **90–100%:** Reframe + send-off (reflective but punchy).

### Evidence Rhythm

Evidence appears in waves:

- **Wave 1:** Screenshot of generated workflow.
- **Wave 2:** Screenshots of n8n-mcp failing.
- **Wave 3:** Prompt text + download screenshots.
- **Wave 4:** Imported workflow screenshot + node-level verification.
- **Wave 5:** Funding news + money statement.

There is no long block of theory without a visual or example.

### AIO / Answerability Moments

The article naturally captures AIO-style answers because it asks and resolves specific questions:

- "Can AI generate real n8n workflows?" → Yes, with context engineering.
- "Why does n8n-mcp fail?" → It relies on AI guessing instead of learning existing logic.
- "What is the better method?" → Claude Code + existing JSON templates.
- "Should I still learn n8n?" → Learn architecture, not manual configuration.

For Sunriver, equivalent answerable moments would be:

- "Can a hybrid inverter run without a battery?" → Yes, the SAJ H2 runs in grid-tied mode.
- "Is solar without a battery a bad idea?" → Not if you choose a battery-ready path.
- "What is the cheapest future-proof setup?" → Path A/B/C framework.

### Rant → Demonstration → Lesson-Pivot Arc

The article follows a clean emotional arc:

- **Rant (provocation):** "不要学了，已经过时了。"
- **Demonstration (credibility):** Full live build with screenshots.
- **Lesson pivot (reframe):** "我们不再需要学习…体力活；我们必须开始学习…业务架构能力。"

Sunriver should mirror this: rant against the "battery is mandatory" assumption → demonstrate with product evidence and a homeowner case → pivot to "the real skill is choosing the right battery-ready hardware path."

---

## Reader Advancement Mechanism

| Stage | Reader mental state | What the section does |
|-------|---------------------|-----------------------|
| Arrival | Skeptical / curious about "n8n is dead" | Title creates dissonance; opener resolves part of it with proof |
| Commitment | Wants to believe but needs evidence | Screenshot + "90%可用" lowers doubt |
| Doubt | "What about the popular MCP method?" | 青铜 section validates and then destroys that path |
| Orientation | "So what should I do instead?" | 黄金 section introduces context engineering |
| Execution | "Can I actually do this?" | Step-by-step tutorial with copy-paste prompts |
| Verification | "Does it really work?" | Step 4 shows running nodes and honest caveats |
| Valuation | "Is this worth my time?" | "2k到4k…10倍" translates to money |
| Reflection | "What does this mean for my career/strategy?" | 写在最后 reframes the learning question |
| Action | "I want to try / argue / share" | Open challenge invites comment engagement |

The reader is never asked to trust for more than one section at a time. Each section earns the next.

---

## What to Borrow / What NOT to Borrow for Sunriver

Reference: project-profile.md §5 Brand Voice and Red Lines; §7 Benchmark Policy.

### Borrow

1. **Contradiction-title structure.** A title that seems to reject the topic, then reframes it in the opening. For Sunriver: the title already does this (*Solar Without a Battery: The Battery Industry Hopes You Never Read This*).
2. **Proof-before-explanation opener.** Show the end state (battery-ready system running without a battery) before explaining the method.
3. **青铜 / 黄金 (Wrong-way / Right-way) tiered framing.** Highly borrowable as "The retrofit trap" vs. "The battery-ready path."
4. **Specific failure narration.** The author lists exactly why n8n-mcp fails. Sunriver should list exactly why a non-battery-ready inverter or premature battery purchase fails.
5. **Numbered protagonist case.** The DJI Reddit workflow is a concrete client scenario. Sunriver should use a concrete homeowner/EPC scenario with realistic specs and location.
6. **Honest caveats within proof.** "Gmail节点…算是败笔" builds trust. Sunriver should admit real trade-offs (e.g., no backup during outage, future battery cost not guaranteed).
7. **Lesson-pivot conclusion.** Reframe from "avoid batteries" to "choose the right battery-ready hardware path."
8. **Open challenge CTA.** "如果你能找到比这个更好的方案，欢迎评论区挑战！！" can become an invitation to share project specs for a custom path recommendation.
9. **Colloquial emotional markers in moderation.** Phrases like "magic" ("这不是magic吗"), "问题不大," "最后一公里的打磨" can be adapted into English equivalents.
10. **AIO-ready Q&A embedded in the narrative.** Each major objection becomes a mini answer block.

### Do NOT Borrow

1. **Do not bash batteries.** project-profile.md §7 states: "Sunriver does not bash batteries; it argues for the right timing and the right hardware path." The woshipm title is harsher than Sunriver's stance should be.
2. **Do not copy Chinese phrasing or swearing.** "想吃屁呢？", "卧槽", "我敲" are voice-calibration references only; the English article must develop its own colloquial register.
3. **Do not overclaim automation.** The author says "90%的节点可用" and admits fixes. Sunriver must not claim any SAJ product works with any battery or needs zero configuration.
4. **Do not use unsubstantiated pricing.** project-profile.md §5 forbids "specific pricing without a published source." The "2k到4k" anecdote is fine for the benchmark but cannot be copied unless Sunriver has a published source.
5. **Do not make the article a screenshot dump.** The benchmark is image-heavy because it is a UI tutorial. Sunriver's article should use comparison tables, diagrams, and product specs rather than endless screenshots.
6. **Do not become a generic explainer.** project-profile.md §7 warns: "Avoid becoming a generic explainer; maintain the contrarian angle and clear product routing."
7. **Do not omit compliance boundaries.** project-profile.md §5 requires tax/regulatory claims to be framed as "as of 2026 / confirm with a licensed professional." The benchmark has no compliance content, so Sunriver must add this discipline.
8. **Do not lose the supply-partner perspective.** The author is a solo practitioner. Sunriver's voice must remain that of a knowledgeable supply partner helping buyers avoid the retrofit trap, not a lone hacker showing off.

---

*Extraction prepared for /article-skeleton and /article-draft voice calibration. Do not treat this as a final outline or H2 list.*
