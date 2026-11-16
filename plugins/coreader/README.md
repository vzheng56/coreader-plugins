# Coreader

Coreader lets Codex and Claude Code search your personal reading memory and create writing drafts with traceable references.

The plugin is a thin distribution layer. OAuth, permissions, reading data, and MCP business logic remain on Coreader's remote service.

Available tools:

| Tool | What it returns |
| --- | --- |
| `get_overview` | Totals, recent books, shelves, projects |
| `list_books`, `get_book` | Books with publication details, table of contents, endorsements and statistics |
| `search_memory` | Notes and recordings matched by words and by meaning (Chinese and English) |
| `list_notes` | Quotes, reflections, summaries and questions, filtered by book, chapter, page, tag or time |
| `list_captures`, `get_capture` | Voice recordings, photos and typed entries with transcripts and the notes made from them |
| `get_items` | Any item by its `ref` |
| `get_reading_activity`, `list_todos` | Reading time, days, streaks; to-dos said while reading |
| `list_documents`, `get_document` | Writing drafts, research reports, task deliveries, reading Q&A |
| `list_projects`, `get_project` | Groups of books studied together |
| `create_writing_document`, `attach_writing_references` | Save a draft and link its sources, only on request |

Permissions are granted per category on the Coreader consent screen. After updating from 0.1.0, remove the Coreader connection and add it again to grant reading activity, projects and audio.

Never paste a Coreader token into an AI chat. Use the browser OAuth flow started by the client.
