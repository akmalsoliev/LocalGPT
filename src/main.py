import json

from util import (
    streamlit_start,
    check_files,
)

from dotenv import load_dotenv
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage,
)


def main():
    check_files()
    streamlit_start()

    with open("config/settings.json", "r") as file:
        system_message_json = json.load(file)
    sys_message = SystemMessage(content=system_message_json["content"])

    # init ChatGPT
    chat = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=.7,
    )

    # First of sequential run
    if "messages" not in st.session_state:
        st.session_state.messages = [
            sys_message,
        ]

    
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


def display_messages():
    for message in st.session_state.messages:
        if type(message) in [SystemMessage, AIMessage]:
            with st.chat_message("assistant"):
                st.write(message.content)
        elif type(message) == HumanMessage:
            with st.chat_message("user"):
                st.write(message.content)

if __name__ == "__main__":
    main()
