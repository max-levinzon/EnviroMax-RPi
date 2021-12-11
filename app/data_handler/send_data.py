#!/usr/bin/env python3

import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('/home/pi/.ssh/fireToken')
firebase_admin.initialize_app(
    cred, {
        'databaseURL':
        # 'https://test-67222-default-rtdb.europe-west1.firebasedatabase.app/'
        'https://enviromax-8ead5-default-rtdb.europe-west1.firebasedatabase.app/'
    })
uid = 'RPi-2'
ref = db.reference()
user = ref.child('Devices')
user = user.child(uid) # Should be dynamic
user = user.child('Details')

data = {
    "ID": uid,
    "Name": "Netanya_Device",
    "Location": {
        "lat": 32.3081425,
        "lng": 34.8792939,
    },
}
user.push(data)
user = ref.child('Devices')
user = user.child(uid)
user = user.child('Data')
data = {
    "Temperaute": 29.3,
    "humidity": 42,
    "Date": time.asctime(), # timestamp -> send as a long
    "Location": { # No need for location
        "lat": 32.3081425,
        "lng": 34.8792939,
    },
}
user.push(data)
data = {
    "Temperaute": 34.6,
    "humidity": 38,
    "Date": time.asctime(), # timestamp -> send as a long
    "Location": { # No need for location
        "lat": 32.1127,
        "lng": 34.8792939,
    },
}
user.push(data)
#Herzliya_location
    # "lat": 32.1127,
    # "lng": 34.8159,

#Netanya_location
    # "lat": 32.3081425,
    # "lng": 34.8792939,