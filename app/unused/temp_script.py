#!/usr/bin/env python3
import json

tmp = ''
locations = {'Route': 'R', 'Jaffa Park': 'P', 'Beach': 'B', 'Hazard': 'H'}
new_devices = {}
count = 1
with open('/home/pi/EnviroMax-RPi/app/new_locations.txt', 'r') as f:
    lines = f.readlines()
    for i in lines:
        i = i.strip()
        if i in locations.keys():
            tmp = locations[i]
        else:
            lat, lng = i.split(", ")[0], i.split(", ")[1]
            new_devices[f"{count}"] = {
                "id": count,
                "name": f"RPi-{count}",
                "lat": lat,
                "lng": lng,
                "area": tmp
            }
            count = count + 1

with open("/home/pi/EnviroMax-RPi/app/locations_mock_devices.json", 'w') as f:
    json.dump(new_devices, f, indent=4)
