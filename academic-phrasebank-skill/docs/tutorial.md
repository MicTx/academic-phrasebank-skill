# 把一段 Results 写稳：一次受约束的修改

修改论文时，最容易走错的路是从同义词开始。句子变长了，语气变强了，数字却可能被改动，关联也可能被写成因果。

下面只做一件事：把一段示意 Results 改到“表达顺、证据不越界”。示例中的数字、人名和研究对象都是演示材料。

## 1. 先确定这段话要让读者相信什么

开始前先回答三个问题：

1. 这段属于 Introduction、Methods、Results、Discussion 还是 Conclusion？
2. 读者应该带走一个观察、一个解释，还是一个有条件的推论？
3. 哪些内容绝对不能改变？

对科学手稿，第三个问题通常包括数字、单位、变量、方向、样本量、方法名称、引用和不确定性。先列出这些内容，后面的语言变化才可检查。

## 2. 把句子按功能拆开

示意原文：

> We analyzed 248 households. The intervention group had a higher recycling rate than the control group (β = 0.18, 95% CI 0.07–0.29, p = 0.002). The association remained after adjustment for income and household size. This proves that the intervention caused the increase in recycling, and the effect should apply to all urban households.

逐句看，它实际上包含四个动作：

- 样本和分析对象；
- 组间差异及统计量；
- 调整变量后关联仍然存在；
- 因果判断和普遍推广。

前三个动作属于 Results。最后一个动作超出了这段材料能支持的范围。问题因此不是“哪个词不够地道”，而是证据层级混在了一起。

## 3. 把约束写进提示词

不要只说“帮我润色”。把任务、位置、保护条件和禁止事项一次写清楚：

```text
$academic-phrasebank-skill
Polish this Results paragraph for a concise SCI manuscript.
Preserve 248 households, β = 0.18, 95% CI 0.07–0.29, p = 0.002,
the direction of the association, and the adjustment variables.
Do not add citations, mechanisms, or new results.
Replace unsupported causal or universal claims with wording that matches
an association observed in this sample. Return the revised paragraph and
two short sentences describing the meaning-preservation checks.
```

这里有四种约束：

- **任务**是 Results 段润色，不是重新分析结果。
- **保护内容**列出了样本、统计量、方向和调整变量。
- **禁止新增**把引用、机制和新结果挡在外面。
- **目标修正**明确要求收回因果和普遍化，而不是笼统地“更谨慎”。

## 4. 先看改后版本，再逐项对账

一版合格的结果可以是：

> Among the 248 households, the intervention group had a higher recycling rate than the control group (β = 0.18, 95% CI 0.07–0.29, p = 0.002). This association remained after adjustment for income and household size. The findings describe a difference between the groups in this sample; they do not establish that the intervention caused the increase or that the result generalises to all urban households.

现在对照原文核查：

1. 样本量仍然是 248 个家庭吗？
2. β、置信区间和 p 值的数值、符号和方向是否完全保留？
3. 干预组高于对照组的关系有没有被反转？
4. income 和 household size 是否仍然存在？
5. 是否还把 association 写成 causes、proves 或 will apply？

最后一句不是为了让文章听起来更弱，而是让读者知道证据到哪里为止。谨慎表达的目标是精确，不是含糊。

## 5. 同一套方法可以用于翻译

中文示意材料：

> 本研究采用随机森林（random forest, RF）评估城市热岛强度。结果显示，夜间地表温度与建筑密度呈正相关（r = 0.62，p < 0.001），但该结果不能证明建筑密度导致热岛增强。由于样本仅覆盖夏季的三个城区，结论能否推广到其他季节和地区仍需进一步验证（见[REF]）。

提示词可以这样写：

```text
$academic-phrasebank-skill
Translate this paragraph into concise academic English.
Preserve random forest (RF), urban heat-island intensity,
nighttime land-surface temperature, building density, r = 0.62,
p < 0.001, the non-causal limitation, the three summer districts,
the uncertainty about generalisation, and [REF].
Do not invent authors, years, or references. Return only the translation,
followed by one short note if an ambiguity must remain visible.
```

