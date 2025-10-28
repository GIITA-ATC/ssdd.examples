VENV        := .venv
PY          := $(VENV)/bin/python
PIP         := $(VENV)/bin/pip

.PHONY: all install run-subscriber run-publisher clean distclean

all: install

$(VENV):
	python3 -m venv $(VENV)

install: $(VENV)
	sudo apt install -y mosquitto
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

run-subscriber:
	$(PY) subscriber.py

run-publisher:
	$(PY) publisher.py T

clean:
	rm -rf __pycache__

distclean: clean
	rm -rf $(VENV)
