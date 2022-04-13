#!/usr/bin/env python

import sys
import json

from datetime import datetime
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
    sensor = Bme680('bme-sens')
    data = sensor.get_mock_data()
    print(data)
    now = datetime.now()
    db.send_data(device_data["name"], now.strftime("%d%m%Y%H"), data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
