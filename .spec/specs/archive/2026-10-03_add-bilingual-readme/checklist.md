# Add bilingual English and Simplified Chinese README support - 验收清单

## 假设与范围对齐
- [x] 无阻塞性待确认项；无指定中文术语表不阻塞，采用简体中文和现有英文契约
- [x] 范围内/范围外与实现一致
- [x] 本轮发现的可执行问题已回写任务包并完成，未甩给用户

## 简洁性
- [x] 没有未请求的扩展、抽象或配置化
- [x] 当前方案保持最小可行：两个静态 README、发布清单、离线校验和必要测试

## 变更边界
- [x] 每项改动都能追溯到明确任务
- [x] 没有无关重构或顺手清理

## 功能完整性
- [x] `README.md` 提供英文主入口，`README.zh-CN.md` 提供简体中文入口
- [x] 两个 README 顶部互链，且关键安装/保护/参考入口保持一致
- [x] 发布归档包含两个 README，归档内相对链接可达

## 测试与验证
- [x] 双语 README 静态回归测试通过
- [x] 项目 validator、unittest、编译和 release build 通过

## 文档同步
- [x] README、发布构建、校验器和测试已同步
- [x] `spec.md` / `tasks.md` / `checklist.md` 已同步

## 部署验证（如适用）
- [x] 本地运行适用外：本轮没有运行时服务，已用 release build 和安装 smoke 验证用户归档
- [x] 构建成功：`python3 tools/build_release.py` 通过，包含 archive integrity 和 install smoke

## 边界回归
- [x] 越界负样本：只检查任务允许路径，未混入其他 skill/上游数据改动
- [x] 顺序交换负样本：文档静态构建无可交换运行时步骤，N/A：由 spec checker 验证任务依赖而非文件顺序
- [x] 旁路负样本：未运行的 README/release 验证不计为通过，所有任务 verify 均真实执行

## 验收证据
- 裁决性检查：`python3 tools/build_release.py` @ 2026-10-03 13:09 UTC
- 证据锚点：HEAD 5880b7e3e796c5f0ac795fd57a928771067226a9 @ 2026-10-03 13:09:40 UTC
- 外部对标：以 task package 状态机为真，fresh package 不得直接进入实现态
- 脚本验证：`quick_validate.py`、`tools/validate_skill_package.py` 和 `check_spec_package.py` 均 exit 0
- 旧新对比：从单一英文 README 增加 `README.zh-CN.md`、顶部互链和发布归档双文件
- 差异边界：变更仅涉及 README、CHANGELOG、发布/校验脚本、README 回归测试和本任务包
- 行为成效：英文/简体中文读者均可从入口完成安装、参考路由、证据边界和帮助导航
- 构建：`python3 tools/build_release.py` 通过；最新归档同时包含 `README.md` 与 `README.zh-CN.md`
- 测试：`python3 -m unittest discover -s tests -v` -> 9 tests, OK；`py_compile` 通过
- 手工验证：源码和最新归档的 Markdown 相对链接审计均为 `broken_relative_links=0`

---

**验收结果**：通过
