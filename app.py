import streamlit as st
from utils.analyzer import analyze_post

st.set_page_config(page_title="Toxic DM Simulator", layout="centered")

st.title("誹謗中傷DMシミュレーター")

input_text = st.text_area("投稿を入力してください", height=150)

if st.button("解析する"):
    if input_text.strip():
        result = analyze_post(input_text)
        st.subheader("毒性スコア")
        st.progress(result['toxicity'])
        st.write(f"{result['toxicity']*100:.1f} %")

        st.subheader("感情タイプ")
        st.write(", ".join(result['emotions']))

        st.subheader("自動生成されたDM")
        st.success(result['dm'])

    else:
        st.warning("投稿内容を入力してください。")
