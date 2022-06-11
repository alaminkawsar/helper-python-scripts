import scipy.io as sio
import numpy as np
import os
import gc
import six.moves.urllib as urllib
import cv2
import time
import xml.etree.cElementTree as ET
import random
import shutil
from shutil import copyfile
import zipfile

import csv

"""
ORIGINAL SOURCE: https://github.com/molyswu/hand_detection/blob/temp/hand_detection/egohands_dataset_clean.py

I have cleaned up slightly, allowed for python3 functionality and some other things too:
   > using os.path.join instead of string1 + "/" + string2
   > ignores bounding boxes in original dataset where xmin = xmax or ymin=ymax
   > allows to choose a subset of the 40 subfolders of images.
"""


def download_egohands_dataset(dataset_url, dataset_path):
    print(os.path.join('1st','2nd'))

if __name__=="__main__":

    DATASET_URL = "INCLUDE_DATASET_URL"
    DATASET_FILE = "DATASET_NAME.zip"
    images_dir = 'images'

    download_egohands_dataset(DATASET_URL, DATASET_FILE)
