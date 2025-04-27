#!/usr/bin/env python3

import requests

url = 'http://localhost/upload/'
with open('./supplier-datq/images/003.jpeg', 'rb') as opened:
    r = requests.post(url, files={'file': opened})
