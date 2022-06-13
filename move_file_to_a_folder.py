import shutil
import os

'''We can move each file(images,text,any types) using shutil.

syntax: shutil.move(old_directory,new_directory)

'''

'''Type-1'''
# old = '/home/kawsar/Desktop/Deep Learning/helper-python-scripts/folder1/000000000036.jpg'
# new = '/home/kawsar/Desktop/Deep Learning/helper-python-scripts/folder2/000000000036.jpg'
# shutil.move(old, new)


'''Type-2'''

#os.listdir() list all of file in a current directory
images = [f for f in os.listdir() if '.jpg' or '.png' in f.lower()]
print(images)


os.mkdir('downloaded_images')

for image in images:
    new_path = 'downloaded_images/' + image
    shutil.move(image, new_path)