SHELL := /bin/bash

set: # Sets up the required files and directories
	touch .env
	echo "OPENAI_API_KEY=" >> .env
	mkdir -p io/chat

up: # Start streamlit
	@streamlit run --global.developmentMode False --server.headless True --server.allowRunOnSave False --theme.base dark main.py

