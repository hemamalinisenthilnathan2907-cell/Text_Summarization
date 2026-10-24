
import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="Text Summarization",
    page_icon="📝"
)

st.title("AI Text Summarization")
st.write("Summarize long text using Hugging Face Transformers")

@st.cache_resource
def load_model():
    summarizer = pipeline(
        "summarization",
        model="sshleifer/distilbart-cnn-12-6"
    )
    return summarizer

summarizer = load_model()

text = st.text_area(
    "Enter your text here:",
    height=250,
    placeholder="Paste your long paragraph here..."
)

if st.button("Generate Summary"):
    if text.strip():
        with st.spinner("Generating summary..."):
            result = summarizer(
                text,
                max_length=100,
                min_length=30,
                do_sample=False
            )

        st.subheader("Summarized Text")
        st.success(result[0]["summary_text"])

    else:
        st.warning("Please enter some text!")
