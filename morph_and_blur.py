# -*- coding: utf-8 -*-

import cv2
import numpy as np

def morph_and_blur(img):
    kernel = np.ones((3, 3),np.uint8)
    m = cv2.GaussianBlur(img, (3, 3), 0)
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, kernel, iterations=2)
    m = cv2.GaussianBlur(m, (5, 5), 0)
    return m

img_src = cv2.imread("hiyoko.png", 1)
img_filtterd=morph_and_blur(img_src)
# 表示
cv2.imshow("Show GAUSS Image", img_filtterd)
cv2.waitKey(0)
cv2.destroyAllWindows()
