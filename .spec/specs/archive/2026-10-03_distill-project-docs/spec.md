# Rewrite project documentation for human and LLM readability - 项目范围

## 1. 问题定义
- **项目目标**：使用 distill-writing 的问题链、渐进引入和诚实边界，重写项目维护的文档，使人类读者能快速找到下一步，也使 LLM 能稳定识别目的、输入、约束、输出和验证方式。
- **目标用户**：第一次安装技能的研究者、使用或维护技能的贡献者、审查发布包的维护者，以及需要从文档中提取操作契约的 LLM。
- **核心价值**：文档在不改变安装契约、科学写作边界、上游归属和生成数据的前提下，提供可执行、可验证、术语一致的阅读路径。

## 2. 假设与待确认

### 2.1 已确认事实
- 项目包含根目录治理/维护文档、`.github/pull_request_template.md`、`academic-phrasebank-skill/SKILL.md`、两篇用户指南，以及手工维护的索引、来源覆盖和修订框架。
- Phrasebank 句型页由 `tools/build_phrasebank_refs.py` 从 Manchester Academic Phrasebank 生成；原句和来源不能在本轮自由改写。
- `tools/validate_skill_package.py`、skill-creator quick validator、Python 单元测试和发布构建是现有验证入口。
- 当前工作树在任务开始前已有 README、CHANGELOG、Agent.md 和两篇指南的未提交改动；这些改动已保留并纳入本轮范围。

### 2.2 关键假设
- “所有文档”指项目维护的说明性 Markdown 与发布/治理文档；法律文本、生成的上游句型正文、原始抓取数据和机器可读配置不属于可自由重写的说明文档。
- 项目对外主要使用英文，因此英文项目文档继续使用英文；任务包和验收记录使用中文。
- 改写可以调整结构、标题、解释和示例，但不能改变命令、路径、安装目标、版本事实、许可证归属或技能行为契约。

### 2.3 待确认问题
- 无

### 2.4 可选解释与取舍
- 当前选择：把“可读性重写”与“上游内容改写”分开 -> 前者服务项目用户，后者会破坏可复现生成和归属链。
- 当前选择：先改阅读入口，再改细节文档 -> 读者必须先知道该读哪一页，LLM 才能正确选择局部参考。

## 3. 功能范围

### 3.1 核心功能（MVP）
- [x] 重写根 README、贡献/开发/支持/安全/行为准则/通知/变更记录、Agent.md 和 PR 模板，使目的、读者、路径、边界和验证入口清晰。
- [x] 重写 `academic-phrasebank-skill/SKILL.md`，保留 frontmatter、触发范围和 evidence-preserving 契约，改成模型可执行的分层工作流。
- [x] 重写两篇指南、`references/index.md`、`revision-framework.md` 和 `source-coverage.md`，形成从首次使用到深入参考的连贯路径。
- [x] 为生成的 Phrasebank 参考页补充统一入口说明（通过生成器实现），明确用途、来源、占位符和“不把句型当事实”的边界，同时保留生成短语。
- [x] 运行文档链接、skill 包、单元测试和发布构建验证。
- [x] 将本项目特有的生成/发布文档事实沉淀到项目自己的 `.spec/docs/`，不写入全局记忆。

### 3.2 扩展功能
- 无。本轮不增加站点、文档生成框架或新的运行时功能。

### 3.3 不在范围内
- 不改 `LICENSE` 的法律文本，不重写 `data/raw/` 原始 HTML，不改 `academic-phrasebank-skill/evals/evals.json` 或 `agents/openai.yaml`。
- 不改生成参考页中的上游句型、数字、引用、来源 URL 或覆盖统计；不以手工编辑替代生成器。
- 不改变安装路径、skill 名称、命令格式、发布归档内容规则和科学证据保护行为。
- 不新增翻译版本、网站、交互式教程或未请求的配置项。

## 4. 最小实现路径
- 先盘点文档契约和生成边界，建立统一的读者路径、术语和验证命令。
- 直接重写维护文档与 skill 指令，使用清晰标题、问题链、最小例子、显式限制和可复制命令，不引入新文档框架。
- 修改生成器的参考页头部模板并重建参考页，确认只发生预期结构变化和可追溯来源变化。
- 用链接扫描、skill validator、项目校验、单元测试、Python 编译和 release builder 验收；不以静态阅读代替运行验证。
- 暂不引入：多语言站点、自动文档站、全文语义索引、额外 lint 依赖或新的文档格式。

## 5. 技术决策
- 技术栈：Markdown、Python 生成/校验脚本、现有 unittest 和发布构建流程。
- 本轮允许改动：项目维护的 Markdown、参考页生成器模板、任务包验收记录，以及由这些变更产生的确定性生成参考页。
- 本轮不应触碰：法律文本、原始抓取数据、评测输入、安装运行时逻辑和未由文档任务要求的代码。
- 路由：explore 结论无额外 lane；主线程统一执行、验证和验收，避免跨文件写入冲突。
- Git integration branch：`spec/2026-10-03_distill-project-docs`；本地模式：upstream fetch 传输失败，已从本地主分支创建；网络恢复后由 push 再同步远端

## 6. 成功标准与验证方式
- 每个范围内文档都有明确目的、目标读者、下一步、边界和可核对命令 -> verify: `rg` 结构审计 + Markdown 链接扫描 + 人工抽样阅读。
- skill 指令仍能正确触发并保持证据保护规则 -> verify: skill-creator quick validator、`tools/validate_skill_package.py`、现有单元测试。
- 生成参考页仍与来源覆盖和生成器契约一致 -> verify: `python3 tools/build_phrasebank_refs.py`（或在无网络时运行离线包校验）并检查 `git diff` 仅含预期模板变化。
- 发布包内容和安装路径未回归 -> verify: `python3 tools/build_release.py`。

## 7. 风险与约束
- 风险：改写生成参考页会与下一次 rebuild 漂移 -> 只改生成器模板，保留上游短语和来源，并运行生成/校验。
- 风险：为了“可读”误删模型必须执行的限制 -> 先保留行为契约，再重排解释；用 validator、测试和关键词审计回归。
- 风险：现有未提交文档被误判为无关改动 -> 已在分支创建前显式保存并恢复，任务范围明确纳入这些文件。
