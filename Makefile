help: # Print help on Makefile
	@grep '^[^.#]\+:\s\+.*#' Makefile | \
	sed "s/\(.\+\):\s*\(.*\) #\s*\(.*\)/`printf "\033[93m"`\1`printf "\033[0m"`	\3 [\2]/" | \
	expand -t20

SHELL:=/bin/bash
BUILD:=docker build -t localgpt -f config/Dockerfile .

RUN_STREAMLIT:=streamlit run /LocalGPT/src/main.py
RUN:=docker run --name gpt --rm -v $(PWD):/LocalGPT -p 8501:8501 --env-file=.env localgpt $(RUN_STREAMLIT)

build:$(SHELL)
build: 
	$(BUILD)

run: $(SHELL)
run:
	if [[ -z "$(docker images -q localgpt 2> /dev/null)" ]]; then \
		$(BUILD); \
	fi
	$(RUN)
