import json

from datetime import datetime

from data_handler.utils import DATABASE_URL_TEST
from data_handler.data import fireData
from sensors.bme_680 import Bme680


def connect_to_db():
    db = fireData('EnviroMax', dbURL=DATABASE_URL_TEST)
    db.init_db(test=True)
    return db


def get_db():
    return fireData('EnviroMax', dbURL=DATABASE_URL_TEST)


def get_device():
    with open('/home/pi/EnviroMax-RPi/app/.config', 'r') as f:
        device_data = json.load(f)
    return device_data


def get_multiple_devices():
    with open('/home/pi/EnviroMax-RPi/app/range_mock_devices.json', 'r') as f:
        devices_data = json.load(f)
    return devices_data


def create_sensor():
    sensor = Bme680('bme-sens')
    return sensor


def handle_data(db, device_data, sensor):
    data = sensor.get_mock_data()
    now = datetime.now()
    return db.send_data(device_data["name"],
                        f'data/{now.strftime("%d%m%Y%H")}', data)


def handle_multiple_data(db, devices_data):
    for device in devices_data.values():
        sensor = Bme680(f'bme-sens-{device["id"]}')
        data = sensor.get_mock_data()
        now = datetime.now()
        db.send_data(device["name"], f'data/{now.strftime("%d%m%Y%H")}', data)
    return 1


def read_data(data):
    valid_keys = {
        'Air_Pollution': int,
        'Humidity': int,
        'Pressure': int,
        'Temperature': int
    }
    for k, v in data.items():
        if v.keys() != valid_keys.keys():
            return 0
    return 1


db = connect_to_db()


def test_sanity():
    device = get_device()
    sensor = create_sensor()
    assert handle_data(db, device, sensor)


def test_multiple_devices():
    devices = get_multiple_devices()
    assert handle_multiple_data(db, devices)


def test_data():
    ref = db.get_ref(path='data')
    last_entry = list(ref.get(shallow=True).keys())[0]
    last_data = ref.child(path=last_entry).get()
    assert read_data(last_data)
