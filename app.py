import streamlit as st
import json
import os
from datetime import datetime

st.set_page_config(page_title=".NET 8.0 Journey", layout="centered")

st.title("🧭 .NET 8.0 Developer Learning Journey")
st.subheader("🌟 Week 1: Core C# & .NET Basics")

# User login / name entry
user_name = st.text_input("👤 Enter your name to begin:")
if not user_name:
    st.warning("Please enter your name to proceed.")
    st.stop()

# Load JSON content
json_path = os.path.join("content", "phase1", "week1.json")
try:
    with open(json_path, "r") as f:
        data = json.load(f)
except FileNotFoundError:
    st.error("Challenge file not found.")
    st.stop()

st.markdown(f"**Badge:** 🎖️ {data.get('badge', '')}")
st.markdown(f"**Leaderboard:** 🏆 {data.get('leaderboard', '')}")
st.markdown("---")

# Split challenges
mcq_challenges = [c for c in data["challenges"] if c["type"] == "mcq"][:10]
code_challenges = [c for c in data["challenges"] if c["type"] == "coding"]

# --- Timer for MCQ section ---
if "quiz_start_time" not in st.session_state:
    st.session_state.quiz_start_time = datetime.now()

elapsed = datetime.now() - st.session_state.quiz_start_time
minutes, seconds = divmod(elapsed.seconds, 60)
st.markdown(f"⏰ **Time elapsed:** `{minutes:02d}:{seconds:02d}`")

# Part 1: MCQ Arena
st.header("🧠 Part 1: MCQ Arena (10 Questions)")

score = 0
for idx, challenge in enumerate(mcq_challenges):
    st.markdown(f"### MCQ {idx + 1} / {len(mcq_challenges)}")
    answer = st.radio(challenge["question"], challenge["options"], key=f"mcq_{idx}")
    if st.button(f"Submit Answer {idx + 1}", key=f"btn_mcq_{idx}"):
        if answer == challenge["answer"]:
            st.success("✅ Correct!")
            score += 1
        else:
            st.error("❌ Incorrect.")

# Part 2: Code Craft
st.header("👨‍💻 Part 2: Code Craft")
for idx, challenge in enumerate(code_challenges):
    st.markdown(f"### Coding Challenge {idx + 1}")
    st.markdown(f"**{challenge['title']}**")
    st.markdown(challenge["description"])
    st.text(f"Input: {challenge['input']}")
    st.text_area("Write your code in C# (offline)", height=150, key=f"code_{idx}")
    st.info("⚠️ C# execution not supported in-browser. Submit offline or use peer review.")

# Final MCQ Score
st.markdown("---")
total_mcqs = len(mcq_challenges)
st.markdown(f"### 🏁 Final MCQ Score for {user_name}: **{score} / {total_mcqs}**")
