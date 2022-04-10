#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# GPIO SETUP
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

cred = credentials.Certificate('/home/pi/.ssh/fireToken')
firebase_admin.initialize_app(
    cred, {
        'databaseURL':
        # 'https://test-67222-default-rtdb.europe-west1.firebasedatabase.app/'
        'https://enviromax-8ead5-default-rtdb.europe-west1.firebasedatabase.app/'
    })
ref = db.reference()
temp = ref.child('Rpi-1')


def callback(channel):
    if GPIO.input(channel):
        print("Sound Detected !")
        data = {
            "Sound": "Sound Found!",
            "Date": time.asctime(),
        }
        temp.push(data)
    else:
        print("Sound Detected !")


GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)

while True:
    time.sleep(1)
