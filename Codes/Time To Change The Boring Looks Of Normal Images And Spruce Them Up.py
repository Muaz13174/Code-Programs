import cv2
import numpy as np
import matplotlib.pyplot as plt
import warnings as w
w.filterwarnings("ignore")
img = cv2.imread("../Pictures/test pic.jpg")
imgrgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)