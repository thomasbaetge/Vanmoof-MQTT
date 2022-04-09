# Vanmoof-MQTT
MQTT integration of PYMOOF

This is based on Henri Bai's great work for the VM bluetooth API
https://github.com/quantsini/pymoof
Main credit goes to him!

this project provides a simple MQTT interface for the VM API, so it can be easily integrated into most automation systems via Node-Red.

What you need:

A Vanmoof bike (SX3, S2)...obviously..;)
A Linux machine running Python 3.8 or above (prefereably a Raspberry PI) in the vicinity of you bike (i.e. in the same room)
A MQTT-Broker like mosquitto (can be on the same machine or elsewhere)
A Node-Red installation (again: same machine or elsewhere)
The skills to run all of the above :)

How to start:
Install Python dependencies:
pip3 install bleak
pip3 install pymoof
pip3 install paho-mqtt

copy vm_mqtt.py and VM_MQTT.cfg into a directory of choice i.e. /home/pi/vanmoof or elsewhere
edit VM_MQTT according to your MQTT Broker's settings
make vm_mqtt.py executable by opening a termimal and type
sudo chmod +x vm_mqtt.py

for perament use, you may want to setup the program to run as a systemd service.
if you don't know how to do it, you can follow this guide:
https://medium.com/codex/setup-a-python-script-as-a-service-through-systemctl-systemd-f0cc55a42267

if you get bluetooth permission errors, you need to add you user to the bluetooth group:
sudo adduser <user> bluetooth
and reboot for the changes to take effect.

You will need your bikes encryption key, the key_id and the bike's frame number, so you need to retrieve it once from the VM server. In order to get that and verify that you installed all dependencies properly, rund the attached sample.py which is a copy of Henri's sample program.

if all goes well and the programm is up and running, you can then set up your own Node-Red flow for communication with your bike.
You can start by importing the sample flow and play with it.



