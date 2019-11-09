# -*- coding: utf-8 -*-

import cv2
import numpy as np

def morph(img):
    kernel = np.ones((3, 3),np.uint8)
    opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=2)
    return opened

img_src = cv2.imread("hiyoko.png", 1)
img_filtterd=morph(img_src)
# 表示
cv2.imshow("Show GAUSS Image", img_filtterd)
cv2.waitKey(0)
cv2.destroyAllWindows()
