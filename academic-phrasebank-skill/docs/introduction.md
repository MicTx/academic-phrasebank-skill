# 科研英语的第一步：先守住证据，再改善表达

科研英语常被误解成“把普通词换成更难的词”。真正危险的地方通常更早出现：一句 Results 把关联写成因果，一段 Discussion 把可能解释写成机制，或者一个局部样本被推广成所有对象。

Academic Phrasebank Skill 处理的是这条边界。它帮助你起草、翻译、重写、诊断和润色英文科研手稿，同时把数字、术语、引用和证据强度留在原来的位置。

## 先看一个最小例子

下面的数字只是演示材料。假设研究比较了 248 个家庭，干预组回收率更高，回归系数为 β = 0.18，95% CI 为 0.07–0.29，p = 0.002。原句却写成：

> The intervention caused the increase in recycling, and the effect should apply to all urban households.

这句话同时跨过了两道证据边界：它把关联写成了因果，又把当前样本推广到所有城市家庭。

一个更稳的改法是：

> The intervention group had a higher recycling rate than the control group (β = 0.18, 95% CI 0.07–0.29, p = 0.002). This association does not establish that the intervention caused the increase or that the result generalises to all urban households.

第一句核对观察，第二句说明观察没有支持什么。语言变清楚的同时，证据没有变强。

## 它究竟在改什么

把 Phrasebank 当成修辞模式库，而不是结论库。先问句子要完成哪个动作，再选择模式：

- 引出研究背景、空白、目标或贡献；
- 说明设计、样本、材料、程序和分析；
- 报告结果、数量、趋势和比较；
- 区分观察、解释、局限、含义和建议；
- 定义术语、引用来源、承接段落或表达谨慎程度。

如果问题在段落顺序，就先重构；如果顺序已经成立，再润色句子。一个漂亮的句子不能修复章节功能混乱。

## 它怎样工作

使用时，先给出四类信息：

1. **任务**：draft、translate、rewrite、polish、restructure 或 diagnose。
2. **位置**：Introduction、Methods、Results、Discussion、Conclusion 或摘要。
3. **保护条件**：数字、单位、变量、缩写、引用、方法名、占位符和不确定性。
4. **交付形式**：改后全文、诊断报告、备选版本或简短改动说明。

例如：

```text
$academic-phrasebank-skill
Polish this Results paragraph. Preserve every number, citation, variable,
and uncertainty marker. Do not add interpretation or references.
```

如果你还不知道问题在哪一层，先要求诊断：

```text
$academic-phrasebank-skill
Diagnose this Discussion section at manuscript, section, paragraph,
sentence, and phrase levels. Do not rewrite it yet. Keep [REF] unchanged.
```

它会先判断最高层级的问题，再决定是否需要动到句子。你也可以只让它使用某个章节参考页，不必加载全部句型。

## 哪些东西不能由它替你决定

它不会凭空补充实验结果、方法细节、机制、统计数字或参考文献，也不会把 “proves” 换成另一个强词来替你完成科学判断。

它可以把“结果提示某种解释”写得清楚，却不能把提示变成证明；可以保留 [REF]，却不能替你完成文献检索；可以明确局限，却不能替你判断结论是否足以推广。

遇到缺少的信息，保留 [REF] 或提出一个具体问题。不要用看起来合理的内容填空。

## 参考材料从哪里来

项目中的参考页来自公开的 [Manchester Academic Phrasebank](https://www.phrasebank.manchester.ac.uk/about-academic-phrasebank/)，覆盖研究背景、文献、方法、结果、讨论、结论，以及比较、因果、数量、趋势、举例、过渡和谨慎表达。

这些页面提供句型和修辞动作，不提供你的数据或证据。上游页面、抓取范围和归属信息见 [source-coverage.md](../references/source-coverage.md) 和仓库根目录的 [NOTICE.md](../../NOTICE.md)。

## 下一步

先读 [tutorial.md](tutorial.md)，跟着一段示意 Results 做完一次受约束的修改；需要选择参考页时，从 [references/index.md](../references/index.md) 开始。

如果只记住一个原则，请记住：**先让语言准确表达证据，再让语言变得漂亮。**
