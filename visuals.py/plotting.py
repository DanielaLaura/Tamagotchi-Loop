import pandas as pd
import streamlit as st

def plot_mood_timeseries(logs):
    if not logs: return
    df = pd.DataFrame([{"timestamp": l["timestamp"], **l["mood"]} for l in logs])
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.set_index("timestamp")
    st.line_chart(df)
