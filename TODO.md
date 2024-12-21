# Transcription and Content Management Plan

## 1. Create Transcripts for Each Resource

### Web Articles
- Use [Jina AI](https://r.jina.ai/) to extract and transcribe web articles
  - Example: https://r.jina.ai/https://www.mattprd.com/p/the-complete-beginners-guide-to-autonomous-agents

### YouTube Videos
- Use yt-dlp to download and extract transcripts:

1. Save transcripts in markdown format:
   ```bash
   yt-dlp --write-auto-sub --sub-format srt --convert-subs srt [video_url]
   ```
2. Convert SRT to markdown using a script
3. Commit and push transcripts to GitHub repository
   - Organize in folders by content type
   - Include metadata (title, author, date)
   - Add table of contents

## Send Markdown Files to Kindle
- Convert markdown files to .mobi format using Calibre or Pandoc
- Email converted files to Kindle email address
- Ensure "Send to Kindle" settings allow receiving documents

## Add Resources to NotebookLM
- Use NotebookLM API to programmatically add new resources