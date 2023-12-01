import os 
import streamlit as st 
from langchain.schema import (
    AIMessage,
    HumanMessage
)
import markdown2
import pdfkit
import pyperclip

def display_messages():
    for index, message in enumerate(st.session_state.messages):
        if type(message) in [AIMessage]:
            with st.chat_message("assistant"):
                st.write(message.content)

            if index > 1:
                col1 = st.columns(1, gap="small")[0]

                with col1:
                    if st.button("Copy", key=f"copy-{index}"):
                        pyperclip.copy(message.content)

        elif type(message) == HumanMessage:
            with st.chat_message("user"):
                st.write(message.content)
