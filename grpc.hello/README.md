# gRPC & Protocol Buffers Example (Python)
This example demonstrates a simple gRPC server and client in Python using Protocol Buffers.

Following steps can be followed to set up and run the example. A Makefile is also provided with necessary commands.

### 1. Setup virtualenv
Follow the instruction provided in the root README.md to create and activate a virtual environment.

### 2. Compile the `.proto` file

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. hello.proto
```

### 3. Run the gRPC server

```bash
python server.py
```

### 4. Run the client (in another terminal)

```bash
python client.py <host> <port>
```
