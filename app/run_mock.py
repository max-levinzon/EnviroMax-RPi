#!/usr/bin/env python

import sys
import json
import time

from datetime import datetime, timedelta
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
    with open('/home/pi/EnviroMax-RPi/app/mock/locations_mock_devices.json',
              'r') as f:
        devices_data = json.load(f)
    for device in devices_data.values():
        device["lat"] = float(device["lat"])
        device["lng"] = float(device["lng"])
        db.register_new_device(device)
    iterations = args.iters if args.iters else 1
    print("Starting to send data")
    # for _ in range(0, iterations):
    for i in range(1, 26):
        delta = 26 - i
        for device in devices_data.values():
            sensor = Bme680('bme-sens', test=True)
            delta_time = datetime.now() - timedelta(hours=delta)
            time_to_send = delta_time.strftime("%d%m%Y%H")
            data = sensor.get_custom_data(delta_time.strftime("%H"),
                                          device["area"])
            db.send_data(device["name"], f'data/{time_to_send}', data)
        if args.time:
            print(f'Sleeping for {args.time}')
            time.sleep(args.time)
    return 0


if __name__ == "__main__":
    sys.exit(main())
