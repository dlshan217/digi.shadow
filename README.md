# Digital Shadow

An offline desktop application for personal reflection through pattern analysis.

Digital Shadow observes what you write over time and reflects recurring themes,
tone, and habits. It does not chat, give advice, or simulate intelligence.

---

## Features

- Offline desktop GUI (Windows)
- Local data storage (JSON)
- Pattern-based insight generation
- Tone detection (positive / heavy / neutral)
- Stop-word filtering for clean insights
- Repetition detection
- Weekly summaries
- No external APIs
- No internet required

---

## How It Works

1. **Input**
   - User writes free-form text.
   - Entries are saved locally.

2. **Storage**
   - Data is stored in `data.json` with timestamps and day information.
   - File is created automatically if missing.

3. **Analysis**
   - Text is tokenized into words.
   - Grammar fillers and joiners are removed.
   - Meaningful words are counted.
   - Positive vs negative word balance determines tone.
   - Repetition and time patterns are detected.

4. **Output**
   - Frequent themes
   - Overall tone
   - Repeated thoughts
   - Weekly summaries

The system performs deterministic analysis only.
No AI models or external services are used.

---

## Tone Detection Logic

Tone is calculated using simple word frequency comparison:

- More positive words → `positive`
- More negative words → `heavy`
- Otherwise → `neutral`

This is intentionally transparent and explainable.

---

## GUI Controls

- **Enter** → Save entry
- **Shift + Enter** → New line
- **Insight** → Current reflection
- **Weekly Summary** → Recent trends
- Closing the window exits the app

---

## Tech Stack

- Python 3
- Tkinter (GUI)
- JSON (storage)
- PyInstaller (packaging)

---
