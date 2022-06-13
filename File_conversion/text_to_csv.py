import os
import csv
from turtle import heading
import cv2
import matplotlib.pyplot as plt
from PIL import Image



path = '/home/kawsar/Desktop/Deep Learning/helper-python-scripts'
list2d = []
img_path='/home/kawsar/Desktop/Deep Learning/helper-python-scripts/Images'
indx = 0
list2d.append(['filename','width','height','class','xmin','ymin','xmax','ymax'])
listSize = {
    
}
filepath = os.listdir(img_path)
for x in filepath:
    img = Image.open(os.path.join(img_path,x))
    width, height = str(img.width), str(img.height)
    listSize[x] = [width, height]

with open(os.path.join(path,"text_file.txt"), "r") as f:
    for line in f.readlines():
        if line[-1]=='\n' :
            line = line[:-1]
        new_val = line.split(',')
        
        if new_val[0] in listSize.keys():
            width_height = listSize[new_val[0]]
        else:
            continue
        
        new_val[2], new_val[3] = new_val[3], new_val[2]
        new_val = ['images/test/'+new_val[0]] + width_height+ ['hand'] + new_val[1:5]
        
        #print(new_val)
        list2d.append(new_val)


with open(os.path.join(path,'images/test/test.csv'), 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(list2d)
    