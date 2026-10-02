# Rename skill and package to academic-phrasebank-skill - 项目范围

## 1. 问题定义

- **项目目标**：统一本地项目、技能内部名称、安装目录、release 名称和用户调用名为 `academic-phrasebank-skill`。
- **目标用户**：使用该 Codex/Claude 技能的用户和维护开源版本的贡献者。
- **核心价值**：用户只需要记住一个稳定名称；旧安装目录仍能被安全清理。

## 2. 假设与待确认

### 2.1 已确认事实

- 当前私有开发 remote 仍为 `origin`，地址是 git.mxk.dev 上的旧仓库路径。
- GitHub 账号已授权，但 GitHub 上尚未创建开源仓库。
- 历史 `.spec/specs/archive/` 记录保留原名称，不回写历史事实。

### 2.2 关键假设

- 新内部 skill name、目录名、安装目标和 release 前缀统一为 `academic-phrasebank-skill`。
- `academic-phrasebank-assistant` 和 `sci-academic-writing` 只作为安装清理兼容名，不再作为运行时名称。
- GitHub remote 和仓库创建留待用户提供准确仓库地址或明确创建动作后处理。

### 2.3 待确认问题

- 无。

### 2.4 可选解释与取舍

- 当前选择：保留旧名兼容清理，避免用户机器留下旧安装目录；不保留旧名作为 `$skill` 调用别名，减少名称漂移。
- 当前选择：不猜测私有仓库或 GitHub 仓库的 URL，不在本轮创建 GitHub 仓库。

## 3. 功能范围

### 3.1 核心功能（MVP）

- [x] 重命名技能目录、frontmatter、metadata、脚本常量、文档和 release 输出。
- [x] 安装新目录并清理两个旧目录。
- [x] 用新名称运行 quick validator、项目 validator、测试和 release 构建。

### 3.2 扩展功能

- 无。

### 3.3 不在范围内

- 不创建 GitHub 仓库，不添加未经确认的 GitHub remote。
- 不修改历史 spec 归档中的旧名称。
- 不改变技能内容、参考语料逻辑或用户功能。

## 4. 最小实现路径

- 使用目录 rename 和全量当前文档/代码引用更新。
- 在 installer 中保留两个旧名的清理路径。
- 运行全量 validators、6 个单测、安装兼容 smoke 和用户 release archive 检查。

## 5. 技术决策

- 技术栈：Git、Python 标准库、POSIX shell；适用外：无依赖升级。
- 本轮允许改动：技能目录、安装器、构建器、校验器、开发/用户文档、测试和 release 产物。
- 本轮不应触碰：历史 `.spec` archive、远程 URL、GitHub 账户和无关分支。
- Git integration branch：`spec/2026-10-02_rename-skill-package`

### 5.4 编排策略

- route: local
- 当前改动边界清晰，主会话直接执行和验收，不派发 sidecar。

## 6. 成功标准与验证方式

- 当前代码中除历史 archive 外不再使用旧运行时名称：`rg` 检查。
- 新 skill 路径通过 quick validator、项目 validator、6 个单测和 py_compile。
- installer 生成 `academic-phrasebank-skill` 并清理两个旧目录。
- release 产物使用 `academic-phrasebank-skill-<commit>` 前缀且用户归档不含旧名。

## 7. 风险与约束

- 旧名引用过早删除会留下旧安装目录；通过 installer legacy cleanup 覆盖。
- 私有 remote 的仓库路径仍可能是旧名；本轮不擅自改远程服务端仓库名。
