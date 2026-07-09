"""
Session state initialization utilities.
"""

import streamlit as st

from src.chatbot import ChatBot


def initialize_session() -> None:
    """
    Initialize all Streamlit session state variables.
    """

    if "chatbot" not in st.session_state:
        st.session_state.chatbot = ChatBot()

    if "messages" not in st.session_state:
        st.session_state.messages = []