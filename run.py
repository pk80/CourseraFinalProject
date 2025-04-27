#!/usr/bin/env python3

import os
import requests

fruits = {}
keys = ['name', 'weight', 'description', 'image_name']
index = 0
descPath = './supplier-data/descriptions'
imagePath = './supplier-data/images'

upload_url = 'http://localhost/fruits/'

for file in os.listdir(descPath):
    with open(os.path.join(descPath, file), 'r') as f:
        for ln in f:
            line = ln.strip()
            if 'lbs' in line:
                nline = line.split()
                wght = nline[0]
                fruits['weight'] = wght
                index += 1
            else:
                try:
                    fruits[keys[index]] = line
                    index += 1
                except:
                    fruits[keys[2]] = line
        index = 0
        split_f = file.split('.')
        name = split_f[0] + '.jpeg'
        for fl in os.listdir(imagePath):
            if fl == name:
                fruits['image_name'] = name
        response = requests.post(upload_url, json=fruits)
        fruits.clear()
