Instalar
--------

- protobuf-compiler
- python3-protobuf


Generar stubs
-------------

$ python3 -m grpc_tools.protoc -I=. --python_out=. sensor.proto


Run server
----------

% ./udp-server.py


Run client
----------

% ./udp-client.py localhost

.
