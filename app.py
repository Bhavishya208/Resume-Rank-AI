
import streamlit as st
from src.similarity import calculate_score

st.set_page_config(page_title="ResumeRank AI", layout="centered")
st.title("ResumeRank AI – Resume Match Analyzer")

resume = st.text_area("Paste Resume Text")
jd = st.text_area("Paste Job Description")

if st.button("Analyze Match"):
    if resume and jd:
        score = calculate_score(resume, jd)
        st.metric("Match Score", f"{score}%")
    else:
        st.warning("Please paste both Resume and Job Description")
