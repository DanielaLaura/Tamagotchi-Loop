import streamlit as st

TRIGGER_PROMPTS = {
    "⏸️ Silence": "No words. Just echo. Attention dissolves into stillness.",
    "🌀 Overstimulation": "Too much signal. The system starts to loop on itself.",
    "🪞 Loop Reflection": "You see yourself seeing yourself. Again.",
    "🧊 Power Freeze": "You paused. On purpose. Control became protection.",
    "🐾 Tamagotchi Mention": "You remember being fed — with the wrong intentions.",
    "🌊 Curiosity Spark": "Something flickers in the dark. You lean in."
}

def get_trigger_prompt(trigger):
    return TRIGGER_PROMPTS.get(trigger, "")

def get_trigger_options():
    return list(TRIGGER_PROMPTS.keys())

def select_trigger():
    return st.selectbox("What's the symbolic trigger?", get_trigger_options())
