def summarize_logs(logs):
    summary = "Recent Symbolic States:\n"
    for entry in logs:
        timestamp = entry.get("timestamp", "unknown time")
        style = entry.get("style", "unknown style")
        trigger = entry.get("trigger", "unknown trigger")
        mood = entry.get("mood", {})
        note = entry.get("note", "")
        reflection = entry.get("reflection", "")
        summary += f"- {timestamp}: style={style}, trigger={trigger}, mood={mood}, note={note}, reflection={reflection}\n"
    return summary

