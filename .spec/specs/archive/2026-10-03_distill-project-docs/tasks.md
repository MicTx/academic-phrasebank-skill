# Rewrite project documentation for human and LLM readability - 任务拆解

## 使用规则
- 每个任务都要写清楚 `boundary` 和 `verify`
- 如果一个任务没有验证方式，就不能开始
- 发现的可执行问题必须回写本包，并在本轮做完
- 新任务包使用 `YYYY-MM-DD_<verb>-<object>`，详见 `references/naming-and-commits.md`

## 阶段一：澄清与初始化
- [x] 固化问题定义、关键假设与非目标
  - id: task-scope-locked
  - boundary: 只更新 `.spec/specs/2026-10-03_distill-project-docs/spec.md`
  - verify: 已检查 `spec.md`，其中包含事实、假设、待确认问题、不在范围内内容、最小路径和 integration branch。
- [x] 从主分支创建独立工作分支
  - id: task-branch-created
  - boundary: 只执行 Git 分支检查/创建，不改业务文件；恢复任务开始前已存在的未提交文件属于本任务范围。
  - verify: `git branch --show-current` 输出 `spec/2026-10-03_distill-project-docs`，且 `git log --oneline main..HEAD` 无额外提交。

## 阶段二：核心实现
- [x] 盘点并锁定文档契约
  - id: task-inventory-docs
  - depends-on: task-scope-locked, task-branch-created
  - boundary: 只读取文档、脚本、发布规则和当前 diff；更新任务包中的范围/清单，不改项目文档正文。
  - verify: `rg --files` 清单与 spec 范围逐项对照，生成/手工维护/法律/机器数据边界记录完整。
- [x] 重写项目入口与治理文档
  - id: task-rewrite-project-docs
  - depends-on: task-inventory-docs
  - boundary: 只改 `README.md`、`CONTRIBUTING.md`、`DEVELOPMENT.md`、`SECURITY.md`、`SUPPORT.md`、`CODE_OF_CONDUCT.md`、`NOTICE.md`、`CHANGELOG.md`、`Agent.md`、`.github/pull_request_template.md` 及已有公开指南。
  - verify: Markdown 文档抽样检查目的、读者、下一步、边界和命令；`git diff --check` 通过。
- [x] 重写 skill 指令与手工参考文档
  - id: task-rewrite-skill-docs
  - depends-on: task-rewrite-project-docs
  - boundary: 只改 `academic-phrasebank-skill/SKILL.md`、`references/index.md`、`references/revision-framework.md`、`references/source-coverage.md`；保留 frontmatter、名称、触发范围和证据保护契约。
  - verify: skill-creator quick validator、`python3 tools/validate_skill_package.py` 和关键词/路径审计通过。
- [x] 统一生成参考页入口并重建
  - id: task-regenerate-reference-docs
  - depends-on: task-rewrite-skill-docs
  - boundary: 只改 `tools/build_phrasebank_refs.py` 的文档模板及其生成的 `academic-phrasebank-skill/references/*.md`；不得人工改写上游句型正文或来源 URL。
  - verify: 运行生成器或等价离线校验；检查生成页数、来源覆盖、句型占位符和 diff 边界。

## 阶段三：集成与验收
- [x] 打通文档到安装、验证和发布的关键路径
  - id: task-verify-doc-path
  - depends-on: task-regenerate-reference-docs
  - boundary: 只补文档链接、命令和生成结果所需的粘合改动，不改运行时功能。
  - verify: 链接扫描、skill validator、单元测试、Python 编译和 release builder 均通过。
- [x] 最小化复核点：确认未引入未请求扩展或越界改写
  - id: task-review-boundary
  - depends-on: task-verify-doc-path
  - boundary: 只审查当前任务包相关 diff 与范围外文件。
  - verify: `git diff --name-only main...HEAD` 与 spec 范围逐项匹配；生成文件、LICENSE、raw 数据和配置未越界。
- [x] 完成验收检查并补齐文档
  - id: task-close-package
  - depends-on: task-review-boundary
  - boundary: 只更新任务包文档、检查项、验收证据，以及本项目 `.spec/docs/` 中的工程事实沉淀。
  - verify: `check_spec_package.py` exit 0，`checklist.md` 全部可判定并记录真实命令证据。

---

**当前进度**：由脚本计算，无需手动维护
