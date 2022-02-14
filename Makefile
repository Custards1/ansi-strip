build:
	docker build . -t ansi-sweep

run: build;
	docker run -p 8000:8000 ansi-sweep