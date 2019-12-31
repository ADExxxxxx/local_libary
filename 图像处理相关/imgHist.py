"""
item: 图像直方图处理相关函数
author by : WIT_lyp
timestamp : 2019/11/16
"""


import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


"""
函数功能:得到图片的灰度直方图
@:param1:[grayImage]:灰度图像
@:return:灰度直方图
"""


def grayHist(grayImage):
    plt.hist(grayImage.ravel(), 256)
    plt.show()

"""
函数功能:得到图片的灰度直方图
@:param1:[grayImage]:灰度图像
@:return:RGB直方图
"""
def RGBHist(image):
    B, G, R = cv.split(image)
    plt.subplot(2, 2, 1), plt.title("original_img")
    plt.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB)), plt.axis("off")
    plt.subplot(2, 2, 2), plt.title("R")
    plt.hist(R.ravel(), 256)

    plt.subplot(2, 2, 3), plt.title("G")
    plt.hist(G.ravel(), 256)
    plt.subplot(2, 2, 4), plt.title("B")
    plt.hist(B.ravel(), 256)
    plt.show()
