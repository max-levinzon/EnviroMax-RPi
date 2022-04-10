#!/usr/bin/env python

import time
import random
import sys
import json

from pprint import pprint

from sensors.bme_680 import Bme680
from mock.mock_data import *
from data_handler.data import fireData
from data_handler.utils import get_latest_device
from device.device import Device


def main():
    with open('mock/device_locations.json') as f:
        dev_locations = json.load(f)
    mock_count = len(dev_locations.keys())
    db = fireData('EnviroMax')
    db.init_db()
    device_ref = db.db_instance.child('Devices')
    devices = mock_device(dev_locations, device_ref, reg_device=False)
    for device in devices.values():
        send_report(device, device_ref)
        time.sleep(5)
    # mock_data(devices, mock_count, 2, db)
    # For the mockup
    # 200 Devices
    # LONG - 34.786715 TO 34.837904
    # LAT - 32.053144 TO 32.125158
    return 0


if __name__ == "__main__":
    sys.exit(main())
