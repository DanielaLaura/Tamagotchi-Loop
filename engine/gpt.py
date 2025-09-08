from openai import OpenAI
import json

def generate_gpt_insight(api_key, log_path):
    client = OpenAI(api_key=api_key)

    try:
        with open(log_path, "r") as f:
            logs = json.load(f)
    except FileNotFoundError:
        return "No log data found."

    recent_logs = logs[-5:]
    prompt = (
        "Analyze the following symbolic emotional states and triggers. "
        "Identify any recurring loops, symbolic themes, or behavioral patterns. "
        "If possible, name the loop and suggest a way to shift it.\n\n"
    )

    for entry in recent_logs:
        timestamp = entry.get("timestamp", "unknown time")
        trigger = entry.get("trigger", "unknown trigger")
        mood = entry.get("mood", "unknown mood")
        note = entry.get("note", "")
        prompt += f"- {timestamp}: {trigger}, mood: {mood}, note: {note}\n"

    prompt += "\nPlease respond with a concise analysis."

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        # Fallback logic if gpt-4o fails
        fallback_models = ["gpt-3.5-turbo"]
        for fallback_model in fallback_models:
            try:
                response = client.chat.completions.create(
                    model=fallback_model,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7,
                )
                return f"[Fallback to {fallback_model}]\n\n" + response.choices[0].message.content.strip()
            except Exception:
                continue

        return f"Error generating insight: {str(e)}"
