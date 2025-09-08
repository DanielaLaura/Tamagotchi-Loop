import streamlit as st
import os
import json
from openai import OpenAI

from agents.agent_styles import apply_agent_style, get_style_options, get_style_description
from memory.summarizer import summarize_logs
from engine.triggers import select_trigger

st.set_page_config(page_title="Tamagotchi Mood Loop", layout="centered")
st.title("🧠 Tamagotchi Mood Loop")

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
st.caption(f"{get_style_description(selected_style)}")

# --- SYMBOLIC TRIGGER ---
st.subheader("🔁 Symbolic Trigger")
trigger = select_trigger()

# --- REFLECTION INPUT ---
st.subheader("💭 Input Prompt")
prompt = st.text_area("What do you want the agent to reflect on?", height=200)

# --- GENERATE REFLECTION ---
if st.button("✨ Generate Reflection") and prompt:
    mood_context = ", ".join([f"{k}: {v}" for k, v in state.items()])
    styled_prompt = apply_agent_style(
        f"Mood context: {mood_context}\nSymbolic Trigger: {trigger}\n{prompt}",
        selected_style
    )
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": styled_prompt}]
        )
        reflection = response.choices[0].message.content
        st.markdown("---")
        st.subheader("🪞 Reflection")
        st.markdown(reflection)

        # Save to session
        if "logs" not in st.session_state:
            st.session_state.logs = []
        st.session_state.logs.append({
            "trigger": trigger,
            "reflection": reflection,
            "style": selected_style,
            "mood": state
        })
    except Exception as e:
        st.error(f"Failed to generate reflection: {e}")

# --- SESSION LOG ---
if "logs" in st.session_state and st.session_state.logs:
    st.markdown("---")
    st.subheader("🧾 Reflection Log")
    for entry in st.session_state.logs[::-1]:
        st.markdown(f"**Trigger:** {entry['trigger']} | **Style:** {entry['style']}")
        st.markdown(f"{entry['reflection']}")
        st.markdown("---")

    # --- SUMMARY ---
    st.subheader("📊 Symbolic Summary")
    summary = summarize_logs(st.session_state.logs)
    st.text(summary)
