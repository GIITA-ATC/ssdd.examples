#!/usr/bin/env python3

import json
import paho.mqtt.client as mqtt

TOPIC = "iotevents/+/#"  # '+' single-level, '#' multi-level


def on_message(client, userdata, msg):
    try:
        decoded = json.loads(msg.payload)
        pretty = json.dumps(decoded, indent=2)
        print(f"\nTopic: {msg.topic}\nPayload:\n{pretty}\n")

    except json.JSONDecodeError:
        print(f"[{msg.topic}] non-JSON payload: {msg.payload!r}")


subscriber = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2,
    protocol=mqtt.MQTTv5,
)

subscriber.on_message = on_message
subscriber.on_disconnect = lambda *args: print("Disconnected.")
subscriber.connect("localhost", 1883)
subscriber.subscribe(TOPIC)

try:
    subscriber.loop_forever()
except KeyboardInterrupt:
    print("\nStopping subscriber...")
finally:
    subscriber.disconnect()
