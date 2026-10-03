# Add bilingual English and Simplified Chinese README support - 项目范围

## 1. 问题定义
- **项目目标**：为仓库提供结构对齐的英文和简体中文 README，并让两个语言入口在源码仓库和发布归档中都可用。
- **目标用户**：使用 Codex 或 Claude Code 安装此 skill 的英文科研写作者、中文科研写作者、维护者和发布包使用者。
- **核心价值**：读者可以按语言快速理解用途、安装方式、证据边界和参考入口，同时不会因发布归档裁剪文件而遇到断链。

## 2. 假设与待确认

### 2.1 已确认事实
- 当前仓库只有根目录 `README.md`，其内容会被 `tools/build_release.py` 复制到用户归档。
- 安装命令、skill 名称、上游 Phrasebank 归属和引用路径属于现有契约。
- 当前默认主入口保持英文，简体中文使用独立的 `README.zh-CN.md`，两者顶部互链。

### 2.2 关键假设
- “支持中英文 README”表示双文件语言入口，而不是在单文件内重复整篇内容。
- 中文 README 与英文 README 需要保持同一信息架构、安装契约、保护边界和参考入口。
- 发布归档应同时包含两个 README，否则语言切换会在归档中失效。

### 2.3 待确认问题
- 无：用户未指定术语表或中文翻译风格，本轮采用简体中文、直接、面向使用者的说明。

### 2.4 可选解释与取舍
- 当前选择：`README.md` 作为英文主入口，新增 `README.zh-CN.md`，顶部互链 -> 遵循开源仓库惯例，保持默认英文入口并避免单文件重复维护。
- 当前选择：只同步 README、发布清单、离线校验和必要回归测试 -> 不扩展到完整中文化的治理文档或 skill 参考页。

## 3. 功能范围

### 3.1 核心功能（MVP）
- [x] 提供英文与简体中文 README，包含一致的用途、快速开始、安装、参考来源、帮助和许可证入口。
- [x] 在两个 README 顶部提供互链，并保持安装命令、skill 名称、证据边界和相对链接一致。
- [x] 将中文 README 纳入发布归档、归档完整性检查和项目离线校验。
- [x] 增加 README 双语入口与发布边界的回归验证。

### 3.2 扩展功能
- 无

### 3.3 不在范围内
- 不翻译 `SKILL.md`、教程、参考页、治理文档或上游 Phrasebank 句型。
- 不增加文档站、语言选择器脚本、自动翻译流程、包管理器元数据或运行时配置。
- 不修改安装路径、skill frontmatter、上游来源数据或许可证正文。

## 4. 最小实现路径
- 新增 `README.zh-CN.md`，按现有英文 README 的信息架构提供简体中文版本，并在两个文件顶部互链。
- 把 `README.zh-CN.md` 加入 `tools/build_release.py` 的公开文件和归档必需文件集合。
- 在 `tools/validate_skill_package.py` 与项目测试中锁定双语文件、互链、关键入口和发布边界。
- 不引入 i18n 抽象、构建时翻译或第三方文档系统，因为本轮只有两个静态 README 入口。

## 5. 技术决策
- 技术栈：Markdown、现有 Python 发布/校验脚本和 unittest。
- 本轮允许改动：`README.md`、新增 `README.zh-CN.md`、`CHANGELOG.md`（如需记录公开变化）、发布构建/校验脚本、README 回归测试、本任务包文档。
- 本轮不应触碰：`LICENSE`、`install.sh`、`academic-phrasebank-skill/` 内容、上游数据、现有安装契约和其他治理文档正文。
- Git integration branch：`spec/2026-10-03_add-bilingual-readme`

### 5.4 编排策略
- route: explore
- 路由脚本给出 `explore`，但本任务只有一个共享文档/发布边界切片；由主线程顺序执行设计、实现、验证和验收，不启动旁路代理，避免共享 README 与发布脚本的并行冲突。

## 6. 成功标准与验证方式
- 两个 README 顶部互链，且关键章节、安装命令、skill 名称和参考入口语义一致 -> `python3 tools/validate_skill_package.py` 与专门 unittest 通过。
- 发布归档同时包含两个 README，归档中的双语 README 相对链接可达 -> `python3 tools/build_release.py` 后检查最新归档目录和链接。
- 现有 skill、安装和发布行为无回归 -> quick validator、完整 unittest、Python 编译和 release build 通过。
- 变更只落在任务边界内 -> `git diff --check`、spec package checker 和最终路径审计通过。

## 7. 风险与约束
- 风险点：只修改源码 README 会使发布归档缺少中文入口 -> 将中文文件加入 `PUBLIC_ROOT_FILES` 和 `verify_archive` 必需集合，并用发布构建实测。
- 风险点：两种语言内容漂移 -> 两份 README 使用相同章节顺序和关键契约断言，校验器锁定互链和关键入口。
- 约束：发布归档继续排除 `CONTRIBUTING.md`、`DEVELOPMENT.md` 等开发文档，README 不得在归档中建立指向这些排除文件的链接。
