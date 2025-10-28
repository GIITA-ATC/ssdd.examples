VENV        := .venv
PY          := $(VENV)/bin/python
PIP         := $(VENV)/bin/pip
PROTO_NAME  := hello
GEN_PY      := $(PROTO_NAME)_pb2.py $(PROTO_NAME)_pb2_grpc.py

.PHONY: all install run-server run-client clean distclean

all: install $(GEN_PY)

$(VENV):
	python3 -m venv $(VENV)

install: $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

$(GEN_PY): $(PROTO_NAME).proto
	$(PY) -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. $(PROTO_NAME).proto

run-server:
	$(PY) server.py

run-client:
	$(PY) client.py localhost 2000

clean:
	rm -f $(GEN_PY)
	rm -rf __pycache__

distclean: clean
	rm -rf $(VENV)
