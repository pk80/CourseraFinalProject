#!/usr/bin/env python3

import requests
import os

url = 'http://localhost/upload/'
filesPath = './supplier-data/images'

for f in os.listdir(filesPath):
    if f.endswith('.jpeg'):
        with open(os.path.join(filesPath, f), 'rb') as opened:
            r = requests.post(url, files={'file': opened})
