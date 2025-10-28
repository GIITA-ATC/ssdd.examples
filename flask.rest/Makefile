VENV        := .venv
PY          := $(VENV)/bin/python
PIP         := $(VENV)/bin/pip

.PHONY: all install run-server run-client clean distclean

all: install

$(VENV):
	python3 -m venv $(VENV)

install: $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

run-server:
	$(PY) server.py

run-client:
	$(PY) client.py

clean:
	rm -rf __pycache__

distclean: clean
	rm -rf $(VENV)
