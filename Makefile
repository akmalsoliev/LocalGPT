SHELL := /bin/bash

set: # Sets up the required files and directories
	@if [ ! -f .env ]; then \
		echo "Creating .env file"; \
		touch .env; \
		read -p "OpenAI Key: " key; \
		if [ -z "$$key" ]; then \
			echo "Error: OpenAI Key cannot be empty."; \
			exit 1; \
		fi; \
		echo "OPENAI_API_KEY=$$key" >> .env; \
		echo "Key added to .env file"; \
	else \
		echo ".env file already exists. If you want to update the OpenAI Key, please edit the .env file manually."; \
	fi

	@mkdir -p io/chat

	@if [ ! -f config/system_message.txt ]; then \
		read -p "System Message: " message; \
		mkdir -p config && touch config/system_message.txt; \
		echo "$$message" >> config/system_message.txt; \
	fi

	@if [ ! -f config/settings.json ]; then \
		touch config/settings.json; \
		echo '{}' >> config/settings.json; \
	fi

	@if [ ! -d io/chat ]; then \
		mkdir -p io/chat; \
	fi

up: # Start streamlit
	@streamlit run --global.developmentMode False --server.headless True --server.allowRunOnSave False --theme.base dark main.py

