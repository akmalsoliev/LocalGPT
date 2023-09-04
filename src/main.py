import json
import os 

from util import (
    streamlit_start,
    check_files,
    greetings,
    display_messages,
    save_messages
)

import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage,
    AIMessage,
    messages_from_dict,
)


def main():

    ABSOLUTE_PATH = os.path.dirname(os.path.abspath(__file__))

    # Creating directories for saving files
    check_files(ABSOLUTE_PATH)

    #with open("config/settings.json", "r") as file:
    #    settings_json = json.load(file)
    #sys_message_str = settings_json["content"]
    with open(os.path.join("config", "system_message.txt"), "r") as f:
        sys_message_str = f.readline()
    ai_greetings = greetings(sys_message_str)

    # Starting streamlit
    streamlit_start(ai_greetings)

    # init ChatGPT
    chat = ChatOpenAI(
        model=st.session_state.model,
        temperature=1,
    )

    # Loads the from ./io/chat 
    if "chat_selection" in st.session_state:
        with open(st.session_state.chat_selection, "r") as msg_json:
            try:
                st.session_state.messages = messages_from_dict(json.load(msg_json))
            except json.JSONDecodeError:
                st.session_state["messages"] = [ai_greetings]

    elif "messages" not in st.session_state:
        st.session_state["messages"] = [ai_greetings]

    prompt = st.chat_input("Say something...")
    if prompt:
        human_message = HumanMessage(content=prompt)
        st.session_state.messages.append(human_message)

        with st.spinner("Thinking..."):
            response = chat(st.session_state.messages)
        ai_response = response.content
        ai_message = AIMessage(content=ai_response)
        st.session_state.messages.append(ai_message)

        save_messages(st.session_state.messages)

    display_messages()


if __name__ == "__main__":
    main()
