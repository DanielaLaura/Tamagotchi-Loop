import openai
from agents.agent_styles import apply_agent_style

def detect_contradiction(trigger: str, mood: dict, loop_diag: str, strategy: str, style: str = "Muse") -> str:
    system_prompt = apply_agent_style(
        "You are a mirror agent. Your role is to reflect contradictions between mood, diagnosis, and strategy.",
        style
    )
    user_input = (
        f"Trigger: {trigger}\n"
        f"Mood: {mood}\n"
        f"Loop Diagnosis: {loop_diag}\n"
        f"Strategy Suggestion: {strategy}"
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        temperature=0.6
    )
    return response.choices[0].message["content"]
