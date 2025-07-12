main: build

check:
	flake8 gen_weekly_todo.py

build:
	python3 gen_weekly_todo.py

clean:
	-rm -f todo.md
