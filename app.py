import streamlit as st
import json
import os

st.set_page_config(page_title="Code Odyssey", layout="centered")

st.title("🧭 .NET 8.0 Developer Learning Journey")
st.subheader("🌟 Week 1: Core C# & .NET Basics")

st.markdown(f"**Badge:** 🎖️ {data.get('badge', '')}")
st.markdown(f"**Leaderboard:** 🏆 {data.get('leaderboard', '')}")

# Construct safe relative path
json_path = os.path.join("content", "phase1", "week1.json")

try:
    with open(json_path, "r") as f:
        data = json.load(f)
except FileNotFoundError:
    st.error("Challenge file not found. Please check path.")
    st.stop()

score = 0

for idx, challenge in enumerate(data["challenges"]):
    st.markdown(f"### Challenge {idx + 1}")
    if challenge["type"] == "mcq":
        answer = st.radio(challenge["question"], challenge["options"], key=f"mcq_{idx}")
        if st.button(f"Submit Answer {idx+1}", key=f"btn_{idx}"):
            if answer == challenge["answer"]:
                st.success("✅ Correct!")
                score += 1
            else:
                st.error("❌ Incorrect.")
    elif challenge["type"] == "coding":
        code = st.text_area("Write your function here (reverse_string):", height=150, key=f"code_{idx}")
        if st.button(f"Run Code {idx+1}", key=f"btn_code_{idx}"):
            try:
                exec_globals = {}
                exec(code, exec_globals)
                func = exec_globals.get("reverse_string", lambda x: "")
                result = func(challenge["input"])
                if result == challenge["expected_output"]:
                    st.success("✅ Correct Output!")
                    score += 1
                else:
                    st.error(f"❌ Incorrect Output. Got '{result}', expected '{challenge['expected_output']}'")
            except Exception as e:
                st.error(f"⚠️ Error: {e}")

st.markdown("---")
st.markdown(f"### 🏆 Your Score: **{score} / {len(data['challenges'])}**")
