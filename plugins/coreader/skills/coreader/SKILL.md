---
name: coreader
description: Use Coreader MCP tools when the user asks to search their reading memory, inspect book context, compare notes, retrieve reflections, or create a writing draft from Coreader references.
---

# Coreader

Use the configured `coreader` MCP server. Never ask the user to paste a Coreader API token and never store credentials in files, prompts, or shell history.

If authorization is required, let the client start the Coreader OAuth flow and ask the user to complete login and consent in the browser. If an old connection reports `invalid_grant`, guide the user to remove the existing Coreader connection, reinstall or reconnect the plugin, and authorize again.

Prefer read tools before write tools:

- Use `list_recent_books` for recent books and reading activity.
- Use `get_book_context` for the reading context of one book.
- Use `search_book_memory` for search within a book.
- Use `search_global_memory` for search across the user's reading library.
- Use `get_recent_reflections` for recent reflections on a book.
- Use `create_writing_document` only when the user explicitly asks to create a new draft.
- Use `attach_writing_references` only when the user explicitly asks to bind Coreader evidence to a draft.

Preserve source attribution in the answer. Include the returned book title, source type, artifact kind, and other traceability fields when available. Do not claim that Coreader returned information that is absent from the tool result.
