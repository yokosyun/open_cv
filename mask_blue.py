import cv2
import numpy as np

def mask_blue(path):
    img = cv2.imread(path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    blue_min = np.array([100, 170, 200], np.uint8)
    blue_max = np.array([120, 180, 255], np.uint8)

    blue_region = cv2.inRange(hsv, blue_min, blue_max)
    white = np.full(img.shape, 255, dtype=img.dtype)
    background = cv2.bitwise_and(white, white, mask=blue_region)  # detected blue area becomes white

    inv_mask = cv2.bitwise_not(blue_region)  # make mask for not-blue area
    extracted = cv2.bitwise_and(img, img, mask=inv_mask)

    masked = cv2.add(extracted, background)

    return masked


img=mask_blue("bird.png")
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
