import random

from device.device import Device

# TODO - take real location
MIN_LNG = 34.7969528
MIN_LAT = 32.0567447

MAX_LNG = 34.837904
MAX_LAT = 32.125158


def send_mock_data(device, db, data):
    device.metadata['count'] = device.metadata['count'] + 1

    db.child(f'RPi-{device.id}').child('metadata').update(
        {'count': device.metadata['count']})
    lastData = data
    db.child(f'RPi-{device.id}').child('data').child(
        f'{device.metadata["count"]}').update(lastData)
    db.child(f'RPi-{device.id}').child('data').child('lastData').update(
        lastData)


def mock_data(devices, mock_count, entries, db):
    # Temp -> +-3
    # Pressure -> 100 (10%)
    # Air Pollution -> 40000
    # Humidity -> 5
    result = {
        "Temperature": int,
        "Air_Pollution": int,
        "Humidity": int,
        "Pressure": int
    }
    min_value = -0.1
    max_value = 0.2
    for x in range(1, mock_count + 1):
        for i in range(0, entries):
            result["Temperature"] = 24 + \
                (24 * random.uniform(min_value, max_value))
            result["Air_Pollution"] = 40000 + \
                (40000 * random.uniform(min_value, max_value))
            result["Humidity"] = 38 + \
                (38 * random.uniform(min_value, max_value))
            result["Pressure"] = 1000 + \
                (1000 * random.uniform(min_value, max_value))
            print(f'For device{x} data is {result}')
            send_mock_data(devices[f'device{x}'], db, result)


def send_report(device, db):
    result = {
        "Temperature": int,
        "Air_Pollution": int,
        "Humidity": int,
        "Pressure": int
    }
    min_value = -0.1
    max_value = 0.2
    result["Temperature"] = 24 + (24 * random.uniform(min_value, max_value))
    result["Air_Pollution"] = 40000 + (40000 *
                                       random.uniform(min_value, max_value))
    result["Humidity"] = 38 + (38 * random.uniform(min_value, max_value))
    result["Pressure"] = 1000 + (1000 * random.uniform(min_value, max_value))
    send_mock_data(device, db, result)


def mock_device(data, device_ref, reg_device=True):
    devices = {}
    length = len(data.keys()) + 1
    for i in range(1, length):
        lat = data[f'{i}']['lat']
        lng = data[f'{i}']['lng']
        print(f'Creating device number: {i} in location: {lat},{lng}')
        devices[f'device{i}'] = Device(lat, lng)
        if reg_device:
            devices[f'device{i}'].reg_new_device_db(device_ref)
    return devices
