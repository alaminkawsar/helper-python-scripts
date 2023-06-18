import os
import csv
from turtle import heading
import cv2
import matplotlib.pyplot as plt
from PIL import Image
import shutil


img_directory_path='/content/drive/MyDrive/tv+coco_hand/TV-Hand/TV-Hand_Images'
test_img_dir = '/content/drive/MyDrive/tv+coco_hand/images/test'

text_file_path = '/content/drive/MyDrive/tv+coco_hand/TV-Hand'
text_file_name = "test_IDs.txt"

add_path = 'images/test/'

csv_file_path = '/content/drive/MyDrive/tv+coco_hand/images/test'
csv_file_name = 'test_labels.csv'

list2d = []
indx = 0
list2d.append(['filename','width','height','class','xmin','ymin','xmax','ymax'])

listSize = {
    
}

k = 0
filepath = os.listdir(img_directory_path)
for x in filepath:
    img = Image.open(os.path.join(img_directory_path,x))
    width, height = str(img.width), str(img.height)
    listSize[x] = [width, height]
    #print(x, listSize[x])


#please comment here
    # if k ==10:
    #   break
    # k +=1

#pleae comment here
# listSize['000074_006.jpg'] = ['100','100']
# listSize['000204_005.jpg'] = ['100','100']

copy_img_list = {
    
}
k = 0
with open(os.path.join(text_file_path,text_file_name), "r") as f:
    for line in f.readlines():
        if line[-1]=='\n' :
            line = line[:-1]
        new_val = line.split(',')
        img_name_path = new_val[0]

        #process xmin,ymin,xmax,ymax
        find_val = list(map(int,new_val[1:5]))
        find_val[1], find_val[2] = find_val[2], find_val[1]

        #process name
        img_name = img_name_path.split('/')[-1]
        img_file_path = [add_path + img_name]

        if '-1' in find_val:
          continue

        if img_name in listSize.keys():
          v = img_file_path + listSize[img_name] + ['hand'] + find_val
          print(v)
          
          copy_img_list[img_name] = 1
          list2d.append(v)

        #please comment
        # else:
        #   print(img_name, find_val)

        # k += 1
        # if k==20: 
        #   break


with open(os.path.join(csv_file_path,csv_file_name), 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(list2d)

#move image file into test/train directory
k = 0
check_exist = {}

for x in filepath:
    img = Image.open(os.path.join(img_directory_path,x))
    old_dir = os.path.join(img_directory_path,x)
    new_dir = os.path.join(test_img_dir,x)
    if new_dir in check_exist.keys():
      continue
    #print(old_dir, new_dir)
    if x in copy_img_list.keys():
      shutil.copyfile(old_dir,new_dir)
      check_exist[x] = True

    
    # print(x)
    # if k ==10:
    #   break
    # k +=1
print('successfully shifted and created csv file')
