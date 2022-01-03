
all:
	docker build -t words .

run:
	docker run words

push:
	docker push cadizm/words:latest

.PHONY: all run push
