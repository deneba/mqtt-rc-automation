- First build the wiringPi
cd wiringPi
./build (It also installs it. Afterwards you need to use -lwiringPi in the compile line to link to it.)

- Building PiSwitchLib.so
make
g++ -shared -lwiringPi -Wl,-soname,PiSwitchLib.so -o  PiSwitchLib.so  PiSwitch.o

- Using PiSwitchLib.so

from ctypes import cdll
lib = cdll.LoadLibrary('./PiSwitchLib.so')
lib.setup()
lib.sendCommand("c297b4",24,1) // code, number of bits, protocol
