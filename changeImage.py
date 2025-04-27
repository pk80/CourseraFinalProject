#!/usr/bin/env python3

from PIL import Image
import os

path = './supplier-data/images/'
for f in os.listdir(path):
    if f.endswith('.tiff'):
        split_f = f.split('.')
        name = split_f[0] + '.jpeg'
        im = Image.open(path+f).convert('RGB')
        im.resize((600, 400)).save(path+name, 'JPEG')
