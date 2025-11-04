# RabbitMQ Fanout Example (Python)
This example demonstrates a simple **publish/subscribe** pattern in Python using RabbitMQ and the Pika library.
A single publisher sends messages (tweets), and multiple subscribers receive *all* of them through a **fanout exchange**.

Following steps can be followed to set up and run the example. A Makefile is also provided with necessary commands.

### 1. Setup virtualenv
Follow the instruction provided in the root README.md to create and activate a virtual environment.

### 2. Install and start RabbitMQ broker
Install RabbitMQ and the Python client library if not already installed:

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

### 3. System overview
This example uses a **fanout exchange** named `tweets`.
A fanout exchange routes each published message to *all* queues bound to it — each subscriber gets a copy of every message.

You will need **three terminals**, one for each participant:

* **Terminal 1:** Subscriber 1
* **Terminal 2:** Subscriber 2
* **Terminal 3:** Publisher

### 4. Run the subscribers

Start two subscribers, each connected to its own queue, in separate terminals:

```bash
python subscriber.py
```

### 5. Run the publisher
In another terminal, start the publisher to send tweets to all subscribers through the fanout exchange:

```bash
python publisher.py "<my_tweet>"
```

Example:

```bash
python publisher.py "Hello world ..."
```

All subscribers will receive the same message.

### 6. Observe the broadcast behavior

Each subscriber prints all published tweets:

```
Publisher (P)
Subscriber 1 (S1)
Subscriber 2 (S2)
Exchange (E) - type: fanout
Message queues:
    twitter1 (S1)
    twitter2 (S2)

P --> E ------>  |||||||t3|t2|t1| --> S1 gets t1, t2, t3
      |    twitter1
      +----->  |||||||t3|t2|t1| --> S2 gets t1, t2, t3
           twitter2
```
