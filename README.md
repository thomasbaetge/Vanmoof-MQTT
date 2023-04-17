# Vanmoof-MQTT
MQTT integration of PYMOOF

UPDATE 2023: As I no longer have a VM bike and don't plan on buying any more of their products, this repo is discontinued.
It will still work, but I can only provide limieted assistance.

Disclaimer:  
whatever you do with this, is on yourself. I am not reliable for exploding bikes or any other trouble you get yourself into.  

This is based on Henri Bai's great work for the VM bluetooth API  
https://github.com/quantsini/pymoof  
Main credit goes to him!

this project provides a simple MQTT interface for the VM API, so it can be easily integrated into most automation systems via Node-Red.  

What it can do:  
- retrieve battery level  
- retrieve current mileage  
- retrieve lock state  

...more to come as we may need it...  

Limitations:  
this will only work for one bike by current restriction of the API. If you happen to have more VM bikes, only one will work. I may look into that later. 

What you need:

- A Vanmoof bike (S3, X3)...obviously..;)
- A Linux machine running Python 3.8 or above (prefereably a Raspberry PI) in the vicinity of you bike (i.e. in the same room)  
- A MQTT-Broker like mosquitto (can be on the same machine or elsewhere)  
- A Node-Red installation (again: same machine or elsewhere)  
- The skills to run all of the above :)  

How to start:  
Install Python dependencies:  
- pip3 install bleak    
- pip3 install pymoof  
- pip3 install paho-mqtt  
- pip3 install json  

- copy vm_mqtt.py and VM_MQTT.cfg into a directory of choice i.e. /home/pi/vanmoof or elsewhere  
- edit VM_MQTT.cfg according to your MQTT Broker's settings  
- make vm_mqtt.py executable by opening a termimal and type sudo chmod +x vm_mqtt.py  

for perament use, you may want to setup the program to run as a systemd service.
if you don't know how to do it, you can follow this guide:
https://medium.com/codex/setup-a-python-script-as-a-service-through-systemctl-systemd-f0cc55a42267

if you get bluetooth permission errors, you need to add you user to the bluetooth group:  
sudo adduser <user> bluetooth  
and reboot for the changes to take effect.

You will need your bikes encryption key, the key_id and the bike's frame number, so you need to retrieve it once from the VM server. In order to get that and verify that you installed all dependencies properly, run the sample program. that will also verify your install is okay (if this goes belly up, the main program will most likely too)  

if all goes well and the programm is up and running, you can then set up your own Node-Red flow for communication with your bike.
You can start by importing the sample flow and play with it.

MQTT Topics:
- Vanmoof_S3/in (Receives commands along with enc key and key_id)
- Vanmoof/status (gives status information and errors, i.e. if your bike is not present)
- Vanmoof_S3/<framenumber>/battery
- Vanmoof_S3/<framenumber>/mileage
- Vanmoof_S3/<framenumber>/lockstate  
  ...do exactly what the topics suggest ;)  
  
 Suggestions for usage:  
it's kinda useless...I did it anyway.



