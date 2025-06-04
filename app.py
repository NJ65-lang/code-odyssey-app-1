
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

# Display badge and leaderboard title
st.markdown(f"**Badge:** 🎖️ {data.get('badge', '')}")
st.markdown(f"**Leaderboard:** 🏆 {data.get('leaderboard', '')}")
st.markdown("---")

# Split challenges
mcq_challenges = [c for c in data["challenges"] if c["type"] == "mcq"]
code_challenges = [c for c in data["challenges"] if c["type"] == "coding"]

# Score tracking
score = 0

# Part 1: MCQ Arena
st.header("🧠 Part 1: MCQ Arena")
for idx, challenge in enumerate(mcq_challenges):
    st.markdown(f"### MCQ {idx + 1}")
    answer = st.radio(challenge["question"], challenge["options"], key=f"mcq_{idx}")
    if st.button(f"Submit Answer {idx + 1}", key=f"btn_mcq_{idx}"):
        response_time = datetime.now()
        if answer == challenge["answer"]:
            st.success("✅ Correct!")
            score += 1
        else:
            st.error("❌ Incorrect.")
        # Store responses (to be implemented): user_name, challenge_id, answer, response_time

# Part 2: Code Craft
st.header("👨‍💻 Part 2: Code Craft")
for idx, challenge in enumerate(code_challenges):
    st.markdown(f"### Coding Challenge {idx + 1}")
    st.markdown(f"**{challenge['title']}**")
    st.markdown(challenge["description"])
    st.text(f"Input: {challenge['input']}")
    st.text_area("Write your code in C# (offline)", height=150, key=f"code_{idx}")
    st.info("⚠️ C# execution not supported in-browser. Submit offline or use peer review.")

# Final Score for MCQs
st.markdown("---")
total_mcqs = len(mcq_challenges)
st.markdown(f"### 🏁 Final MCQ Score for {user_name}: **{score} / {total_mcqs}**")
