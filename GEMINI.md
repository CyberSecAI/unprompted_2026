# [un]prompted 2026 - Key Insights Project

This project is dedicated to capturing and organizing knowledge from the **[un]prompted 2026** conference. It automates the process of downloading YouTube transcripts, cleaning them, and extracting structured "Key Insights" using AI reasoning models.

## Project Overview

- **Goal**: Create a comprehensive, searchable knowledge base of all talks from the [un]prompted 2026 conference.
- **Source**: [YouTube Playlist](https://www.youtube.com/playlist?list=PLjmt1tu85IhAiVPugOjP-7Cy0Oemi3m7z)
- **Output**: Structured Markdown files in `insights/` containing summaries, key takeaways, and actionable technical insights.

## Directory Structure

- `transcripts/`: Raw and cleaned SRT/text transcripts of the conference talks.
- `insights/`: Generated Markdown files following a specific topic-based format (6-8 topics, 2-3 bullets each).
- `unprompted_2026/`: Working directory containing processing scripts and the master index.
  - `INDEX.md`: Master index of all talks, linked to transcripts and insights.
  - `venv/`: Python virtual environment for processing scripts.
- `notes.md`: Development log, task list, and useful shell commands.

## Key Scripts

- `unprompted_2026/extract_insights.py`: Individual insight extraction script.
- `unprompted_2026/process_batch.py`: Concurrent batch processing script for transcripts.
- `unprompted_2026/create_index.py`: Generates the master `INDEX.md` from available transcripts.

## Usage & Workflows

### 1. Adding New Transcripts
Use `yt-dlp` to download subtitles:
```bash
yt-dlp --write-auto-sub --write-sub --skip-download --sub-format vtt --convert-subs srt -o "%(id)s_%(title)s.%(ext)s" "[PLAYLIST_URL]"
```

### 2. Extracting Insights
The extraction process requires an `ANTHROPIC_API_KEY`. Use the batch script for efficiency:
```bash
export ANTHROPIC_API_KEY="your_key"
unprompted_2026/venv/bin/python unprompted_2026/process_batch.py unprompted_2026/batch_aa
```

### 3. Updating the Index
Always run the indexer after adding new transcripts or generating insights:
```bash
python3 unprompted_2026/create_index.py
```

## Conventions

- **Insight Format**: Summary (<25 words), Key Takeaway (<15 words), and 6-8 Topic Sections (12-20 words per bullet).
- **Naming**: Files are named using the pattern `{VideoID}_{Talk_Title}.md`.
- **Acronyms**: Always verify and correct transcription errors for technical acronyms (e.g., LLM, RAG, Zero-Day).
