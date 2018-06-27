import os
import urllib.request as ulib
from urllib.request import Request, urlopen
import tempfile
from skimage import io
from matplotlib import pyplot as plt
from PIL import Image

headers = {'User-Agent': 'Chrome/41.0.2228.0 Safari/537.36'}

im = io.imread('https://upload.wikimedia.org/wikipedia/commons/c/ce/White_cup_of_black_coffee.jpg', headers)
img = Image.open(im)

f = tempfile.NamedTemporaryFile()
f.write(img)
print (type(f.read()))
print (f.name)
print (f.read())
#plt.imshow(f.read())
#plt.show()

f.close()
