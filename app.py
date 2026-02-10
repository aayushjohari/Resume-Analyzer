import streamlit as st
st.title("Resume Analyzer")

resume  = st.file_uploader("Upload file" , type = "pdf")
jd  = st.text_area("Paste Job description")

if resume and jd:
    st.success("Inputs received succesfully")