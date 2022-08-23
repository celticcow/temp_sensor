#!/usr/bin/python3

import adafruit_dht
import time
import board

"""
from
https://medium.com/initial-state/how-to-build-a-raspberry-pi-temperature-monitor-8c2f70acaea9
init code
"""

# --------- User Settings ---------
SENSOR_LOCATION_NAME = "Office"
MINUTES_BETWEEN_READS = 10
METRIC_UNITS = False
# ---------------------------------

dhtSensor = adafruit_dht.DHT22(board.D4)
temp = 0.0

while True:
    try:
        humidity = dhtSensor.humidity
        temp_c = dhtSensor.temperature
        print(type(temp_c))
        print(type(humidity))
    except RuntimeError:
        print("RuntimeError, trying again...")
        continue

    if METRIC_UNITS:
        temp = temp_c
        #print(temp_c)
    else:
        temp_f = ((temp_c * 9.0) / 5.0) + 32.0
        temp = format(temp_f, ".2f")
    humidity = format(humidity,".2f")
    print(temp)
    print(humidity)
    break

    #time.sleep(60*MINUTES_BETWEEN_READS)
    
