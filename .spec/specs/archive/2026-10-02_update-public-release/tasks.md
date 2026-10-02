# Prepare public release documentation and user package - 任务拆解

## 阶段一：技能与语料

- [x] 重构技能主体与触发 metadata
  - id: task-skill-contract
  - boundary: 只改 `academic-phrasebank-assistant/SKILL.md`、`agents/openai.yaml` 和对应 routing 文档；保留内部 skill name 与安装路径
  - verify: `python3 /Users/dawud/.agents/skills/skill-creator/scripts/quick_validate.py academic-phrasebank-assistant` 和 `python3 tools/validate_skill_package.py`

- [x] 修复 Phrasebank builder、validator 和 generated references
  - id: task-corpus-pipeline
  - depends-on: task-skill-contract
  - boundary: 只改 `tools/build_phrasebank_refs.py`、`tools/validate_skill_package.py`、生成的 raw/reference/manifest 文件和 `tests/test_phrasebank_builder.py`
  - verify: `python3 -m unittest discover -s tests -v`、一次 `python3 tools/build_phrasebank_refs.py`、`git diff --check`，并确认没有 `B e ing` 或裸 `- break`

## 阶段二：公开文档与用户包

- [x] 补齐开源公开文档并划分开发材料
  - id: task-public-docs
  - depends-on: task-skill-contract
  - boundary: 只新增/更新 `README.md`、`LICENSE`、`NOTICE.md`、`CHANGELOG.md`、`CONTRIBUTING.md`、`CODE_OF_CONDUCT.md`、`SECURITY.md`、`DEVELOPMENT.md`、`Agent.md` 和 `.gitignore`
  - verify: 项目 validator 通过；README、NOTICE、贡献/安全/开发文档均存在且包含各自入口内容

- [x] 实现用户 release 过滤与归档验收
  - id: task-user-release
  - depends-on: task-corpus-pipeline, task-public-docs
  - boundary: 只改 `tools/build_release.py` 和 release 产物；用户包只允许公开 README/LICENSE/NOTICE/CHANGELOG/install.sh 与 skill 目录
  - verify: `python3 tools/build_release.py`；tar/zip 解包、checksum、skill 文件存在、install.sh 0755、开发目录缺失均通过

## 阶段三：验收与交付

- [x] 完成重复构建、安装和对照评测验收
  - id: task-release-acceptance
  - depends-on: task-user-release
  - boundary: 只写 `.spec` 证据和 dist 产物，不改变产品代码行为
  - verify: 连续两次 release 的 tar/zip/manifest/SHA256SUMS 哈希一致；6 个单测、两个 validator、安装 smoke、失败回滚测试和旧新 skill benchmark 均有证据

- [x] 完成 package check、archive 和 commit 前复核
  - id: task-spec-closeout
  - depends-on: task-release-acceptance
  - boundary: 只更新 `.spec/specs/2026-10-02_update-public-release/` 与 `.spec/docs/`，不新增功能
  - verify: `check_spec_package.py` 通过，`complete_spec_package.py --archive` 成功，生成带 `Spec: 2026-10-02_update-public-release` footer 的 commit

---

**当前进度**：由脚本计算，无需手动维护
