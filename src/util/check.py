#!/usr/bin/python3

import os
from dotenv import load_dotenv

def check_files(absolute_path):
    load_dotenv()

    err_message_key = "Please input your key in `config`"
    assert os.getenv("OPENAI_API_KEY") not in [None, ""], err_message_key

    if not os.path.exists("io/chat"):
        chat_path = os.path.join(absolute_path, "io", "chat")
        os.mkdir(chat_path)
