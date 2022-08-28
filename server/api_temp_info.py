#!/usr/bin/python3

import requests
import json
import time

from flask import Flask, request

app = Flask(__name__)

@app.route('/sensor_report', methods=['POST'])
def sensor_report():
    debug = 1
    if(debug == 1):
        print("in report")

    sensor_name = "unknown"
    temp = "unknown"
    humidity = "unknown"

    sensor_info = request.get_json(force=True)

    try:
        sensor_name = sensor_info['sensor_name']
        temp = sensor_info['temp']
        humidity = sensor_info['humidity']
    except:
        print("issue getting fields")
    
    if(debug == 1):
        print(sensor_name)
        print(temp)
        print(humidity)
    
    return({"result" : "success"})
#end of sensor_report

@app.route('/')
def root():
    print("in root call")
    return({"root" : "generic message"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
#end of program