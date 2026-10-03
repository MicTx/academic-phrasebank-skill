# 双语 README 与发布边界

- `README.md` 是英文主入口，`README.zh-CN.md` 是简体中文入口；两个文件顶部必须互链，并保持安装命令、skill 名称、证据边界和参考入口一致。
- `tools/build_release.py` 的 `PUBLIC_ROOT_FILES` 与 `verify_archive` 必需集合必须同时包含两个 README，否则发布归档中的语言切换会失效。
- 发布归档继续排除 `CONTRIBUTING.md` 和 `DEVELOPMENT.md`；README 对这两份文件只能用源码仓库提示，不能建立归档内会断裂的链接。
- `tools/validate_skill_package.py` 是双语入口契约的离线校验真源，`tests/test_repository_docs.py` 覆盖语言切换和归档复制边界。
