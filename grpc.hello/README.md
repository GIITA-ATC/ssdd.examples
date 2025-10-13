# gRPC & Protocol Buffers Example (Python)

This example demonstrates a simple gRPC server and client in Python using Protocol Buffers.

### 1. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Compile the `.proto` file

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. hello.proto
```

### 4. Run the gRPC server

```bash
python server.py
```

### 5. Run the client (in another terminal)

```bash
python client.py <host> <port>
```

## Exit and(or remove) the virtual environment

To exit the virtual environment, run:

```bash
deactivate
```

You can remove generated files with:

```bash
rm -f hello_pb2.py hello_pb2_grpc.py
```

Finally, if you want to remove the virtual environment, simply delete the `venv` directory:

```bash
rm -rf venv
```
