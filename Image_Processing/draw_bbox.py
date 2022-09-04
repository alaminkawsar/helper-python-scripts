#!/usr/bin/env python
from ast import arg
import cv2
import sys

def drawBoundingBoxes(imageData, imageOutputPath, inferenceResults, color):
    """Draw bounding boxes on an image.
    imageData: image data in numpy array format
    imageOutputPath: output image file path
    inferenceResults: inference results array off object (l,t,w,h)
    colorMap: Bounding box color candidates, list of RGB tuples.
    """
    for res in inferenceResults:
        left = int(res['left'])
        top = int(res['top'])
        right = int(res['left']) + int(res['width'])
        bottom = int(res['top']) + int(res['height'])
        label = res['label']
        imgHeight, imgWidth, _ = imageData.shape
        thick = int((imgHeight + imgWidth) // 900)
        print (left, top, right, bottom)
        cv2.rectangle(imageData,(left, top), (right, bottom), color, thick)
        cv2.putText(imageData, label, (left, top - 12), 0, 1e-3 * imgHeight, color, thick//3)
    cv2.imwrite(imageOutputPath, imageData)

def main(imagePath, left, top, width, height, label):
    imgcv = cv2.imread(imagePath)
    print(imgcv.shape)
    color = (0,255,0)
    results = [
        {
            "left": left,
            "top": top,
            "width": width,
            "height": height,
            "label": label
        }
    ]
    drawBoundingBoxes(imgcv, './output.png', results, color)

if __name__ == "__main__":
    #argv = sys.argv
    path = '/home/kawsar/Desktop/Deep Learning/helper-python-scripts/Image_Processing/images/000204_005.jpg'
    xmin, xmax, ymin, ymax = 71,87,89,109
    
    #xmin,ymin,width,height
    argv = ['',path,xmin,ymin,xmax-xmin,ymax-ymin,'handDetected']
    print (argv)
    main(argv[1], argv[2], argv[3], argv[4], argv[5], argv[6])