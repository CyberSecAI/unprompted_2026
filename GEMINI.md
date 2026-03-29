# [un]prompted 2026 - Key Insights Project

This project captures and organizes knowledge from the **[un]prompted 2026** conference. It automates transcript processing and extracts structured "Key Insights" using AI.

## Project Overview

- **Goal**: Create a comprehensive, searchable knowledge base of all talks.
- **Source**: [YouTube Playlist](https://www.youtube.com/playlist?list=PLjmt1tu85IhAiVPugOjP-7Cy0Oemi3m7z)
- **Output**: 
  - `insights/`: Per-talk structured Markdown summaries.
  - `meta/`: Synthesized thematic insights across multiple sessions.
  - `README.md`: Master directory.

## Directory Structure

- `transcripts/`: Raw SRT transcripts from YouTube.
- `insights/`: Individual talk insights (Summary, Takeaway, 6-8 topics).
- `meta/`: Meta-insights synthesizing recurring conference themes.
- `scripts/`: Automation and maintenance scripts.
- `README.md`: Main conference index.

## Key Scripts

- `scripts/generate_index.py`: Regenerates `README.md` from available transcripts and insights.
- `scripts/find_missing.py`: Utility to verify 1:1 mapping between transcripts and insights.

## Usage & Workflows

### 1. Adding New Transcripts
Use `yt-dlp` to download subtitles:
```bash
yt-dlp --write-auto-sub --write-sub --skip-download --sub-format vtt --convert-subs srt -o "%(id)s_%(title)s.%(ext)s" "[PLAYLIST_URL]"
```

### 2. Updating the Index
Run the indexer to refresh `README.md`:
```bash
python3 scripts/generate_index.py
```

## Conventions

- **Insight Format**: Summary (<25 words), Key Takeaway (<15 words), and 6-8 Topic Sections (12-20 words per bullet).
- **Naming**: Files are named using the pattern `{VideoID}_{Talk_Title}.md`.
- **Acronyms**: Verify technical acronyms (LLM, RAG, MCP, etc.) against project context.
