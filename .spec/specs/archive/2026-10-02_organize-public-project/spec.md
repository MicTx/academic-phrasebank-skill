# Organize open-source project structure and documentation - 项目范围

## 1. 问题定义

- **项目目标**：按标准开源项目结构核对本仓库，修正文档路径和职责说明，并对目录保留/迁移做有证据的判断。
- **目标用户**：开源用户、贡献者和本项目维护者。
- **核心价值**：仓库入口、开发说明、生成数据和用户技能之间的边界清楚，文档链接不再产生歧义。

## 2. 假设与待确认

### 2.1 已确认事实

- 结构审计显示 `academic-phrasebank-skill`、`data`、`tests`、`tools` 各有 live 引用或明确生成/验证职责。
- `.spec/` 是历史治理记录，不是运行时目录；`data/raw` 是 builder 的审计输入；`Agent.md` 是内部维护说明。
- 审计发现的实际文档问题是相对路径表述不完整，未发现需要移动或删除的 live 目录。

### 2.2 关键假设

- 保留现有目录结构，优先修正文档和 release 边界；目录迁移需要独立证据和独立任务。
- `.DS_Store` 属于本地忽略文件，不进入 Git 或用户 release，本轮不把它纳入项目迁移。

### 2.3 待确认问题

- 无。

### 2.4 可选解释与取舍

- `data/raw` 和 `data/processed` 即使被结构脚本标为部分 unreferenced，也保留，因为 builder、manifest 和审计流程使用它们。
- `.spec/` 保留在仓库中作为历史治理记录，不为“无 live reference”而归档或删除。

## 3. 功能范围

### 3.1 核心功能（MVP）

- [x] 修正 `Agent.md` 和 `CONTRIBUTING.md` 的路径指向。
- [x] 复核用户 release、开发文档、技能目录和生成数据的职责边界。
- [x] 运行结构审计 `--check`、项目 validators、tests 和 release 白名单检查。

### 3.2 扩展功能

- 无。

### 3.3 不在范围内

- 不移动或删除 `data`、`tests`、`tools`、`.spec` 或 skill references。
- 不改变运行时 skill 行为、remote 配置和 GitHub 仓库。
- 不把内部 `Agent.md` 或开发工具放入用户 release。

## 4. 最小实现路径

- 根据结构审计事实决定目录全部保留。
- 只修正已确认的文档路径歧义。
- 运行结构检查、现有测试和用户 release 构建验证，不引入新架构或目录层级。

## 5. 技术决策

- 技术栈：Markdown、Python 标准库、Git；适用外：无。
- 本轮允许改动：`Agent.md`、`CONTRIBUTING.md`、本 spec 记录和必要验收证据。
- 本轮不应触碰：运行时代码、参考语料、生成数据、remote、用户包内容规则。
- Git integration branch：`spec/2026-10-02_organize-public-project`

### 5.4 编排策略

- route: local
- 结构事实已经由主会话取得，改动范围窄，直接在主会话完成。

## 6. 成功标准与验证方式

- `Agent.md` 和 `CONTRIBUTING.md` 中的路径均能从仓库根目录解析。
- `organize_project_structure.py --check` 通过；保留目录的理由写入本记录。
- quick validator、项目 validator、6 个单测、`git diff --check` 和用户 release 构建通过。

## 7. 风险与约束

- 过度清理会破坏 builder 输入或历史记录；本轮所有无 live reference 候选都采用 keep-and-document。
- 用户 release 与开发仓库职责不同；只修文档表述，不把内部材料公开打包。
