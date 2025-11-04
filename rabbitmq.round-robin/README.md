# RabbitMQ Round-Robin Example (Python)

This example demonstrates a simple **work queue** pattern in Python using RabbitMQ and the Pika library.
It distributes jobs among multiple worker processes in a round-robin manner.

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

### 3. System overview
This example implements a simple **round-robin scheduler** using a single message queue named `job`.
Each job sent by the producer is delivered to the next available worker in order, ensuring load balancing across workers.

You need **three terminals** — one for each participant:

* **Terminal 1:** Worker 1
* **Terminal 2:** Worker 2
* **Terminal 3:** Producer

### 4. Run the workers
Start two workers that will receive and process jobs from the queue. In 2 separate terminals:

```bash
python worker.py
```

### 5. Run the producer

In another terminal, start the producer to send jobs to the queue:

```bash
python producer.py <a_string_with_an_arbitrary_number_of_dots>
```

The **number of dots (".")** in each string determines how long the worker will take to process the job (in seconds).

Example:

```bash
python producer.py job1.... job2. job3...
```

Interpretation:

* `job1` requires **4 seconds**
* `job2` requires **1 second**
* `job3` requires **3 seconds**

### 6. Observe the round-robin scheduling

Each worker will receive alternating messages:

```
 [W1] Received job1....
 [W2] Received job2.
 [W1] Received job3...
```

Change the value of `STRICT_ROUND_ROBIN` in `worker.py` to see how it affects message distribution.
