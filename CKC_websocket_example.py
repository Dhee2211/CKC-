#!/usr/bin/env python
#########################################################################################
# Cisco Kinetic for Cites Websocket Guide                                               #
# By: Dheerendra Panwar                                                                 #
# Description:  This is just an example to subscribe alerts from CKC using Websockets   #
#########################################################################################
import asyncio
import websockets
import json 

"""
    CKC's Device Engine supports the subscription to the User WebSocket where user can get notification for CRUD operation on models over which the users have access.
    wss://<server>/<tenant>/ deveng/ws/fid-CIMUserQueryInterfaceWS.<userId>

"""
uri = 'wss://ckc-preprod.cisco.com/sanjose.com/deveng/ws/fid-CIMUserQueryInterfaceWS.{userID}' <-------------------- (Enter your User ID here)

query={
 "Query":{
 "Storage":"TqlSubscription",
 "Save":{
 "TqlSubscription":{
 "Label":"SensorSubscription",
 "sid":"22",
 "Notify.Format":"all",
 "Notify.As":"$event:Model:Attribute",
 "Topic":"*.*",
 "MessageType":"json:compact"
 }
 }
 }
}

async def hello(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps(query))
        while True:
            print (await websocket.recv())
            print (" Data Recieved!!!")


asyncio.get_event_loop().run_until_complete(
    hello(uri))
    