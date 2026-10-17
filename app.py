"""
app.py - Streamlit front end for the Vision Code & Document Analyser.

Run with:  streamlit run app.py
"""

import streamlit as st

from analyzer import AnalyzerError, analyze, get_model_name

# Must be the first Streamlit call in the script.
st.set_page_config(page_title="Vision Analyser", page_icon="🔍", layout="centered")

st.title("🔍 Vision Code & Document Analyser")
st.caption("Upload a screenshot or paste text. Get a structured AI review in seconds.")

# ---- Sidebar: mode selection --------------------------------------------
with st.sidebar:
    st.header("Settings")
    mode = st.radio("Analysis mode", ["Code Analyser", "Document Analyser"])
    st.caption(f"Model: `{get_model_name()}`")

# ---- Inputs -------------------------------------------------------------
uploaded = st.file_uploader("Upload an image (PNG, JPG, WEBP)", type=["png", "jpg", "jpeg", "webp"])
if uploaded:
    st.image(uploaded, caption="Preview", use_container_width=True)

pasted_text = st.text_area("...or paste text / code (optional)", height=150)
question = st.text_input("Specific question (optional)", placeholder="e.g. Are there any security issues?")

# ---- Action -------------------------------------------------------------
if st.button("Analyse", type="primary"):
    try:
        with st.spinner("Analysing..."):
            result = analyze(
                mode=mode,
                image_bytes=uploaded.getvalue() if uploaded else None,
                mime_type=uploaded.type if uploaded else None,
                text=pasted_text,
                question=question,
            )
        st.markdown(result)
        st.download_button("Download report (.md)", result, file_name="analysis.md")
    except AnalyzerError as err:
        # Expected, user-fixable problems: show the message, no stack trace.
        st.error(str(err))
    except Exception:
        # Anything unexpected: generic message so we never leak internals.
        st.error("Something unexpected went wrong. Please try again.")
