PYTHON=python3
VENV=venv
ACTIVATE=. $(VENV)/bin/activate;

.PHONY: all venv install proto server client clean distclean

all: install proto server

venv:
	$(PYTHON) -m venv $(VENV)

install: venv
	$(ACTIVATE) pip install --upgrade pip
	$(ACTIVATE) pip install -r requirements.txt

proto:
	$(ACTIVATE) python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. hello.proto

server:
	$(ACTIVATE) python server.py

client:
	$(ACTIVATE) python client.py localhost 2000

clean:
	rm -f hello_pb2.py hello_pb2_grpc.py
	rm -rf __pycache__

distclean: clean
	rm -rf $(VENV)
