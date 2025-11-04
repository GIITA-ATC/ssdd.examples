VENV        := .venv
PY          := $(VENV)/bin/python
PIP         := $(VENV)/bin/pip

.PHONY: all install run-consumer run-producer clean distclean

all: install

$(VENV):
	python3 -m venv $(VENV)

install: $(VENV)
	sudo apt install -y rabbitmq-server
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

run-consumer:
	$(PY) subscriber.py

run-producer:
	$(PY) publisher.py

clean:
	rm -rf __pycache__

distclean: clean
	rm -rf $(VENV)
