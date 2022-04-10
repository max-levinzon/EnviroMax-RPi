#!/usr/bin/env python

import sys
import json
import time

from argparse import ArgumentParser

from data_handler.data import fireData
from sensors.bme_680 import Bme680


def main():
    parser = ArgumentParser()
    parser.add_argument('--iters', type=int)
    parser.add_argument('--time', type=int)
    args = parser.parse_args()
    db = fireData('EnviroMax')
    db.init_db()
    with open('/home/pi/EnviroMax-RPi/app/mock/device_locations.json',
              'r') as f:
        devices_data = json.load(f)
    print(devices_data)
    for device in devices_data.values():
        db.register_new_device(device)
    iterations = args.iters if args.iters else 1
    for _ in range(0, iterations):
        for device in devices_data.values():
            print(device)
            record = str(db.get_next_count(device['name']))
            sensor = Bme680('bme-sens')
            data = sensor.get_mock_data()
            db.send_data(device["name"], record, 'Devices', data)
        if args.time:
            time.sleep(args.time)
    return 0


if __name__ == "__main__":
    sys.exit(main())
