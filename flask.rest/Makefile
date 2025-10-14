PYTHON=python3
VENV=venv
ACTIVATE=. $(VENV)/bin/activate;

.PHONY: all install run-server run-client clean distclean

all: install

venv:
	$(PYTHON) -m venv $(VENV)

install: venv
	$(ACTIVATE) pip install --upgrade pip
	$(ACTIVATE) pip install -r requirements.txt

run-server:
	$(ACTIVATE) python server.py

run-client:
	$(ACTIVATE) python client.py

clean:
	rm -rf __pycache__

distclean: clean
	rm -rf $(VENV)
