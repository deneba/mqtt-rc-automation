'''
Title: Use MQTT to control RF433 MHz devices
Author: Dr. Asif Rana (aiqbalrana@gmail.com)
Date: Mar 20, 2016
'''

import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import time
import sys
from ctypes import cdll


# pre-declare variables
ser = 0
rclib = 0

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("/home/command/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
     print("Time:" + time.strftime("%d/%b/%y %H%M%S",time.localtime()) + "," +  msg.topic+ " " +str(msg.payload))
     command = str(msg.payload)
     if str(msg.topic) == "/home/command/rf433":
         rclib.sendCommand(command,24,4)
     elif str(msg.topic) == "/home/command/rfled1":
         rclib.sendCommand(command,24,5)
     else:
         print("Warning: unrecognized command")
     time.sleep(0.1)

if __name__ == '__main__':
    # Setup RC Switch Library
    rclib = cdll.LoadLibrary('./deneb-rc-switch/PiSwitchLib.so')
    rclib.setup()
    print("rc switch library initialized")

    # Setup MQTT and stay listening
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("localhost")
    client.loop_forever()
