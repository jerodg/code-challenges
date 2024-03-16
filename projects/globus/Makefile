.venv:
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt

.PHONY: run clean
run: .venv
	FLASK_APP=app.py .venv/bin/flask run
clean:
	-rm -rf .venv
