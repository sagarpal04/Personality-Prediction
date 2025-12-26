import streamlit as st
import numpy as np
import pickle

# ---------------- LOAD MODEL ----------------
with open("personality_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Personality Predictor",
    page_icon="🧠",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
    .title {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        color: #4B0082;
    }
    .result {
        font-size: 26px;
        font-weight: bold;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        background: linear-gradient(to right, #667eea, #764ba2);
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown('<div class="title">🧠 Personality Prediction App</div>', unsafe_allow_html=True)
st.write("")

# ---------------- SIDEBAR INPUTS ----------------
st.sidebar.header("📊 Enter Personality Traits")

def slider(label):
    return st.sidebar.slider(label, 0, 100, 50)

inputs = [
    slider("Social Energy"),
    slider("Alone Time Preference"),
    slider("Talkativeness"),
    slider("Deep Reflection"),
    slider("Group Comfort"),
    slider("Party Liking"),
    slider("Listening Skill"),
    slider("Empathy"),
    slider("Organization"),
    slider("Leadership"),
    slider("Risk Taking"),
    slider("Public Speaking Comfort"),
    slider("Curiosity"),
    slider("Routine Preference"),
    slider("Excitement Seeking"),
    slider("Friendliness"),
    slider("Planning"),
    slider("Spontaneity"),
    slider("Adventurousness"),
    slider("Reading Habit"),
    slider("Sports Interest"),
    slider("Online Social Usage"),
    slider("Travel Desire"),
    slider("Gadget Usage"),
    slider("Work Style Collaborative"),
    slider("Decision Speed")
]

# ---------------- MAIN SECTION ----------------
st.subheader("🔍 Predict Your Personality")
st.write("Fill the sliders and click the button below")

if st.button("🚀 Predict Personality"):
    input_array = np.array([inputs])
    input_scaled = scaler.transform(input_array)
    prediction = model.predict(input_scaled)[0]

    label_map = {
        0: "🧍 Introvert",
        1: "⚖️ Ambivert",
        2: "🗣️ Extrovert"
    }

    st.markdown(
        f'<div class="result">Predicted Personality: {label_map[prediction]}</div>',
        unsafe_allow_html=True
    )

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("💡 Built with Streamlit & Logistic Regression")
