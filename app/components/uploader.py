"""
PDF uploader component.
"""

import streamlit as st

from src.indexing import IndexingService


def render_uploader() -> None:

    uploaded_file = st.file_uploader(
        "Choose a PDF document",
        type=["pdf"],
    )

    if uploaded_file is None:
        return

    indexing_service = IndexingService()

    with st.spinner("Indexing document..."):

        result = indexing_service.upload_pdf(
            uploaded_file
        )

    if result["already_indexed"]:

        st.info(
            f"📄 '{result['filename']}' is already indexed."
        )

    else:

        st.success(
            f"✅ Successfully indexed '{result['filename']}'."
        )

    st.rerun()