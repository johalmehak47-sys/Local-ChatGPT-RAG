import streamlit as st


def render_chat():

    chatbot = st.session_state.chatbot

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    question = st.chat_input(
        "Ask a question about your documents..."
    )

    if not question:
        return

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            answer = chatbot.ask(question)

            st.markdown(answer)

            sources = chatbot.get_last_sources()

            if sources:

                with st.expander("📚 Sources"):

                    for item in sources:

                        st.markdown(
                            f"**📄 {item['source']}**  \n"
                            f"Page: {item['page']}"
                        )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )