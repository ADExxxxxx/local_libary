"""
item: 图像像素处理相关函数
author by : WIT_lyp
timestamp : 2019/11/5
"""


import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

"""
函数功能，实现图像的翻转
@:param1:[image]:输入图像
@:param2:[angle]:转动角度(逆时针)
@:param3:[center]:旋转中心点
@:param4:[scale]:缩放比例
@:return:返回翻转后的图像
"""
def rotate(image, angle, center=None, scale=1):
    (h, w) = image.shape[:2]
    if center is None:
        center = (w // 2, h // 2)

    M = cv.getRotationMatrix2D(center, angle, scale)
    rotate = cv.warpAffine(image, M, (w, h))
    return rotate


if __name__ == '__main__':
    img = cv.imread("./1/lena.jpg")

    img = cv.resize(img, (250, 250))
    cv.imshow("scale = 0.5", img)
    img = cv.resize(img, (750, 750))
    cv.imshow("scale = 1.5", img)

    plt.show()
    cv.waitKey(0)

