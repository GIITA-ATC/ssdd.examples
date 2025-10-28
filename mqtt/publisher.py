#!/usr/bin/env python3
'Usage: {0} [H | T]\n - H (default): humidity events\n - T: temperature events'

import sys
import json
import time
import random
import paho.mqtt.client as mqtt

SENSOR_1 = 'S001'
SENSOR_2 = 'S002'


def take_reading(type):
    return {
        'identifier': SENSOR_2 if type == 'T' else SENSOR_1,
        'value': random.randint(60, 80),
        'unit': '°C' if type == 'T' else '% RH',
        'timestamp': time.time()
    }


def on_connect(client, userdata, flags, info, properties):
    print(
        f"\nConnected to broker ({info})\n"
        f"Client: {client}\n"
        f"User data: {userdata}\n"
        f"Flags: {flags}\n"
        f"Properties: {properties}\n"
    )


def on_publish(client, userdata, mid, info, properties):
    print(f"Message {mid} published ({info})")


publisher = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2,
    protocol=mqtt.MQTTv5
)

publisher.on_connect = on_connect
publisher.on_publish = on_publish
publisher.connect('localhost', 1883)
publisher.loop_start()  # Start networking daemon

reading_type = 'H'
if len(sys.argv) > 1 and sys.argv[1] in ('H', 'T'):
    reading_type = sys.argv[1]

try:
    while True:
        reading = take_reading(reading_type)
        payload = json.dumps(reading)
        topic = f'iotevents/{reading_type}/{reading["identifier"]}'

        # At most once/maybe. QoS 1: at least once. QoS 2: exactly once
        publish_info = publisher.publish(topic, payload, qos=1)

        print(f"Queued reading {publish_info.mid} ({publish_info.rc})")
        time.sleep(1)

except KeyboardInterrupt:
    print("\nStopping publisher...")
finally:
    publisher.loop_stop()
    publisher.disconnect()
