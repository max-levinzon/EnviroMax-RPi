#!/usr/bin/env python3

import time
import pprint
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('/home/pi/.ssh/fireToken')
firebase_admin.initialize_app(
    cred, {
        'databaseURL':
        # 'https://test-67222-default-rtdb.europe-west1.firebasedatabase.app/'
        'https://enviromax-8ead5-default-rtdb.europe-west1.firebasedatabase.app/',
    })
ref = db.reference()
myData = ref.get()
pp = pprint.PrettyPrinter()
pp.pprint(myData)