#!/usr/bin/python3

import sys
import json
import paho.mqtt.client as mqtt
import asyncio
import bleak
from pymoof.clients.sx3 import Sound
from pymoof.clients.sx3 import SX3Client
from pymoof.tools import discover_bike
import configparser

config = configparser.RawConfigParser()
config.read('VM_MQTT.cfg')
config.sections()

#ToDo cleanup passwords
#MQTT Broker
BROKER = config.get('MQTT', 'BROKER')
BROKER_PORT = config.get('MQTT', 'BROKER_PORT')
BROKER_USER = config.get('MQTT', 'BROKER_USER')
BROKER_PW =  config.get('MQTT', 'BROKER_PW')
# other constants
# not required

async def bike_command(s3_command,encryption_key,key_id):
        print (s3_command)
        device = await discover_bike.query()
        try:    
            async with bleak.BleakClient(device) as bleak_client:
                client = SX3Client(bleak_client, encryption_key, key_id)
                await client.authenticate()
                frame_number = await client.get_frame_number()
                mclient.publish('Vanmoof/status', frame_number+' connected')
                if s3_command == 'GET_BATTERY_LEVEL':
                    mclient.publish('Vanmoof_S3/'+frame_number+'/battery',await client.get_battery_level() )
                if s3_command == 'DISTANCE_TRAVELLED':
                    mclient.publish('Vanmoof_S3/'+frame_number+'/mileage',await client.get_distance_travelled() )
                if s3_command == 'LOCK_STATE':
                    await client.authenticate()
                    mclient.publish('Vanmoof_S3/'+frame_number+'/lockstate',str(await client.get_lock_state()) )
                # tbc.....
        except Exception as e:
            print(e)
            mclient.publish('Vanmoof/status', 'bike not found')

class mqttClient:

    def __init__(self):
        #mclient = mqtt.Client('Vanmoof_S3')
        mclient.username_pw_set(BROKER_USER,BROKER_PW)
        mclient.connect(BROKER,BROKER_PORT)
        mclient.subscribe('Vanmoof_S3/in')
        mclient.on_message=self.on_message
        print("MQTT client connected")
        mclient.loop_forever()



    def on_close(self):
        self.live = False
        print("### Vanmoof MQTT disconnected ###")
        sys.exit(0)

    def on_message(client, userdata, any, message):
        print('mqtt_in', message.payload)
        jsPayload = json.loads(message.payload)
        s3_command = jsPayload['command']
        s3_enc_key = jsPayload['encryption_key']
        s3_key_id = jsPayload['key_id']
        mclient.publish('Vanmoof/status', s3_command+' received')
        asyncio.run(bike_command(s3_command,s3_enc_key,s3_key_id))
        


if __name__ == "__main__":
  
    mclient = mqtt.Client('Vanmoof_S3')
 
    MqttClient = mqttClient()


     

    
    
    
   
