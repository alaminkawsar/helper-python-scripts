import cv2
import matplotlib.pyplot as plt
import numpy as np
import random
import matplotlib.patches as patches
from pathlib import Path

'''Image Read'''
def read_image(path):
    im = cv2.imread(str(path))
    print(im.shape)
    return cv2.cvtColor(im, cv2.COLOR_BGR2RGB)


im = read_image('helper-python-scripts/Images/pikachu.jpg')
plt.imshow(im)
plt.show()
