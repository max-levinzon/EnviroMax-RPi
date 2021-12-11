#!/usr/bin/env python3

import time
import geocoder
from pprint import pprint

import board
import adafruit_bme680

from sensors.sensor import Sensor


class Bme680(Sensor):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        # Create sensor object, communicating over the board's default I2C bus
        # i2c = board.I2C()  # uses board.SCL and board.SDA
        self.bme680 = adafruit_bme680.Adafruit_BME680_I2C(
            self.i2c, address=0x76, debug=False)
        self.bme680.sea_level_pressure = 1013
        self.temperature_offset = 0
        self.result = {"Temperature": int, "Air_Pollution": int,
                       "Humidity": int, "Pressure": int}

    def get_data(self, duration: int = 5) -> dict:
        """
        duration = for how long to read data
        return = dict with duration data
        """
        timeout = time.time() + duration
        while True:
            self.result["Temperature"] = self.bme680.temperature + \
                self.temperature_offset
            self.result["Air_Pollution"] = self.bme680.gas
            self.result["Humidity"] = self.bme680.relative_humidity
            self.result["Pressure"] = self.bme680.pressure
            # self.result["Altitude"].append(self.bme680.altitude)
            if time.time() > timeout:
                return self.result
            time.sleep(1)


# def main():
#     sens = Bme680("test")
#     res = sens.get_data()
#     # print(f'from {sens.name} results for default duration:\n{res}')
#     # pprint(f'from {sens.name} results for default duration:\n{res}', compact=True)
#     pprint(res, compact=True)


# if __name__ == "__main__":
#     sys.exit(main())
