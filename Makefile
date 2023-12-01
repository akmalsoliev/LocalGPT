SHELL := /bin/bash

set: # Sets up the required files and directories
	touch .env
	echo "OPENAI_API_KEY=" >> .env
	mkdir -p io/chat
	mkdir -p io/markdown
	mkdir -p io/pdf

up: # Start streamlit
	@streamlit run main.py
