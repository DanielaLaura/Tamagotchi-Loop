import streamlit as st
import os
import json
from datetime import datetime
from openai import OpenAI
from pathlib import Path  # ✅ NEW

from agents.agent_styles import apply_agent_style, get_style_options, get_style_description
from engine.triggers import select_trigger, get_trigger_prompt
from memory.summarizer import summarize_logs

st.set_page_config(page_title="Tamagotchi Mood Loop", layout="centered")
st.title("🧠 Tamagotchi Mood Loop")

LOG_PATH = "logs/reflection_logs.json"  # ✅ UPDATED

# --- API KEY INPUT ---
openai_api_key = st.text_input("Enter your OpenAI API Key", type="password")
if not openai_api_key:
    st.warning("Please enter your OpenAI API key to continue.")
    st.stop()

client = OpenAI(api_key=openai_api_key)

# --- MOOD STATE SLIDERS ---
st.subheader("🌡️ Mood Sliders")
state = {}
mood_names = [
    ("🌊 Calmness Level", "calmness"),
    ("⚡ Energy Level", "energy"),
    ("🔎 Curiosity Index", "curiosity"),
    ("🛡️ Control Score", "control"),
    ("🔥 Intensity", "intensity"),
    ("⚖️ Balance", "balance")
]

for name, key in mood_names:
    value = st.slider(name, 0, 100, 50)
    state[key] = round(value / 100, 2)

# --- AGENT STYLE ---
st.subheader("🧬 Agent Personality")
selected_style = st.selectbox("Choose an agent style:", get_style_options())
st.caption(get_style_description(selected_style))

# --- SYMBOLIC TRIGGER ---
st.subheader("🔁 Symbolic Trigger")
trigger = select_trigger()
st.caption(get_trigger_prompt(trigger))

# --- REFLECTION INPUT ---
st.subheader("💭 Input Prompt")
prompt = st.text_area("What do you want the agent to reflect on?", height=200)

# --- Load previous logs ---
if os.path.exists(LOG_PATH):
    with open(LOG_PATH, "r") as f:
        persistent_logs = json.load(f)
else:
    persistent_logs = []

# --- GENERATE REFLECTION ---
if st.button("✨ Generate Reflection") and prompt:
    mood_context = ", ".join([f"{k}: {v}" for k, v in state.items()])
    styled_prompt = apply_agent_style(
        f"Mood context: {mood_context}\nSymbolic Trigger: {trigger}\n{prompt}",
        selected_style
    )
    try:
        response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": styled_prompt}],
    temperature=0,     # forces greedy, deterministic decoding
    top_p=1,           # disables nucleus sampling
    n=1                # return only one completion
)
        reflection = response.choices[0].message.content.strip()

        st.markdown("---")
        st.subheader("🪞 Reflection")
        st.markdown(reflection)

        log_entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "trigger": trigger,
            "reflection": reflection,
            "style": selected_style,
            "mood": state,
            "note": prompt
        }

        if "logs" not in st.session_state:
            st.session_state.logs = []
        st.session_state.logs.append(log_entry)
        persistent_logs.append(log_entry)

        # ✅ Ensure logs folder exists
        Path("logs").mkdir(parents=True, exist_ok=True)

        with open(LOG_PATH, "w") as f:
            json.dump(persistent_logs, f, indent=2)

    except Exception as e:
        st.error(f"Failed to generate reflection:\n\n{e}")

# --- SESSION LOG ---
if "logs" in st.session_state and st.session_state.logs:
    st.markdown("---")
    st.subheader("🧾 Reflection Log")
    for entry in reversed(st.session_state.logs):
        timestamp = entry.get("timestamp", "unknown time")
        st.markdown(f"**Timestamp:** {timestamp}  |  **Trigger:** {entry['trigger']}  |  **Style:** {entry['style']}")
        st.markdown(entry["reflection"])
        st.markdown("---")

    # --- SUMMARY ---
    st.subheader("📊 Symbolic Summary")
    summary = summarize_logs(st.session_state.logs)
    st.text(summary)
