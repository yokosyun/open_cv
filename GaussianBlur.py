# -*- coding: utf-8 -*-

import cv2
import numpy as np

def blur(img):
    # 平均化する画素の周囲の大きさを指定する。
    # (5, 5) の場合、個々の画素の地点の周囲5×5マスの平均をとる。
    # 数値が大きいほどぼやける。
    average_square = (25, 25)

    # x軸方向の標準偏差
    sigma_x = 0

    # Gaussianオペレータを使用して平滑化
    img_gauss = cv2.GaussianBlur(img, average_square, sigma_x)
    return img_gauss

# 画像の読み込み
img_src = cv2.imread("karasu.jpg", 1)
img_filtterd=blur(img_src)
# 表示
cv2.imshow("Show GAUSS Image", img_filtterd)
cv2.waitKey(0)
cv2.destroyAllWindows()
