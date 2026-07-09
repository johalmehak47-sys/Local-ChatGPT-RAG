"""
Streamlit application entry point.
"""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st

from components.chat import render_chat
from components.sidebar import render_sidebar
from components.uploader import render_uploader
from utils.session import initialize_session

st.set_page_config(
    page_title="Local ChatGPT",
    page_icon="📚",
    layout="wide",
)

initialize_session()

render_sidebar()

st.title("📚 Local ChatGPT")

st.markdown(
    """
Chat with your documents using **Gemini**, **LangChain**, and **ChromaDB**.
"""
)

# Welcome message
if len(st.session_state.messages) == 0:

    st.info(
        """
👋 **Welcome!**

You can:

- 📄 Upload PDF documents
- 💬 Ask questions about them
- 📚 Get answers grounded in your documents

Start by uploading a PDF or ask a question below.
"""
    )

with st.expander("📄 Upload Documents", expanded=False):
    render_uploader()

st.divider()

render_chat()

st.divider()

st.caption(
    "Local ChatGPT • Version 1.0"
)