#!/usr/bin/python3
# Extracted from: https://www.rabbitmq.com/tutorials/tutorial-five-python.html
'Usage: {0} [binding key]...\n'

import sys
import pika


def callback(ch, method, properties, body):
    print(f"[x] Received {method.routing_key}: {body.decode()}")


binding_keys = sys.argv[1:]
if not binding_keys:
    sys.stderr.write(__doc__.format(sys.argv[0]))
    sys.exit(1)

localhost = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(localhost)
channel = connection.channel()

channel.exchange_declare(exchange='twitter-pattern', exchange_type='topic')
result = channel.queue_declare(queue='', exclusive='True')
queue_name = result.method.queue

for binding_key in binding_keys:
    channel.queue_bind(
        queue=queue_name,
        routing_key=binding_key,
        exchange='twitter-pattern',
    )

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
