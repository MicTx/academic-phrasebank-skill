# Rewrite project documentation for human and LLM readability - 验收清单

## 假设与范围对齐
- [x] 无阻塞性待确认项；剩余上游 sitemap 是否变化不阻塞本轮，已由生成器和来源边界处理
- [x] 范围内/范围外与实现一致；边界审计命令通过
- [x] 本轮发现的可执行问题已回写任务包并完成，未甩给用户

## 简洁性
- [x] 没有未请求的扩展、抽象或配置化
- [x] 当前方案保持最小可行：只改维护文档、生成器模板、生成参考入口和必要回归测试

## 变更边界
- [x] 每项改动都能追溯到明确任务
- [x] 没有无关重构或顺手清理；`data/raw/` 和 `data/processed/` 无差异

## 功能完整性
- [x] 所有范围内维护文档都已重写或明确记录为保留原因
- [x] skill frontmatter、触发范围、证据保护和安装/发布契约保持不变
- [x] 生成参考页保留上游短语、来源 URL、覆盖统计和占位符边界

## 测试与验证
- [x] skill validator 与项目离线校验通过
- [x] 单元测试、Python 编译和链接/路径审计通过
- [x] 发布构建和安装 smoke test 通过

## 文档同步
- [x] 受影响文档已更新，或记录适用外
- [x] `spec.md` / `tasks.md` / `checklist.md` 已同步

## 部署验证（如适用）
- [x] 本地发布构建和归档内容验证通过
- [x] 运行时部署不适用：本轮只改文档和生成模板，已记录理由

## 边界回归
- [x] 越界负样本：边界审计命令列出 36 个变更路径且无 boundary violation，未混入范围外文件
- [x] 顺序交换负样本：本轮任务依赖由任务包校验器解析；无可交换的运行时步骤，验收不依赖文件顺序（N/A：文档任务）
- [x] 旁路负样本：`check_spec_package.py` 要求每项 task 有 boundary/verify，未运行的验证不会被任务包接受

## 验收证据
- 裁决性检查：`python3 tools/build_release.py` @ 2026-10-03 04:22 UTC
- 证据锚点：HEAD f882e8ebb8904ca3a8c70fb81e34612881b86d29 @ 2026-10-03 04:22:27 UTC
- 外部对标：以 task package 状态机为真，fresh package 不得直接进入实现态
- 脚本验证：`python3 tools/validate_skill_package.py` -> Skill package audit passed；Markdown link check -> broken=0
- 旧新对比：入口文档由“功能清单”改为按读者任务组织；生成参考页只增加统一入口说明
- 差异边界：边界审计命令通过，36 个工作树路径全部属于任务包允许前缀；`data/raw/`、`data/processed/` 无差异
- 行为成效：读者能从 README 进入安装、使用、参考和排障；LLM 能从 skill 入口识别任务层级与禁止事项
- 构建：`python3 tools/build_release.py` -> archive integrity、install smoke、manifest/checksum generation passed
- 测试：`python3 -m unittest discover -s tests -v` -> 7 tests, OK；quick validator -> Skill is valid!
- 手工验证：抽查 README、SKILL、tutorial、reference index、generated reference；入口、路由、边界和来源说明均可见

---

**验收结果**：通过
