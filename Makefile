main: build

check:
	flake8 *.py

build:
	python3 weekly4note.py

clean:
	-rm -f todo.md
