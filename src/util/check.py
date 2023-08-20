#!/usr/bin/python3

import os
from dotenv import load_dotenv

def check_files(absolute_path):
    load_dotenv()

    err_message_key = "Please input your key in `config`"
    assert os.getenv("OPENAI_API_KEY") not in [None, ""], err_message_key

    IO_CHAT_PATH = os.path.join(absolute_path, "io", "chat")
    if not os.path.exists(IO_CHAT_PATH):
        os.makedirs(IO_CHAT_PATH)
