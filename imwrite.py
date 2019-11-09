#coding: utf-8

import numpy as np
import cv2

img = cv2.imread('hand.png', cv2.IMREAD_GRAYSCALE)

#forsaleという名前でjpeg保存
cv2.imwrite('hand-edit.jpg', img)

#forsale2というpngを保存
cv2.imwrite('hand-edit2.png', img)
