Instalar
--------

- protobuf-compiler
- python3-protobuf


Generar stubs
-------------

$ python3 -m grpc_tools.protoc -I=. --python_out=. sensor.proto


Run server
----------

% ./server.py


Run client
----------

% ./client.py localhost

.
