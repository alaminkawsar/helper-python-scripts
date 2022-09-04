import os
import csv
from turtle import heading
import cv2
import matplotlib.pyplot as plt
from PIL import Image
import shutil
import random



img_directory_path='/content/drive/MyDrive/HandGestureCenterNet/COCO-Hand/COCO-Hand-Big/COCO-Hand-Big_Images'
test_img_dir = '/content/drive/MyDrive/HandGestureCenterNet/images/test'
train_img_dir = '/content/drive/MyDrive/HandGestureCenterNet/images/train'

text_file_path = '/content/drive/MyDrive/HandGestureCenterNet/COCO-Hand/COCO-Hand-Big'
text_file_name = "COCO-Hand-Big_annotations.txt"

add_path = 'images/test/'

csv_file_path = '/content/drive/MyDrive/HandGestureCenterNet/images/test'
csv_file_name = 'test_labels.csv'

list2d = []
indx = 0
#list2d.append(['filename','width','height','class','xmin','ymin','xmax','ymax'])

listSize = {
    
}

k = 0
filepath = os.listdir(img_directory_path)
for x in filepath:
    img = Image.open(os.path.join(img_directory_path,x))
    width, height = str(img.width), str(img.height)
    listSize[x] = [width, height]
    #print(x, listSize[x])


#please comment here bellow
    if k ==50:
      break
    k +=1

#pleae comment here
# listSize['000074_006.jpg'] = ['100','100']
# listSize['000204_005.jpg'] = ['100','100']
#images/train/000011_004.jpg

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
        x_val = list(map(int,new_val[5:13]))
        y_val = [x_val[i] for i in range(0,8) if i%2==1]
        x_val = [x_val[i] for i in range(0,8) if i%2==0]

        if min(x_val) == -1:
          continue

        xy = [min(x_val),min(y_val),max(x_val),max(y_val)]
        
        find_val = xy

        #process name
        img_name = img_name_path.split('/')[-1]        

        #v = img_file_path + listSize[img_name] + ['hand'] + find_val
        v = [img_name] + ['hand'] + find_val
        #print(v)
        list2d.append(v)
        
        '''
        if img_name in listSize.keys():
          v = img_file_path + listSize[img_name] + ['hand'] + find_val
          print(v)
          
          copy_img_list[img_name] = 1
          list2d.append(v)

        #please comment bellow
        else:
          print(img_name, find_val)
          print(img_name,xy)
          print(x_val,y_val)
        '''

        k += 1
        if k==20: 
          break

random.shuffle(list2d)

k = 0
test_list = []
test_vis = {
    
}

train_list = []
train_vis = {
    
}

test_list.append(['filename','width','height','class','xmin','ymin','xmax','ymax'])
train_list.append(['filename','width','height','class','xmin','ymin','xmax','ymax'])


#need to change
for x in list2d:
  if k<10:
    v = ['images/test/'+x[0]] + x[1:]
    #print(v)
    test_list.append(v)
    test_vis[x[0]] = True

  else:
    v = ['images/train/'+x[0]] + x[1:]
    #print(v)
    train_list.append(v)
    train_vis[x[0]] = True
    
  k += 1
  

for x in train_list:
  print(x)

test_csv_file_path = '/content/drive/MyDrive/HandGestureCenterNet/images/test'
test_csv_file_name = 'test_labels.csv'

train_csv_file_path = '/content/drive/MyDrive/HandGestureCenterNet/images/train'
train_csv_file_name = 'train_labels.csv'



# with open(os.path.join(test_csv_file_path ,test_csv_file_name), 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(test_list)

# with open(os.path.join(train_csv_file_path,train_csv_file_name), 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(train_list)


# move image file into test/train directory
k = 0
check_exist = {}

filepath = os.listdir(img_directory_path)

for x in filepath:
    img = Image.open(os.path.join(img_directory_path,x))
    old_dir = os.path.join(img_directory_path,x)

    if x in check_exist.keys():
      continue
    
    check_exist[x] = True
    
    path_select = test_img_dir
    if x in train_vis.keys:
      path_select = train_img_dir
    elif x in test_vis:
      path_select = test_img_dir
    else:
      continue
    

    new_dir = os.path.join(path_select,x)

    if new_dir in check_exist.keys():
      continue
    print(old_dir, new_dir)
    if x in copy_img_list.keys():
      #shutil.copyfile(old_dir,new_dir)
      check_exist[x] = True

    
    #print(x)
    if k ==10:
      break
    k +=1
print('successfully shifted and created csv file')



