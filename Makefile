help: # Print help on Makefile
	@grep '^[^.#]\+:\s\+.*#' Makefile | \
	sed "s/\(.\+\):\s*\(.*\) #\s*\(.*\)/`printf "\033[93m"`\1`printf "\033[0m"`	\3 [\2]/" | \
	expand -t20

SHELL:=/bin/bash
BUILD:=docker build -t localgpt:latest -f config/Dockerfile .
RUN:=docker run --name gpt --rm -v $PWD:/LocalGPT --network=host localgpt:latest

build: $(SHELL)
build: 
	$(BUILD)

run: $(SHELL)
run: 
	$(RUN)
