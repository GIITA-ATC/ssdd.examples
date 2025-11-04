#!/usr/bin/python3
# Extracted from: https://www.rabbitmq.com/tutorials/tutorial-three-python.html

import pika


def callback(ch, method, properties, body):
	print(f"[x] Received {body.decode()}")


localhost = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(localhost)
channel = connection.channel()

channel.exchange_declare(exchange='twitter', exchange_type='fanout')
result = channel.queue_declare(queue='', exclusive='True')

queue_name = result.method.queue
channel.queue_bind(exchange='twitter', queue=queue_name)

channel.basic_consume(
	queue=queue_name,
	on_message_callback=callback,
	auto_ack=True,
)

print("[*] Waiting for messages. To exit press Ctrl+")

try:
    channel.start_consuming()
except KeyboardInterrupt:
    print("\nStopping subscriber...")
    connection.close()
