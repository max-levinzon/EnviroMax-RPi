EnviroMax:  
RPi component with the BME-680 Sensor to send data into firebase with the following data:  

        Temperature - The sensor temperature in degrees Celsius.  
        Gas - The resistance (in Ohms) of the gas sensor.  This is proportional to the amount of VOC particles in the air (Air Pollution).  
        Humidity - The percent humidity as a value from 0 to 100%.  
        Pressure - The pressure in hPa.  
        Altitude - The altitude in meters.  

Usage:

    1. source enviro/bin/active
    2. pip install -r requirements.txt
    3. python setup.py

Crontab:
        Should run every 15 minuts
        Log from crontab can be found at /etc/var/syslog OR /var/mail/pi