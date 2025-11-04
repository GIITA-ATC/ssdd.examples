#!/usr/bin/python3
# Extracted from: https://www.rabbitmq.com/tutorials/tutorial-two-python.html

import time
import pika

STRICT_ROUND_ROBIN = True

def callback(ch, method, properties, body):
    print(f"[x] Received {body.decode()}")
    time.sleep(body.count(b'.'))
    print("[x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)
    # This ACK tells RabbitMQ that the message has been processed


localhost = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(localhost)
channel = connection.channel()

channel.queue_declare(queue='tasks', durable=True)

if not STRICT_ROUND_ROBIN:
    channel.basic_qos(prefetch_count=1)  # Not new msg until ACK

channel.basic_consume(
    queue='tasks',
    on_message_callback=callback,
    auto_ack=False,
)

print("[*] Waiting for messages. Press Ctrl+C to exit")

try:
    channel.start_consuming()
except KeyboardInterrupt:
    print("\nStopping worker...")
    connection.close()
