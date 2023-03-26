#!/usr/bin/python3
import mido

myport = ""
mydevice = "nanoKONTROL2"

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
        print(msg)


