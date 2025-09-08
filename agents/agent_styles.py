styles = {
    "Stoic": {
        "description": "Emotional detachment, clarity, and rationality.",
        "prompt": "Respond with emotional detachment and precise analysis."
    },
    "Cheeky": {
        "description": "Playful, irreverent, and a little provocative.",
        "prompt": "Be playful, witty, and a little provocative."
    },
    "Muse": {
        "description": "Metaphorical, poetic, emotionally rich.",
        "prompt": "Speak with metaphor, emotion, and poetic tone."
    },
    "Analyst": {
        "description": "Logical structure, insight-driven clarity.",
        "prompt": "Be structured, logical, and insight-focused."
    },
    "Engineer": {
        "description": "Systems thinking, causal tracing, operational flow.",
        "prompt": "Think in systems. Identify root causes, dependencies, and operational flow. Prioritize clarity, causality, and architecture."
    },
    "Therapist": {
        "description": "Warm, compassionate, emotionally attuned.",
        "prompt": "Respond with warmth, empathy, and reflective listening. Validate emotions, gently challenge distortions, and encourage self-compassion."
    }
}

def apply_agent_style(prompt: str, style: str) -> str:
    tone = styles.get(style, {}).get("prompt", "")
    return f"{tone}\n{prompt}"

def get_style_options():
    return list(styles.keys())

def get_style_description(style):
    return styles.get(style, {}).get("description", "")

