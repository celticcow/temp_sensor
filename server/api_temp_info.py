#!/usr/bin/python3

import requests
import json
import time

from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def root():
    print("in root call")
    return({"root" : "generic message"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
#end of program