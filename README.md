# 🧠 Tamagotchi Mood Loop

A symbolic reflection app powered by GPT-4o. This interactive Streamlit tool is an experimental interface for studying adaptive AI reflection an user emotion modeling.


##

## ✨ Features

- Mood sliders for real-time emotional input
- Symbolic triggers and agent personality selection
- Reflections generated using OpenAI GPT-4o
- Session log with mood/trigger/style tracking
- Auto-summary of recent symbolic states
- Log persistence to local JSON file (`logs.json`)

## 🛠️ Installation

1. **Clone the repo**:

   ```bash
   git clone https://github.com/yourusername/tamagotchi-mood-loop.git
   cd tamagotchi-mood-loop
   ```

2. **(Optional) Create and activate a virtual environment**:

   ```bash
   python3 -m venv tamagochi
   source tamagochi/bin/activate  # On Windows: tamagochi\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Create/Open your logs file (optional)**:

   Create an empty `logs.json` in the project root:

   ```bash
   echo "[]" > logs.json
   ```

## 🚀 Running the App

Start the Streamlit app with:

```bash
streamlit run app.py
```

Then open the URL shown in your terminal (typically `http://localhost:8501`).

## 🧩 Directory Structure

```
.
├── app.py                         # Main Streamlit application
├── logs.json                     # (Optional) persistent reflection logs
├── requirements.txt              # Project dependencies
├── agents/
│   └── agent_styles.py           # Defines personality presets
├── engine/
│   └── triggers.py               # Symbolic triggers and prompts
├── memory/
│   └── summarizer.py             # Reflection summarization logic
```

## 🔐 API Key

You’ll need an [OpenAI API key](https://platform.openai.com/account/api-keys). Paste it into the input field when prompted inside the app.

## 🧠 Concept

The Tamagotchi Mood Loop is an interactive emotional-feedback prototype that models symobolic context and generates adaptive reflections for cognitive awareness.

## 🧼 Troubleshooting

- **Missing timestamp error**: Make sure your logs contain `"timestamp"` keys. These are auto-injected during new reflections in the latest app version.
- **OpenAI version errors**: You must use `openai>=1.0.0` — we use `OpenAI(api_key=...)` and `client.chat.completions.create(...)` per the latest SDK.

## 🧪 Example Log Entry

```json
{
  "timestamp": "2025-09-07 14:30",
  "trigger": "Recognition withdrawal",
  "reflection": "You're seeking control by overperforming in ambiguous spaces...",
  "style": "Analyst",
  "mood": {
    "calmness": 0.4,
    "energy": 0.8,
    "curiosity": 0.9,
    "control": 0.6,
    "intensity": 0.7,
    "balance": 0.5
  }
}
```

## 📄 License

MIT — free to remix, adapt, or repurpose for your own reflection experiments.

---

> Built for personal narrative feedback loops. Your subconscious has a UI now.
