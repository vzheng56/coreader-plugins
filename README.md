# Coreader Plugins

Official Coreader plugins for Codex and Claude Code.

Coreader connects your AI client to your personal reading memory through the remote, OAuth-backed MCP service at `https://mcp.coreader.dev/mcp`. You never need to create or paste a long-lived API token.

[中文说明](./README.zh-CN.md) · [Install guide](https://www.coreader.dev/en/install) · [Privacy](https://www.coreader.dev/privacy) · [Terms](https://www.coreader.dev/terms)

## Install for Codex

```bash
codex plugin marketplace add vzheng56/coreader-plugins
codex plugin add coreader@coreader
```

Start a new Codex task, finish the browser authorization when prompted, and try:

```text
@coreader What have I read recently?
```

Update:

```bash
codex plugin marketplace upgrade coreader
codex plugin add coreader@coreader
```

## Install for Claude Code

```bash
claude plugin marketplace add https://github.com/vzheng56/coreader-plugins.git
claude plugin install coreader@coreader
```

Finish the browser authorization when prompted, then try:

```text
Use Coreader to show me what I have read recently.
```

Update:

```bash
claude plugin marketplace update coreader
claude plugin install coreader@coreader
```

## Security

- Authentication uses OAuth Authorization Code with PKCE.
- The plugin contains no client secret, user token, or reading data.
- The remote service only receives the scopes shown on the Coreader consent screen.
- Connections can be revoked at any time from [Coreader connections](https://www.coreader.dev/dashboard/integrations).

See [SECURITY.md](./SECURITY.md) for vulnerability reporting.
