import os 
import streamlit as st 
from langchain.schema import (
    AIMessage,
    HumanMessage
)

def display_messages():
    for index, message in enumerate(st.session_state.messages):
        if type(message) in [AIMessage]:
            with st.chat_message("assistant"):
                st.write(message.content)
            if index > 2:
                if st.button("Export Markdown"):
                    name = message.content[:30]
                    file_name = os.path.join("io", "markdown", f"{name}.json")
                    with open(file_name, "w") as f:
                        f.write(message.content)

        elif type(message) == HumanMessage:
            with st.chat_message("user"):
                st.write(message.content)
