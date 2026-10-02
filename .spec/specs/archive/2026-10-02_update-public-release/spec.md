# Prepare public release documentation and user package - 项目范围

## 1. 问题定义

- **项目目标**：把 `academic-phrasebank-assistant` 整理成可公开使用的技能与用户 release，并保留可复现的开发验证链。
- **目标用户**：使用 Codex 或 Claude Code 进行英文科研论文编辑的用户，以及维护该技能的开源贡献者。
- **核心价值**：用户拿到只包含安装所需内容的稳定包；贡献者能通过文档、测试和校验器复现构建结果。

## 2. 假设与待确认

### 2.1 已确认事实

- 当前项目远程 `origin` 指向私有 Git 服务 `git.mxk.dev`；GitHub remote 尚未配置。
- 当前 skill 名称与安装路径必须保持 `academic-phrasebank-assistant`。
- Phrasebank 参考文件来自 University of Manchester 的公开 Academic Phrasebank 页面；来源 URL 已记录在 source coverage 文档中。
- 现有技能重构、语料重建、测试和 release 改动属于同一套公开发布准备工作。

### 2.2 关键假设

- 原创代码和项目原创文档采用 Apache-2.0；上游 Phrasebank 派生内容保持单独归因，不被默认为项目重新授权。
- 用户 release 只需要安装器、技能目录、用户 README、许可证、NOTICE 和 CHANGELOG。
- `Agent.md`、`DEVELOPMENT.md`、tests、evals、raw source、manifest 和 build tools 供维护者自用，不进入用户包。

### 2.3 待确认问题

- 无。

### 2.4 可选解释与取舍

- 当前选择：一个 Development Record 覆盖本次所有改动；这些改动共同服务于公开发布，拆分会破坏构建与文档验收链。
- 当前选择：release 采用 commit 派生标识，不引入未经确认的语义版本号。
- GitHub remote 的准确 URL 尚未提供；本轮只推送已配置的 `origin`，不猜测 GitHub 地址。

## 3. 功能范围

### 3.1 核心功能（MVP）

- [x] 规范 skill 主体、触发描述、边界、反模式和最终质量门。
- [x] 修复 Phrasebank 提取伪残留并以 staging/rollback 方式重建参考文件。
- [x] 补齐开源项目公开文档和上游来源声明。
- [x] 生成只含用户运行所需内容的 `.tar.gz` 与 `.zip` release，并验证归档、权限、checksum 和安装流程。

### 3.2 扩展功能

- 无。本轮不配置 GitHub remote，不发布 GitHub Release，不引入自动 CI/CD。

### 3.3 不在范围内

- 不改变 skill 内部名称或安装目标。
- 不把开发评测、Agent 笔记、原始抓取数据或构建工具塞进用户包。
- 不声称上游 Phrasebank 派生内容自动适用 Apache-2.0。

## 4. 最小实现路径

- 重构 `SKILL.md` 和 UI metadata；保留详细 revision framework 作为唯一流程参考。
- 修复 builder/validator，重建 references，并用 fixture/unit tests 锁住 inline tag、hidden break 和 rollback 语义。
- 增加 LICENSE、NOTICE、CHANGELOG、CONTRIBUTING、CODE_OF_CONDUCT、SECURITY、DEVELOPMENT，并把 README 收敛为用户文档。
- 让 release builder 显式复制公开文件和 skill 目录，排除开发目录，再执行 validator、安装 smoke、归档检查和重复构建校验。

## 5. 技术决策

- 技术栈：Python 标准库、POSIX shell、Git；适用外：无运行时依赖变更。
- 本轮允许改动：skill、references、raw/manifest 生成物、安装器、校验器、release builder、公开/内部文档、tests 和 `.spec` 记录。
- 本轮不应触碰：用户主目录下已安装技能、远程仓库配置、无关分支和外部账号。
- Git integration branch：`spec/2026-10-02_update-public-release`

### 5.4 编排策略

- route: explore
- 本轮改动已在主会话完成，保持单线程验收，不再派发新的 sidecar lane。
- 原因：当前任务的代码、归档内容和 Git push 互相耦合，最终边界与验收必须由主会话统一裁决。

## 6. 成功标准与验证方式

- skill 与项目文档校验通过：quick validator、项目 validator、`git diff --check`。
- builder 回归通过：`python3 -m unittest discover -s tests -v`、live rebuild、生成物无 `B e ing`/裸 `break`。
- 用户包只包含公开文件和 skill；不包含 Agent、DEVELOPMENT、tests、evals、data、tools。
- release tar/zip 可解包，`install.sh` 保留 0755，checksum 通过，连续两次构建归档哈希一致。
- 当前所有改动在本包范围内，完成后 archive + commit，再执行 spec push。

## 7. 风险与约束

- 上游 Phrasebank 的知识产权与项目原创文件不同：通过 NOTICE、source coverage 和 README 分开声明。
- 当前工作树来自 retro-pack；必须先在本分支完成 package gate，禁止把 dirty tree 直接推送。
- GitHub remote 缺少准确地址；本轮只操作 `origin`。
