# frontend/app.py

import streamlit as st
import requests

# --- Configuration ---
BACKEND_URL = "https://shorts-backend-n73r.onrender.com"  # Replace with your Render backend URL

# --- Helper Function ---
def get_video_ideas(topic: str):
    """
    Calls the backend /generate endpoint and returns the list of short video ideas.
    """
    try:
        response = requests.get(f"{BACKEND_URL}/generate", params={"topic": topic})
        response.raise_for_status()  # Raise error if HTTP status is not 200

        data = response.json()
        return data.get("series", [])

    except requests.exceptions.RequestException as e:
        return [f"Error fetching data: {e}"]

# --- Streamlit App ---
st.set_page_config(page_title="AI Short Video Generator", page_icon="🎬", layout="centered")
st.title("🎬 AI Short Video Generator")
st.write("Generate a series of short video ideas automatically!")

# User input
topic = st.text_input("Enter a topic for your short videos:", "Motivation")

if st.button("Generate Ideas"):
    st.subheader("Generated Short Video Ideas:")
    ideas = get_video_ideas(topic)
    
    if ideas:
        for idx, idea in enumerate(ideas, start=1):
            st.write(f"{idx}. {idea}")
    else:
        st.write("No ideas generated. Try another topic.")
