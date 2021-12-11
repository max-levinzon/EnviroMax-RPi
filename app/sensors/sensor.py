import itertools

import board


class Sensor:
    newid = itertools.count()

    def __init__(self) -> None:
        self.id = Sensor.newid.__next__()
        self.name = "sensor"
        # Create sensor object, communicating over the board's default I2C bus
        self.i2c = board.I2C()  # uses board.SCL and board.SDA

    def get_data():
        raise NotImplementedError()
