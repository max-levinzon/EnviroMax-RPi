#!/usr/bin/env python

import sys
import geocoder
import json
import os

from crontab import CronTab

from data_handler.data import fireData


def main():
    db = fireData('EnviroMax')
    db.init_db(test=True)
    latest_device = db.get_latest_device() + 1
    device_details = {
        'id': latest_device,
        'name': f'RPi-{latest_device}',
        'lat': geocoder.ip('me').lat,
        'lng': geocoder.ip('me').lng
    }
    with open(".config", 'w') as f:
        json.dump(device_details, f)
    # Register the new device in the database
    db.register_new_device(device_details)
    # Add node_exporter monitoring
    os.system('sudo ./apts/node_exporter_installer.sh')
    # Trigger another script to run and send data each hour
    crontab = CronTab(user='pi')
    job = crontab.new(
        command=
        '/home/pi/EnviroMax-RPi/enviro/bin/python3 /home/pi/EnviroMax-RPi/app/run.py'
    )
    job.minute.every(60)

    crontab.write()
    return 0


if __name__ == "__main__":
    sys.exit(main())
