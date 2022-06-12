import cv2
import numpy as np


# read image
img = cv2.imread('/home/kawsar/Desktop/Deep Learning/helper-python-scripts/draw_bounding_box.jpg')

# convert to grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# threshold
thresh = cv2.threshold(gray,128,255,cv2.THRESH_BINARY)[1]


# get contours
result = img.copy()
contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]
for cntr in contours:
    x,y,w,h = cv2.boundingRect(cntr)
    cv2.rectangle(result, (x, y), (x+w, y+h), (0, 0, 255), 2)
    print("x,y,w,h:",x,y,w,h)
 
# save resulting image
cv2.imwrite('two_blobs_result.jpg',result)      

# show thresh and result    
cv2.imshow("bounding_box", result)
cv2.waitKey(0)
cv2.destroyAllWindows()