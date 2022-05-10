import geocoder
import itertools
import time

from sensors.bme_680 import Bme680


class Device:
    newid = itertools.count(1)

    def __init__(self, lat, lng) -> None:
        self.id = Device.newid.__next__()
        self.name = f'RPi-{self.id}'
        self.lat = lat  # geocoder.ip('me').lat
        self.lng = lng  # geocoder.ip('me').lng
        self.location = {"lat": self.lat, "lng": self.lng}
        self.sensors = {}
        self.metadata = {'count': 0, 'highest': 0, 'average': 0}

    def add_sensor(self, sensor):
        print(f'Adding {sensor.name} to {self.name} device !')
        self.sensors[sensor.name] = sensor

    def get_sensor(self, sensor_name):
        if sensor_name in self.sensors.keys():
            return self.sensors[sensor_name]
        else:
            raise SensorNotFoundException()

    def print_available_sensors(self):
        print(self.sensors.keys())

    def reg_new_device_db(self, db):
        db.update(
            {self.name: {'id': self.id, 'location': self.location, 'data': '', 'metadata': self.metadata}})

    def send_data(self, db):
        lastData = self.sensors["bme_sens"].get_data(1)
        db.child(
            f'RPi-{self.id}').child('data').child(time.asctime()).update(lastData)
        db.child(
            f'RPi-{self.id}').child('data').child('lastData').update(lastData)


class SensorNotFoundException(Exception):
    pass
