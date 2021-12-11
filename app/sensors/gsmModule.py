#!/usr/bin/env python3
import serial
import RPi.GPIO as GPIO
import os
import time

GPIO.setmode(GPIO.BOARD)
port = serial.Serial("/dev/serial0", baudrate=9600, timeout=1)
port.flush()
# port.write(("AT\r\n").encode())
# rcv = port.read(10)
# print(rcv)
# time.sleep(1)

command = b"AT+CGATT = 1"
port.write(b"$")
port.write(command)
port.write(b"\r\n")
# port.write("".encode())  # Disable the Echo
print(port.read(10))
rcv = port.read(10)
print(rcv)
time.sleep(1)

# port.write("AT+CMGF=1\r\n".encode())  # Select Message format as Text mode
# rcv = port.read(10)
# print(rcv)
# time.sleep(1)

# port.write("AT+CNMI=2,1,0,0,0\r\n".encode())  # New SMS Message Indications
# rcv = port.read(10)
# print(rcv)
# time.sleep(1)
