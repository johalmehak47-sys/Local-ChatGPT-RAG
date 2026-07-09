import streamlit as st

from src.vector_store import VectorStore


def render_sidebar() -> None:

    vector_store = VectorStore()

    stats = vector_store.get_stats()

    with st.sidebar:

        st.title("📚 Local ChatGPT")

        st.caption("Personal RAG Assistant")

        st.divider()

        st.subheader("Knowledge Base")

        st.metric(
            label="Indexed Chunks",
            value=stats["chunks"],
        )

        st.metric(
            label="Collection",
            value=stats["collection"],
        )

        if stats["ready"]:
            st.success("Knowledge Base Ready")
        else:
            st.warning("Knowledge Base Empty")

        st.divider()

        if st.button(
            "🗑️ Clear Conversation",
            use_container_width=True,
        ):
            st.session_state.messages = []
            st.rerun()

        st.divider()

        st.caption(
            """
Powered by

• Gemini

• LangChain

• ChromaDB

• Streamlit
"""
        )