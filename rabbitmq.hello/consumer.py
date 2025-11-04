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
    auto_ack=True,
    on_message_callback=callback,
)

print("[*] Waiting for messages. press Ctrl+C to exit")

try:
    channel.start_consuming()
except KeyboardInterrupt:
    print("\Stopping consumer...")
    connection.close()
