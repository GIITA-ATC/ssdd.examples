# RabbitMQ Example (Python)
This example demonstrates a simple producer and consumer in Python using RabbitMQ and the Pika library:

```
Producer (P)
Consumer (C)
Message queue: hello

P --> ||||||m3|m2|m1| --> C
           hello
```

Following steps can be followed to set up and run the example. A Makefile is also provided with necessary commands.

### 1. Setup virtualenv

Follow the instruction provided in the root README.md to create and activate a virtual environment.

### 2. Install and start RabbitMQ broker
Install RabbitMQ if not already installed:

```bash
sudo apt install rabbitmq-server
```

Then start the RabbitMQ broker:

```bash
sudo service rabbitmq-server start
```

To enable the web-based management interface:

```bash
sudo rabbitmq-plugins enable rabbitmq_management
sudo service rabbitmq-server restart
```

You can now access the management dashboard at:
**[http://localhost:15672](http://localhost:15672)**
(Default credentials: `guest` / `guest`)

### 3. Check queues using rabbitmqadmin (optional)
```bash
rabbitmqadmin list queues
rabbitmqadmin delete queue name=<queue-name>
```

### 4. Run the producer
In one terminal, start the producer to send messages to the queue:

```bash
python producer.py
```

### 5. Run the consumer
In another terminal, start the consumer to receive messages:

```bash
python consumer.py
```
