from PIL import Image
import requests
from io import BytesIO
from matplotlib import pyplot as plt
import argparse
import numpy as np
import cv2
import base64
from skimage import io 
from urllib.request import Request, urlopen
import os

headers = {'User-Agent': 'Chrome/41.0.2228.0 Safari/537.36'}

parser = argparse.ArgumentParser()
parser.add_argument("impath", help="insert the path to url")
parser.add_argument( "-i" ,"--path", action="store_true" , help="insert the path to url")

args =parser.parse_args()

url = args.impath

#req = Request(url, headers = {'User-Agent': 'Mozilla/5.0'} )
#img = urlopen(req).read()

#img = io.imread(url, headers)

response = requests.get(url, headers)

print (type(response.content))

img =Image.open(BytesIO(response.content))
#img_str =base64.b64encode(img.getvalue())
print (img.filename)
print (type(img))

#print(type(img))
#plt.imshow(img)
#plt.show()