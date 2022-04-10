#!/usr/bin/env python3

import random

import board
import adafruit_bme680

from sensors.sensor import Sensor


class Bme680(Sensor):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        # Create sensor object, communicating over the board's default I2C bus
        i2c = board.I2C()  # uses board.SCL and board.SDA
        # FIX IT !!!
        # self.bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c,
        #                                                   address=0x77,
        #                                                   debug=True)
        # self.bme680.sea_level_pressure = 1013
        self.temperature_offset = 0
        self.result = {
            "Temperature": int,
            "Air_Pollution": int,
            "Humidity": int,
            "Pressure": int
        }

    def get_data(self) -> dict:
        """
        duration = for how long to read data
        return = dict with duration data
        """
        self.result["Temperature"] = self.bme680.temperature + \
                self.temperature_offset
        self.result["Air_Pollution"] = self.bme680.gas
        self.result["Humidity"] = self.bme680.relative_humidity
        self.result["Pressure"] = self.bme680.pressure
        return self.result

    def get_mock_data(self) -> dict:
        min_value = -0.1
        max_value = 0.2
        self.result["Temperature"] = 24 + \
                (24 * random.uniform(min_value, max_value))
        self.result["Air_Pollution"] = 40000 + \
            (40000 * random.uniform(min_value, max_value))
        self.result["Humidity"] = 38 + \
            (38 * random.uniform(min_value, max_value))
        self.result["Pressure"] = 1000 + \
            (1000 * random.uniform(min_value, max_value))
        return self.result