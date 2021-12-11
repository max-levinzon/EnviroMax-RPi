#!/usr/bin/env python

import time
import sys
from pprint import pprint

from sensors.bme_680 import Bme680
from data_handler import data
from device.device import Device


def mock_data(device: Device, device_ref):
    device.send_data(device_ref)
    device.send_data(device_ref)
    device.send_data(device_ref)
    device.send_data(device_ref)


def main():
    db = data.fireData('EnviroMax')
    device_ref = db.db_instance.child('Devices')
    sensor = Bme680("bme_sens")
    device1 = Device()
    device2 = Device()
    device3 = Device()
    device1.add_sensor(sensor)
    device2.add_sensor(sensor)
    device3.add_sensor(sensor)
    device1.reg_new_device_db(device_ref)
    device2.reg_new_device_db(device_ref)
    device3.reg_new_device_db(device_ref)
    mock_data(device1, device_ref)
    mock_data(device2, device_ref)
    mock_data(device3, device_ref)
    # print(devices_path.get())
    # res = sensor.get_data()
    # pprint(res, compact=True)
    # db.send_data(res)


if __name__ == "__main__":
    sys.exit(main())
