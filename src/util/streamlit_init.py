import streamlit as st
import os
from glob import glob


def streamlit_start(greetings_msg):
    st.set_page_config(
        page_title="Friendly Chatbot",
        page_icon="🤖"
    )
    st.header("Your own ChatGPT 🤖")

    MODELS = ["gpt-4-1106-preview", "gpt-4" "gpt-3.5-turbo-1106"]
    CHAT_PATH = "io/chat"

    with st.sidebar:

        # New Chat Button
        if st.button("New Chat"):
            st.session_state.messages = [greetings_msg]
            if "chat_selection" in st.session_state:
                del st.session_state["chat_selection"]
        st.divider()

        # Temperature 
        st.session_state.temperature = st.slider(
            "Model temperature",
            .0, 1., 1.,
        )
        # Model selection 
        st.session_state.model = st.selectbox(
            "Select the GPT model",
            MODELS
        )
        st.write("Selected model: ", st.session_state.model)
        
        # Historical Interactions
        if os.path.exists(CHAT_PATH):
            files = glob(f"{CHAT_PATH}/*.json")
            files.sort(key=os.path.getmtime, reverse=True)

            if len(files) > 0:
                st.divider()
                st.write("Historical Chat:")

            if len(files) > 21:
                delete_file = files[-1]
                os.remove(delete_file)

            for file in files:
                name_file = os.path.basename(file)
                clean_name = name_file.replace(".json", "")
                if st.button(clean_name):
                    st.session_state["chat_selection"] = file
