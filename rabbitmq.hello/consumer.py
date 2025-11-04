#!/usr/bin/python3
# Extracted from: https://www.rabbitmq.com/tutorials/tutorial-one-python.html

import pika


def callback(ch, method, properties, body):
    print(f"[x] Received: ({method.delivery_tag}) {body.decode()}")


localhost = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(localhost)  # Blocks main thread
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_consume(
    queue='hello',
    on_message_callback=callback,
    auto_ack=True,  # No wait for ack from the consumer
)

print("[*] Waiting for messages. press Ctrl+C to exit")

try:
    channel.start_consuming()
except KeyboardInterrupt:
    print("\nStopping consumer...")
    connection.close()
