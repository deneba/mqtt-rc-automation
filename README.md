# mqtt-rc-automation

This runs on a raspberry pi to receive mqtt messages to generate rf packets using a simple 433 mhz rf transmitter connected to a gpio pin.

The rf library is based on pi-switch-python (https://github.com/lexruee/pi-switch-python). I've added protocol 4 and 5 to control:

- EasyHome rf switches from ALDI.
- Generic RF LED Dimmer

There is a readme.txt in the deneb-rc-switch folder describing how to compile the PiSwitchLib.so.

I chose to create my own library because the  C++ python link  mechansim (python boost) used by pi-switch-python takes very long time to compile on a raspberry pi. My solution can be compiled in mere seconds and the resulting lib can be imported using ctypes in python.