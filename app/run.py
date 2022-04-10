#!/usr/bin/env python

import sys
import json

from data_handler.data import fireData
from sensors.bme_680 import Bme680


# Add timestamp !
def main():
    db = fireData('EnviroMax')
    db.init_db()
    with open('/home/pi/EnviroMax-RPi/app/.config', 'r') as f:
        device_data = json.load(f)
    print(device_data)
    if not db.device_exist(device_data['name']):
        print(f"ERROR !\nDevice not found {device_data['name']}")
    record = str(db.get_next_count(device_data['name']))
    print(record)
    sensor = Bme680('bme-sens')
    data = sensor.get_mock_data()
    print(data)
    db.send_data(device_data["name"], record, 'Devices', data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
