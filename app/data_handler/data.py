from datetime import datetime

from dataclasses import dataclass
import firebase_admin
from firebase_admin import credentials, db, App, initialize_app

from .utils import CRED_LOCATION, DATABASE_URL, DATABASE_URL_TEST, CRED_LOCATION_TEST


@dataclass(init=True, repr=True)
class fireData:
    """Class to save all data from different sensors."""
    name: str
    # sens_data: dict = None
    dbURL: str = DATABASE_URL_TEST
    db_app: App = None
    db_instance: db.Reference = None

    def init_db(self):
        self.db_app: App = initialize_app(
            credential=credentials.Certificate(CRED_LOCATION_TEST),
            name=self.name,
            options={'databaseURL': self.dbURL})
        self.db_instance: db.Reference = db.reference(app=self.db_app)

    def get_app(self, name='EnviroMax'):
        return firebase_admin.get_app(name=name)

    def get_ref(self, path='/', url=None):
        return db.reference(path=path, app=self.db_app, url=url)

    def init_field(self, field: str):
        self.db_instance.push(field)

    def send_data(self, name: str, path: str, data: dict):
        ref = self.get_ref(path)
        # ref.child(f'{name}').child('data').child(record).update(data)
        # ref.child(f'{name}').child('data').child('lastData').update(data)
        ref.child(f'{name}').update(data)

    def get_latest_device(self):
        db = self.get_ref('Devices')
        device_count = db.get()
        if device_count:
            biggest_number = [
                int(k.removeprefix('RPi-')) for k in list(device_count.keys())
            ]
            biggest_number.sort()
            return biggest_number[-1]
        else:
            return 0

    def device_exist(self, device_ref):
        db = self.get_ref('Devices')
        device_count = db.get()
        return device_ref in device_count.keys()

    def get_next_count(self, device_ref):
        db = self.get_ref('Devices')
        device = db.child(device_ref).child('data').get()
        if device:
            return int(list(device.keys())[-2]) + 1
        else:
            return 1

    def register_new_device(self, device_details):
        db = self.get_ref('Devices')
        db.update({
            device_details["name"]: {
                'id': device_details["id"],
                'location': {
                    "lat": device_details["lat"],
                    "lng": device_details["lng"]
                },
                # 'data': ''
            }
        })
