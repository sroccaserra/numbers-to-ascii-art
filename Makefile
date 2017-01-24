
.PHONY: test
.DEFAULT_GOAL := test-all

clean:
	find . \( -name \*.pyc -o -name \*.pyo -o -name __pycache__ \) -prune -delete

coverage:
	pytest --cov=ascii_art test

env:
	pyenv install -s 3.4.5
	pyenv local 3.4.5

lint:
	flake8 ascii_art test application.py

run:
	python -m application 1234567890

test:
	pytest test

requirements:
	pip install pytest flake8
