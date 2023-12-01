#!/usr/bin/python3

import os
from dotenv import load_dotenv

def check_api_key():
    load_dotenv()

    err_message_key = "Please input your key in `config`"
    assert os.getenv("OPENAI_API_KEY") not in [None, ""], err_message_key
