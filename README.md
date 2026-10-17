# 🔍 Vision Analyser

**Drop in a screenshot of code or a document and get an instant, structured AI review.**

## Overview & Problem Statement

Developers and students constantly meet code and documents as *images*:
screenshots in chats, photos of whiteboards, scanned PDFs, slides. Copying that
content out by hand to get help is slow and error-prone.

Vision Analyser takes the image directly, using a multimodal AI model, and returns
a structured review: what the code does, its bugs and risks, and how to improve it,
or a summary, key details, and action items for documents.

## Features

- 🖼️ Image upload (PNG / JPG / WEBP) and/or pasted text
- 🧑‍💻 **Code Analyser** mode: summary, walkthrough, bugs & risks, improvements
- 📄 **Document Analyser** mode: summary, key points, important details, action items
- ❓ Optional focused question ("Is this thread-safe?")
- ⬇️ Download the report as Markdown
- 🔐 API key via environment variable (never hard-coded)
- 🛡️ Input validation, timeouts, and friendly error messages
- 🧩 Clean separation: `analyzer.py` (logic) and `app.py` (UI)

## Quickstart

**Requirements:** Python 3.10+ and a free Gemini API key from https://aistudio.google.com/apikey

```bash
git clone https://github.com/YOUR-USERNAME/vision-analyser.git
cd vision-analyser

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

export GEMINI_API_KEY="your-key"   # Windows PowerShell: $env:GEMINI_API_KEY="your-key"
streamlit run app.py
```

Open the URL Streamlit prints (usually http://localhost:8501).

### Configuration

| Variable | Required | Default | Purpose |
|---|---|---|---|
| `GEMINI_API_KEY` | yes | none | Your Gemini API key |
| `GEMINI_MODEL` | no | `gemini-flash-latest` | Model name to use |

## Project Structure

```
app.py            Streamlit UI
analyzer.py       Validation, prompts, API call, error handling
requirements.txt  Dependencies
```

## Troubleshooting

- **"GEMINI_API_KEY is not set"**: set the variable in the same terminal you run Streamlit from.
- **"Model not found"**: set `GEMINI_MODEL` to a model listed at https://ai.google.dev/models.
- **Rate limit**: free-tier quotas are limited; wait a minute.

## License

MIT, see [LICENSE](LICENSE).
