def apply_feedback_loop(mood, trigger):
    if trigger == "⏸️ Silence":
        mood.obsession += 0.2
        mood.withdrawal += 0.2
        mood.performance -= 0.1
        mood.curiosity -= 0.1
        mood.calmness += 0.1
        mood.intensity -= 0.1
        mood.control += 0.1
    elif trigger == "🌀 Overstimulation":
        mood.stimulation += 0.3
        mood.obsession += 0.2
        mood.numbness += 0.2
        mood.intensity += 0.2
        mood.energy -= 0.1
        mood.control -= 0.1
    elif trigger == "🪞 Loop Reflection":
        mood.curiosity += 0.2
        mood.obsession += 0.1
        mood.numbness -= 0.1
        mood.control += 0.1
    elif trigger == "🧊 Power Freeze":
        mood.withdrawal += 0.3
        mood.control += 0.2
        mood.intensity -= 0.1
        mood.performance -= 0.2
        mood.calmness += 0.1
    elif trigger == "🐾 Tamagotchi Mention":
        mood.obsession += 0.3
        mood.performance += 0.2
        mood.stimulation += 0.1
        mood.intensity += 0.2
        mood.energy += 0.1
    elif trigger == "🌊 Curiosity Spark":
        mood.curiosity += 0.4
        mood.energy += 0.2
        mood.intensity += 0.1
        mood.calmness += 0.2
        mood.numbness -= 0.2
    mood.clip()
    return mood
