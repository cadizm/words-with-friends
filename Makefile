
all:
	docker build -t words .

run:
	docker run words
