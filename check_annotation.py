#read csv to check image innotation
import cv2
from matplotlib import pyplot as plt
import csv

cnt = 1

# create figure
fig = plt.figure(figsize=(30, 30))

rows = 4
columns = 5

with open('/content/drive/MyDrive/R_Hagrid/test/test.csv','r') as file:
  read = csv.reader(file)

  for row in read:
    if('filename' in row[0]):
      continue

    #print(row)

    if 'dislike' not in row[3]:
      continue
    img_name = row[0].split('/')[-1];
    bbox = row[-4:]
    boxes = [int(x) for x in bbox];
    img_file = '/content/drive/MyDrive/R_Hagrid/test/dislike/'+img_name

    print(img_name, bbox)

    img = cv2.imread(img_file)
    cv2.rectangle(img, (boxes[0], boxes[1]), (boxes[2],boxes[3]), (255, 0, 0), 2)

    # Adds a subplot at the 2nd position
    fig.add_subplot(rows, columns, cnt)
    # showing image
    plt.imshow(img)
    plt.title("dislike")


    cnt +=1
    if cnt>=20:
      break;

