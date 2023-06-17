from PIL import Image
import os
 
folder = '/home/kawsar/Desktop/Deep Learning/helper-python-scripts/Images'
w = 1000
h = 980
for i in os.listdir(folder):
    file = os.path.join(folder,i)
    print(file)
    im = Image.open(file)
    im = im.resize((w, h), Image.ANTIALIAS)
    im.save(file)