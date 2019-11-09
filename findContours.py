# -*- coding: utf-8 -*-

import cv2
import numpy as np

def resize_image(img, size):
    # size is enough to img
    img_size = img.shape[:2]
    print("img_size[0]")
    print(img_size[0])
    print("img_size[1]")
    print(img_size[1])
    print("size[0]")
    print(size[0])
    print("size[1]")
    print(size[1])
    if img_size[0] > size[1] or img_size[1] > size[0]:
        raise Exception("img is larger than size")

    # centering
    row = (size[1] - img_size[0]) // 2
    col = (size[0] - img_size[1]) // 2
    resized = np.zeros(list(size) + [img.shape[2]], dtype=np.uint8)
    resized[row:(row + img.shape[0]), col:(col + img.shape[1])] = img

    # filling
    mask = np.full(size, 255, dtype=np.uint8)
    mask[row:(row + img.shape[0]), col:(col + img.shape[1])] = 0
    filled = cv2.inpaint(resized, mask, 3, cv2.INPAINT_TELEA)

    return filled

def binary_threshold_for_birds(path):
    img = cv2.imread(path)
    grayed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    under_thresh = 105
    upper_thresh = 145
    maxValue = 255
    th, drop_back = cv2.threshold(grayed, under_thresh, maxValue, cv2.THRESH_BINARY)
    th, clarify_born = cv2.threshold(grayed, upper_thresh, maxValue, cv2.THRESH_BINARY_INV)
    merged = np.minimum(drop_back, clarify_born)
    return merged

def detect_contour(path, min_size):
    contoured = cv2.imread(path)
    forcrop = cv2.imread(path)

    # make binary image
    birds = binary_threshold_for_birds(path)
    birds = cv2.bitwise_not(birds)

    # detect contour
    im2, contours, hierarchy = cv2.findContours(birds, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    crops = []
    # draw contour
    for c in contours:
        if cv2.contourArea(c) < min_size:
            continue

        # rectangle area
        x, y, w, h = cv2.boundingRect(c)
        x, y, w, h = padding_position(x, y, w, h, 5)

        # crop the image
        cropped = forcrop[y:(y + h), x:(x + w)]
        cropped = resize_image(cropped, (230, 230))
        crops.append(cropped)

        # draw contour
        cv2.drawContours(contoured, c, -1, (0, 0, 255), 3)  # contour
        cv2.rectangle(contoured, (x, y), (x + w, y + h), (0, 255, 0), 3)  #rectangle contour

    return contoured, crops


def padding_position(x, y, w, h, p):
    return x - p, y - p, w + p * 2, h + p * 2


img_filtterd=detect_contour("kamome.png",20)
# 表示
cv2.imshow("Show GAUSS Image", img_filtterd)
cv2.waitKey(0)
cv2.destroyAllWindows()
