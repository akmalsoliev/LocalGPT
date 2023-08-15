import streamlit as st
import os


def streamlit_start(greetings_msg):
    st.set_page_config(
        page_title="Friendly Chatbot",
        page_icon="🤖"
    )
    st.header("Your own ChatGPT 🤖")

    MODELS = ["gpt-3.5-turbo", "gpt-4"]
    CHAT_PATH = "io/chat"

    with st.sidebar:

        # New Chat Button
        if st.button("New Chat"):
            st.session_state.messages = [greetings_msg]
            if "chat_selection" in st.session_state:
                del st.session_state["chat_selection"]
        st.divider()

        # Model selection 
        st.session_state.model = st.selectbox(
            "Select the GPT model",
            MODELS
        )
        st.write("Selected model: ", st.session_state.model)
        
        # Historical Interactions
        if os.path.exists(CHAT_PATH):
            files = []
            for _, _, f in os.walk(CHAT_PATH):
                if f:
                    files = f

            if len(files) > 0:
                st.divider()
                st.write("Historical Chat:")

            if len(files) > 20:
                delete_file = files[-1]
                path_delete_file = os.path.join(CHAT_PATH, delete_file)
                os.remove(path_delete_file)

            for file in files:
                clean_name = file.replace(".json", "")
                if st.button(clean_name):
                    file_path = os.path.join(CHAT_PATH, file)
                    st.session_state["chat_selection"] = file_path
