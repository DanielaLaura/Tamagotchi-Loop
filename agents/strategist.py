import openai
from agents.agent_styles import apply_agent_style

def suggest_exit(trigger: str, mood: dict, style: str = "Stoic") -> str:
    system_prompt = apply_agent_style(
        "You are a strategist. Your job is to offer an actionable next step to disrupt or exit the current loop.",
        style
    )
    user_input = f"Trigger: {trigger}\nMood: {mood}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        temperature=0.8
    )
    return response.choices[0].message["content"]
