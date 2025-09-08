import openai
from agents.agent_styles import apply_agent_style

def detect_loop(trigger: str, mood: dict, style: str = "Analyst") -> str:
    system_prompt = apply_agent_style(
        "You are a loop analyst. Your job is to identify internal emotional loops based on the trigger and mood.",
        style
    )
    user_input = f"Trigger: {trigger}\nMood: {mood}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        temperature=0.7
    )
    return response.choices[0].message["content"]

