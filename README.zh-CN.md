# Coreader 插件

这是 Coreader 面向 Codex 和 Claude Code 的官方插件仓库。

Coreader 通过 `https://mcp.coreader.dev/mcp` 提供基于 OAuth 的远程 MCP 服务，让 AI 安全访问你的个人阅读记忆。你不需要创建、复制或粘贴长期 API Token。

[English](./README.md) · [安装中心](https://www.coreader.dev/zh/install) · [隐私政策](https://www.coreader.dev/privacy) · [服务条款](https://www.coreader.dev/terms)

## 安装到 Codex

```bash
codex plugin marketplace add vzheng56/coreader-plugins
codex plugin add coreader@coreader
```

安装后新建一个 Codex 任务，按提示在浏览器完成授权，然后输入：

```text
@coreader 我最近读了什么书？
```

更新：

```bash
codex plugin marketplace upgrade coreader
codex plugin add coreader@coreader
```

## 安装到 Claude Code

```bash
claude plugin marketplace add vzheng56/coreader-plugins
claude plugin install coreader@coreader
```

按提示在浏览器完成授权，然后输入：

```text
使用 Coreader 查看我最近读过的书。
```

更新：

```bash
claude plugin marketplace update coreader
claude plugin install coreader@coreader
```

## 安全性

- 授权使用 OAuth Authorization Code + PKCE。
- 插件中不包含客户端密钥、用户 Token 或阅读数据。
- 服务只会获得 Coreader 授权页明确展示的权限。
- 可以随时在 [Coreader 连接管理](https://www.coreader.dev/dashboard/integrations) 中撤销连接。
