import streamlit as st
import requests

st.title("AI Short Video Series Generator")

backend_url = st.text_input(
    "Backend URL",
    "https://ai-shorts-system.onrender.com"
)

topic = st.text_input("Video Topic", "Motivation")
count = st.slider("Number of videos", 1, 20, 5)

if st.button("Generate Series"):
    payload = {"topic": topic, "count": count}
    res = requests.post(f"{backend_url}/generate", json=payload)
    st.json(res.json())
