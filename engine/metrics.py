def compute_mood_metrics(state):
    return {
        "🌀 Stimulation": round(state.stimulation * 100, 1),
        "🔥 Intensity": round(state.intensity * 100, 1),
        "⚡ Energy": round(state.energy * 100, 1),
        "🔎 Curiosity": round(state.curiosity * 100, 1),
        "🌊 Calmness": round(state.calmness * 100, 1),
        "🧊 Numbness": round(state.numbness * 100, 1),
        "🔁 Obsession": round(state.obsession * 100, 1),
        "🎭 Performance": round(state.performance * 100, 1),
        "⏸️ Withdrawal": round(state.withdrawal * 100, 1),
        "🛡️ Control": round(state.control * 100, 1),
        "🧲 Attention": round(state.attention * 100, 1),
        "⚖️ Balance": round((
            state.calmness +
            (1 - state.obsession) +
            (1 - state.withdrawal) +
            (1 - state.numbness) +
            state.control +
            state.curiosity +
            state.energy -
            state.intensity * 0.5
        ) / 7 * 100, 1)
    }
