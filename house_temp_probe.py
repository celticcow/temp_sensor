#!/usr/bin/python3

import adafruit_dht
import time
import board


def get_sensor_info(location_name):
    debug = 1
    print("getting location " + location_name)

    ## PI4 is using GPIO4 on pin 7
    dhtSensor = adafruit_dht.DHT22(board.D4)
    temp = 0.0
    humidity = 0.0

    while(True):
        try:
            humidity = dhtSensor.humidity
            temp_c = dhtSensor._temperature
            if(debug == 1):
                print(type(temp_c))
                print(type(humidity))

                print(temp_c)
                print(humidity)
        except RuntimeError:
            print("run time error ... trying again ...")
            continue

        temp_f = ((temp_c * 9.0) / 5.0) + 32.0
        
        temp = format(temp_f, ".2f")
        humidity = format(humidity, ".2f")

        print(temp)
        print(humidity)
        break

#end of get_sensor_info

def main():
    debug = 1

    get_sensor_info("office")
    

if __name__ == "__main__":
    main()
#end 