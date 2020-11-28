import argparse
import time, threading
import string
import random
import paho.mqtt.client as mqtt

# <HOST> <PORT> <TOPIC> <MESSAGE> <FREQUENCY>

parser = argparse.ArgumentParser()
parser.add_argument('host', type=str)
parser.add_argument('--port', default=1883, type=int)
parser.add_argument('topic', type=str)
parser.add_argument('--message_length', default=116, type=int, dest='ml')
parser.add_argument('--frequency', default=10, type=int)

args = parser.parse_args()


def randstr(st=string.ascii_letters, N=args.ml):
    return ''.join(random.choice(st) for _ in range(N))


def send_mqtt():
    print(randstr())
    mqttc.publish(args.topic, payload=randstr())
    threading.Timer(1 / args.frequency, send_mqtt).start()


mqttc = mqtt.Client()
mqttc.connect(args.host, args.port)

send_mqtt()