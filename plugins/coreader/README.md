# Coreader

Coreader lets Codex and Claude Code search your personal reading memory and create writing drafts with traceable references.

The plugin is a thin distribution layer. OAuth, permissions, reading data, and MCP business logic remain on Coreader's remote service.

Available tools:

- `list_recent_books`
- `get_recent_reflections`
- `search_book_memory`
- `search_global_memory`
- `get_book_context`
- `create_writing_document`
- `attach_writing_references`

Never paste a Coreader token into an AI chat. Use the browser OAuth flow started by the client.
