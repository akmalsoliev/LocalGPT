import json

from util import (
    streamlit_start,
    check_files,
    greetings,
    display_messages
)

import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage,
    AIMessage,
    messages_to_dict,
    messages_from_dict,
)


def main():
    check_files()
    streamlit_start()

    with open("config/settings.json", "r") as file:
        system_message_json = json.load(file)
    sys_message_str = system_message_json["content"]
    ai_greetings = greetings(sys_message_str)

    # First of sequential run
    if "messages" not in st.session_state:
        st.session_state.messages = [
            ai_greetings
        ]

    # init ChatGPT
    chat = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=1,
    )

    prompt = st.chat_input("Say something...")
    if prompt:
        human_message = HumanMessage(content=prompt)
        st.session_state.messages.append(human_message)

        with st.spinner("Thinking..."):
            response = chat(st.session_state.messages)
        ai_response = response.content
        ai_message = AIMessage(content=ai_response)
        st.session_state.messages.append(ai_message)

    display_messages()


if __name__ == "__main__":
    main()
