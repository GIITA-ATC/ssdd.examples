# REST API with Flask (Python)
This example demonstrates how a simple REST API can be implemented using Flask in Python.

Following steps can be followed to set up and run the example. A Makefile is also provided with necessary commands.

### 1. Setup virtualenv
Follow the instruction provided in the root README.md to create and activate a virtual environment.

### 2. Run the Flask server

```bash
python server.py
```

### 3. Run the client
You can use your web browser to access the REST API endpoints. For example, if the server is running on `localhost` and port `5000`, you can access:

- `http://localhost:5000/`

This will show a device list (GET).

Now, run the python client provided to update a device (PUT):

```bash
python client.py
```

Refresh the browser to see the updated device list.
