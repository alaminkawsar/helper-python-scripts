import os
dir = '/content/drive/MyDrive/CocoHandResnet50/COCO-Hand/COCO-Hand-S/COCO-Hand-S_Images'
list = os.listdir(dir) # dir is your directory path
number_files = len(list)
print (number_files)