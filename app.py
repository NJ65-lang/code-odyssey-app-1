import streamlit as st
import json
import os

st.set_page_config(page_title=".NET 8.0 Journey", layout="centered")

st.title("🧭 .NET 8.0 Developer Learning Journey")
st.subheader("🌟 Week 1: Core C# & .NET Basics")

# Construct the path to the JSON file
json_path = os.path.join("content", "phase1", "week1.json")

# Load challenge data
try:
    with open(json_path, "r") as f:
        data = json.load(f)
except FileNotFoundError:
    st.error("Challenge file not found. Please check the file path.")
    st.stop()

# Display badge and leaderboard details
st.markdown(f"**Badge:** 🎖️ {data.get('badge', '')}")
st.markdown(f"**Leaderboard:** 🏆 {data.get('leaderboard', '')}")

# Score tracking (only MCQs are auto-evaluated for now)
score = 0

# Loop through each challenge
for idx, challenge in enumerate(data["challenges"]):
    st.markdown(f"### Challenge {idx + 1}")

    if challenge["type"] == "mcq":
        answer = st.radio(challenge["question"], challenge["options"], key=f"mcq_{idx}")
        if st.button(f"Submit Answer {idx + 1}", key=f"btn_{idx}"):
            if answer == challenge["answer"]:
                st.success("✅ Correct!")
                score += 1
            else:
                st.error("❌ Incorrect.")
    
    elif challenge["type"] == "coding":
        st.markdown(f"**{challenge['title']}**")
        st.markdown(f"{challenge['description']}")
        st.text(f"Input: {challenge['input']}")
        st.text_area("Write your code in C# (offline)", height=150, key=f"code_{idx}")
        st.info("⚠️ C# code execution is not supported in-browser. Please submit this coding challenge offline or via peer review.")

# Final score (MCQs only)
st.markdown("---")
total_mcqs = sum(1 for c in data["challenges"] if c["type"] == "mcq")
st.markdown(f"### 🏁 Final Score (MCQs Only): **{score} / {total_mcqs}**")
