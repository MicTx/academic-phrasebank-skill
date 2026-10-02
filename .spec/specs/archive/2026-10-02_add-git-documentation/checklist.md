# Add mature open source documentation and GitHub templates - 验收清单

## 假设与范围对齐

- [x] 无阻塞性待确认项。
- [x] 范围内/范围外与实现一致：文档与 GitHub 模板，不改运行时行为。
- [x] 本轮发现的可执行问题已回写并完成。

## 简洁性

- [x] 没有未请求的扩展、抽象或服务配置。
- [x] 当前方案保持最小可行：Markdown + GitHub 原生模板。

## 变更边界

- [x] 改动可追溯到四个文档任务。
- [x] 没有无关重构或过程性叙述。

## 功能完整性

- [x] README 面向读者，包含安装、用法、来源、许可证和导航。
- [x] 贡献、安全、支持、行为准则、开发和变更文档完整。
- [x] Issue forms 和 PR 模板覆盖公开协作入口。

## 测试与验证

- [x] validator 检查所有公开文档和 GitHub 模板。
- [x] 7 个单测、quick validator、项目 validator 和 release 构建通过。

## 文档同步

- [x] README、CHANGELOG、CONTRIBUTING、SUPPORT、SECURITY、CODE_OF_CONDUCT、DEVELOPMENT 已同步。
- [x] `.spec/specs/archive/` 记录已同步。

## 部署验证（如适用）

- [x] 用户 release 继续生成并通过归档白名单、checksum 和安装 smoke。
- [x] GitHub templates 作为源码随仓库发布，不进入用户运行包。

## 边界回归

- [x] 越界负样本：没有修改 skill runtime、builder 数据契约或历史 archive。
- [x] 顺序交换负样本：文档顺序不影响安装、validator 和 release。
- [x] 旁路负样本：validator 直接检查缺失文档和模板，不依赖人工判断。

## 验收证据

- 裁决性检查：`python3 tools/validate_skill_package.py` @ 2026-10-02。
- 证据锚点：HEAD `49fa42d` @ 2026-10-02T21:40:00+08:00
- 脚本验证：quick validator、项目 validator、py_compile、git diff check 通过。
- 差异边界：只增加公开 Git 文档与模板，用户 release 内容规则保持不变。
- 行为成效：读者拥有清晰 README、贡献入口、支持入口和安全报告入口。
- 构建：公开 release archive、manifest、checksum 和白名单通过。
- 测试：`python3 -m unittest discover -s tests -v`，7 个测试通过。
- 手工验证：README、GitHub issue forms 和 PR template 路径存在且内容可读。

---

**验收结果**：通过
