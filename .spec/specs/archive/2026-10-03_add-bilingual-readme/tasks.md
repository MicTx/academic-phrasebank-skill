# Add bilingual English and Simplified Chinese README support - 任务拆解

## 使用规则
- 每个任务都要写清楚 `boundary` 和 `verify`
- 如果一个任务没有验证方式，就不能开始
- 发现的可执行问题必须回写本包，并在本轮做完
- 新任务包使用 `YYYY-MM-DD_<verb>-<object>`，详见 `references/naming-and-commits.md`

## 阶段一：范围与契约
- [x] 固化双语 README 的范围、发布边界和非目标
  - id: task-scope
  - boundary: 只更新 `.spec/specs/2026-10-03_add-bilingual-readme/spec.md`
  - verify: `spec.md` 写明双文件策略、发布边界、非目标、integration branch 和 5.4 编排策略
- [x] 固化任务顺序和逐项验证方式
  - id: task-plan
  - depends-on: task-scope
  - boundary: 只更新本任务包的 `tasks.md`
  - verify: 每个任务都有唯一 id、明确 boundary/verify，依赖顺序可由 spec checker 解析

## 阶段二：双语内容与发布契约
- [x] 增加结构对齐的英文/简体中文 README 入口
  - id: task-readmes
  - depends-on: task-plan
  - boundary: 只修改根目录 `README.md` 并新增 `README.zh-CN.md`；不改其他项目文档正文
  - verify: 两个 README 顶部互链，章节顺序、安装命令、skill 名称、证据边界和相对入口一致；运行 README 静态回归测试
- [x] 让发布归档包含双语 README
  - id: task-release-contract
  - depends-on: task-readmes
  - boundary: 只修改 `tools/build_release.py` 与 `tools/validate_skill_package.py` 中 README 文件清单/校验，不改变其他发布边界
  - verify: `python3 tools/validate_skill_package.py` 通过；`python3 tools/build_release.py` 生成的最新归档目录同时含 `README.md` 与 `README.zh-CN.md`
- [x] 增加双语 README 与发布边界回归测试
  - id: task-tests
  - depends-on: task-release-contract
  - boundary: 只新增或修改 README/发布契约相关测试，不重写现有 Phrasebank 提取测试
  - verify: `python3 -m unittest discover -s tests -v` 通过，且测试覆盖互链和双 README 发布存在性

## 阶段三：验收与交付
- [x] 运行完整验证并审计双语链接
  - id: task-verify
  - depends-on: task-tests
  - boundary: 只更新任务包 checklist/evidence，不再扩展产品范围
  - verify: quick validator、项目 validator、unittest、py_compile、release build、Markdown 相对链接审计和 spec checker 全部通过
- [x] 完成最小化复核并记录被拒绝扩展
  - id: task-scope-review
  - depends-on: task-verify
  - boundary: 只审查本任务相关 diff 和任务包记录
  - verify: 验收记录明确没有引入 i18n、自动翻译、文档站或无关文档翻译
- [x] 完成验收检查并补齐文档
  - id: task-acceptance
  - depends-on: task-scope-review
  - boundary: 只更新本任务包的 `checklist.md` 与证据字段
  - verify: `checklist.md` 所有检查项有真实证据并达到 `**验收结果**：通过`

---

**当前进度**：由脚本计算，无需手动维护
