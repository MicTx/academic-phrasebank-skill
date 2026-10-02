# Add mature open source documentation and GitHub templates - 项目范围

## 1. 问题定义

- **项目目标**：为公开仓库补齐面向读者、贡献者和维护者的长期有效文档与 GitHub 协作模板。
- **目标用户**：技能使用者、开源贡献者、问题报告者和安全报告者。
- **核心价值**：用户能快速安装和理解项目，贡献者知道如何提交高质量变更，维护者能稳定处理问题和安全报告。

## 2. 假设与待确认

### 2.1 已确认事实

- GitHub 公开仓库为 `MicTx/academic-phrasebank-skill`。
- 项目已有 README、许可证、来源声明、贡献、安全和开发文档，但缺少统一的 GitHub Issue/PR 入口和成熟的读者叙事。
- 项目名称已统一为 `academic-phrasebank-skill`。

### 2.2 关键假设

- 本轮文档使用英语，面向公开 GitHub 读者和贡献者。
- README 不叙述内部会话、当前工作树或验收过程；开发细节只保留为稳定的命令参考。

### 2.3 待确认问题

- 无。

### 2.4 可选解释与取舍

- 使用 Keep a Changelog 格式和一个初始公开版本条目。
- 增加 GitHub issue forms、PR 模板和支持入口，不引入 CI、机器人或额外服务配置。

## 3. 功能范围

### 3.1 核心功能（MVP）

- [x] 面向读者重写 README：用途、安装、用法、来源、许可证和仓库导航。
- [x] 面向贡献者完善 CONTRIBUTING、DEVELOPMENT、SUPPORT、SECURITY、CODE_OF_CONDUCT、CHANGELOG。
- [x] 增加 GitHub bug/feature issue forms、配置文件和 pull request 模板。
- [x] validator 检查公开文档与 GitHub 模板存在并包含关键入口。

### 3.2 扩展功能

- 无。本轮不新增 CI/CD、发布机器人或项目治理自动化。

### 3.3 不在范围内

- 不改变 skill runtime、参考语料和安装行为。
- 不引入新的服务账号、邮箱或维护者身份。
- 不在文档中描述内部会话过程状态。

## 4. 最小实现路径

- 重写公开 README 和长期有效的协作文档。
- 添加 GitHub 原生 issue forms 和 PR 模板。
- 扩展离线 validator，运行文档、模板、skill、测试和 release 验收。

## 5. 技术决策

- 技术栈：Markdown、GitHub YAML forms、Python 标准库；适用外：无。
- 本轮允许改动：根目录公开文档、`.github/` 模板、validator、本 spec 和 release 文档。
- 本轮不应触碰：skill reference 内容、builder 数据契约、远程配置和历史 spec archive。
- Git integration branch：`spec/2026-10-02_add-git-documentation`

### 5.4 编排策略

- route: local
- 文档与模板属于同一 ownership slice，主会话直接完成验收。

## 6. 成功标准与验证方式

- README 只描述用户可验证的功能、安装、用法、来源和许可证。
- 贡献、安全、支持、行为准则、开发、变更记录均有稳定入口。
- GitHub templates 可被 GitHub 识别，validator 和项目测试通过。
- 用户 release 继续只包含公开用户材料，不包含内部文档和测试。

## 7. 风险与约束

- 文档不能承诺未配置的服务或联系方式；使用 GitHub 原生入口。
- CHANGELOG 使用公开版本语言，不写工作树或会话状态。
