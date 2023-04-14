#!/usr/bin/python3.10
import mido
import xair_api

kind_id = "XR18"
ip = "192.168.0.58"

mixer = xair_api.connect(kind_id, ip=ip)

myport = ""
mydevice = "X-TOUCH"

ports = mido.get_input_names()

for match in ports:
    print("checking ", match)
    if mydevice in match:
        myport = match
        print("will use ", myport)
        break
if ( myport == ""):
    print("no ", mydevice, ", exiting ...")
    exit()


with mido.open_input(myport) as inport:
    for msg in inport:
        msg = msg.dict()
        print(msg)


