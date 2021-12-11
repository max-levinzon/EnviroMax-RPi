from dataclasses import dataclass
import firebase_admin
from firebase_admin import credentials, db, App, initialize_app

from .utils import CRED_LOCATION, DATABASE_URL, DATABASE_URL_TEST


@dataclass(init=True, repr=True)
class fireData:
    """Class to save all data from different sensors."""
    name: str
    sens_data: dict = None
    # credentials: str = CRED_LOCATION
    dbURL: str = DATABASE_URL
    db_app: App = initialize_app(
        credential=credentials.Certificate(CRED_LOCATION), name="EnviroMax", options={'databaseURL': dbURL})
    db_instance: db.Reference = db.reference(app=db_app)
    db_instance.update({
        "Devices": "",
    })

    def print_all(self):
        print(self.__repr__)

    def get_app(self, name='[DEFAULT]'):
        return firebase_admin.get_app(name=name)

    def get_database(self, path='/', url=None):
        return db.reference(path=path, app=self.db_app, url=url)

    def init_field(self, field: str):
        self.db_instance.push(field)

    # def init_db(self):
    #     self.db_ref = firebase_admin.initialize_app(
    #         credentials.Certificate(self.credentials), {'databaseURL': self.dbURL})
    #     print(f"{self.db_ref.name} was initialized")

    def send_data(self, data: dict):
        pass
        # self.db_ref.child(self.id).push(dict)
        # ref = db.reference()
        # user = ref.child('Devices')
        # user = user.child(uid)  # Should be dynamic
        # user = user.child('Details')

        # data = {
        #     "ID": uid,
        #     "Name": "Netanya_Device",
        #     "Location": {
        #         "lat": 32.3081425,
        #         "lng": 34.8792939,
        #     },
        # }
        # user.push(data)

        # def main():
        #     data = {
        #         "ID": 'RPi-1',
        #         "Name": "Netanya_Device",
        #         "Location": {
        #             "lat": 32.3081425,
        #             "lng": 34.8792939,
        #         },
        #     }
        #     fd = fireData(1, 'RPi-1', 32.3081425, 34.8792939, data)
        #     fd.init_db()

        # if __name__ == "__main__":
        #     sys.exit(main())

        # uid = 'RPi-2'
        # ref = db.reference()
        # user = ref.child('Devices')
        # user = user.child(uid) # Should be dynamic
        # user = user.child('Details')

        # data = {
        #     "ID": uid,
        #     "Name": "Netanya_Device",
        #     "Location": {
        #         "lat": 32.3081425,
        #         "lng": 34.8792939,
        #     },
        # }
        # user.push(data)
        # user = ref.child('Devices')
        # user = user.child(uid)
        # user = user.child('Data')
        # data = {
        #     "Temperaute": 29.3,
        #     "humidity": 42,
        #     "Date": time.asctime(),
        #     "Location": {
        #         "lat": 32.3081425,
        #         "lng": 34.8792939,
        #     },
        # }
        # user.push(data)
