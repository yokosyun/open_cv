#coding: utf-8

import numpy as np
import cv2

#読み込み
img = cv2.imread('hand.png', cv2.IMREAD_GRAYSCALE)

#表示
cv2.imshow('image', img)

#キーボード入力を受け付ける
key = cv2.waitKey(0)

if key == 27:            #escの処理
    cv2.destroyAllWindows()
elif key == ord('s'):      #sの入力の処理
    cv2.imwrite('forsale.jpg', img)
    cv2.destroyAllWindows()
