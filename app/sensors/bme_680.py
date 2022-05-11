#!/usr/bin/env python3

import random

import board
import adafruit_bme680

from sensors.sensor import Sensor


class Bme680(Sensor):
    def __init__(self, name, test=False) -> None:
        super().__init__()
        self.name = name
        # Create sensor object, communicating over the board's default I2C bus
        i2c = board.I2C()  # uses board.SCL and board.SDA
        if not test:
            self.bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c,
                                                            address=0x76,
                                                            debug=True)
            self.bme680.sea_level_pressure = 1013
        self.temperature_offset = 0
        self.result = {
            "Temperature": float,
            "Air_Pollution": float,
            "Humidity": float,
            "Pressure": float
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

    def get_time(self, hour):
        if int(hour) >= 9 and int(hour) <= 18:
            return 'day'
        return 'night'

    def get_route_time(self, hour):
        # Pollution Highest 08:00-10:00, Medium 10:00-18:00, Highest 18:00-21:00, 21:00-08:00 Lowest
        if (int(hour) > 8 and int(hour) <= 10) or (int(hour) >= 18
                                                   and int(hour) <= 21):
            return 'highest'
        elif int(hour) > 10 and int(hour) < 18:
            return 'medium'
        return 'lowest'

    def get_custom_data(self, hour, location_type) -> dict:
        if location_type == 'B':
            if self.get_time(hour) == 'day':
                self.result["Temperature"] = 27 + (random.uniform(-0.5, 0.5))
            else:
                self.result["Temperature"] = 23 + (random.uniform(-0.5, 0.5))
            self.result["Pressure"] = 970 + (random.uniform(-10, 10))
            self.result["Air_Pollution"] = 37250 + (random.uniform(-50, 50))
            self.result["Humidity"] = 41.5 + (random.uniform(-0.5, 0.5))
        elif location_type == 'R':
            if self.get_time(hour) == 'day':
                self.result["Temperature"] = 26 + (random.uniform(-0.5, 0.5))
            else:
                self.result["Temperature"] = 22 + (random.uniform(-0.5, 0.5))
            route_time = self.get_route_time(hour)
            if route_time == 'highest':
                self.result["Air_Pollution"] = 44500 + (random.uniform(
                    -100, 100))
            elif route_time == 'medium':
                self.result["Air_Pollution"] = 42000 + (random.uniform(
                    -100, 100))
            else:
                self.result["Air_Pollution"] = 37400 + (random.uniform(
                    -100, 100))

            self.result["Pressure"] = 1020 + (random.uniform(-10, 10))
            self.result["Humidity"] = 37 + (random.uniform(-0.5, 0.5))
        elif location_type == 'H':
            if self.get_time(hour) == 'day':
                self.result["Temperature"] = 26 + (random.uniform(-0.5, 0.5))
            else:
                self.result["Temperature"] = 22 + (random.uniform(-0.5, 0.5))
            route_time = self.get_route_time(hour)
            if route_time == 'highest':
                self.result["Air_Pollution"] = 44500 + (random.uniform(
                    -100, 100))
            elif route_time == 'medium':
                self.result["Air_Pollution"] = 42000 + (random.uniform(
                    -100, 100))
            else:
                self.result["Air_Pollution"] = 37400 + (random.uniform(
                    -100, 100))

            self.result["Pressure"] = 1020 + (random.uniform(-10, 10))
            self.result["Humidity"] = 37 + (random.uniform(-0.5, 0.5))
        else:
            if self.get_time(hour) == 'day':
                self.result["Temperature"] = 24 + (random.uniform(-0.5, 0.5))
            else:
                self.result["Temperature"] = 22 + (random.uniform(-0.5, 0.5))
            self.result["Pressure"] = 960 + (random.uniform(-10, 10))
            self.result["Air_Pollution"] = 37250 + (random.uniform(-50, 50))
            self.result["Humidity"] = 38 + (random.uniform(-0.5, 0.5))
        return self.result
