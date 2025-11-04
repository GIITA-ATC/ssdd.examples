# MQTT Paho Example (Python)
This example demonstrates a simple subscriber and publisher in Python using Paho MQTT.

Following steps can be followed to set up and run the example. A Makefile is also provided with necessary commands.

### 1. Setup virtualenv
Follow the instruction provided in the root README.md to create and activate a virtual environment.

### 2. Run mosquitto broker
Install mosquitto with `sudo apt install mosquitto` if not already installed. Then start the mosquitto broker with:

```bash
sudo service mosquitto start
netstat -tuln | grep 1883
```

### 3. Run the gRPC server

```bash
python publisher.py
```

### 4. Run the client (in another terminal)

```bash
python subscriber.py
```