可能的译文：

> This study used a random forest (RF) to assess urban heat-island intensity. The results showed a positive correlation between nighttime land-surface temperature and building density (r = 0.62, p < 0.001), but this correlation does not establish that building density causes stronger heat-island effects. Because the sample covered only three districts in summer, whether the findings generalise to other seasons and regions requires further validation (see [REF]).

The verbs used, showed, and requires report method, result, and remaining uncertainty. Translation checks information relations, not word-for-word matching.

## 6. Discussion 先分动作，再修句子

如果一段话把结果、解释、局限和政策承诺揉在一起，先让工具拆成四个动作：

```text
$academic-phrasebank-skill
Restructure this Discussion passage into four moves: observed result,
possible interpretation, limitation, and implication.
Keep 22%, RMSE 4.1 versus 5.3, one region, one season,
Lee et al. (2021), and [REF] unchanged.
Treat the attention layer as a possible explanation, not a demonstrated
causal mechanism. Do not claim universal transfer or replacement of field measurements.
```

重构后的逻辑应当是：

> The model reduced prediction error by 22%, with RMSE decreasing from 5.3 to 4.1. The attention layer may contribute to this improvement, although the present results do not establish that it captures the system's causal structure. Because the analysis covered one region and one season, transferability to other regions and seasons remains untested. The model therefore warrants evaluation on broader datasets before it is considered for applications that currently rely on field measurements (see [REF]).

四句分别承担观察、可能解释、局限和有条件的含义。它们不再互相冒充。

## 7. 处理整篇手稿时，从高层往下走

按这个顺序检查：

1. **诊断结构。** 研究问题、空白、目标、方法、发现和贡献是否连得起来？
2. **重构章节。** Results 是否只报告结果？Discussion 是否承担解释和局限？
3. **修复段落。** 每段只保留一个主动作，并补上证据到结论的桥。
4. **润色句子。** 再处理语法、清晰度、连接和学术语域。
5. **统一全文。** 最后检查术语、缩写、单位、图表引用、时态和谨慎程度。

如果只想知道问题在哪里，明确要求 diagnose 且暂不改写：

```text
$academic-phrasebank-skill
Diagnose this manuscript section. Identify structural, paragraph,
sentence, and phrase-level problems with their locations.
Do not rewrite the text yet. Preserve all numbers, citations,
placeholders, and uncertainty markers.
```

## 8. 五个常见误区

- **只说“帮我润色”。** 没有章节、目标和保护条件，结果很难验收。
- **把模板当成结论。** X、Smith 和 Jones 是示例，不是你的研究对象或作者。
- **用强词掩盖证据不足。** proves、causes 和 will work in every region 都需要相应设计支持。
- **让语言工具猜文献。** 缺文献就保留 [REF]，再走可核查的检索流程。
- **句子不顺就换词。** 根因可能是段落把结果和讨论混在一起；先提高处理层级。

## 9. 可复制的任务模板

```text
$academic-phrasebank-skill
Task: [draft / translate / revise / polish / restructure / diagnose]
Section: [Introduction / Methods / Results / Discussion / Conclusion]
Audience or journal style: [optional]

Preserve exactly:
- numbers, units, variables, statistical notation
- terminology, abbreviations, named methods
- citations and placeholders such as [REF]
- uncertainty and evidence strength

Do not:
- invent references, results, methods, mechanisms, or statistics
- strengthen association into causation
- generalise beyond the stated sample or design

Return: [revised text / diagnosis / revised text plus concise change note]
Text:
[paste the passage here]
```

## 10. 最后的五个问题

1. 所有数字、符号、方向、单位和样本量是否与原文一致？
2. 结果、解释、机制、建议和推广是否使用了不同强度的措辞？
3. 引用和 [REF] 是否都可追溯？
4. 同一个概念是否始终使用同一个术语和缩写？
5. 这段文字是否仍属于目标章节？

如果有一项答不上来，就把问题交回作者或相应的科学工作流。这个 skill 能让已有证据更清楚、更连贯、更可审查，但不能替代研究判断。
