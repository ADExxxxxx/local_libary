import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def OTSU(gray):
    hist = cv.calcHist([gray], [0], None, [256], [0, 256])  # 255*1的灰度直方图的数组
    gray_size = gray.size  # 图像像素数
    k = 0  # 初始化灰度阈值
    best_k = 0  # 最佳阈值
    best_M = 0  # 衡量阈值性

    p = []  # 灰度出现概率

    # for k in range(30,150):
    for i in range(len(hist)):
        p.insert(i, hist[i][0] / gray_size)  # 灰度集概率分布

    for k in range(30, 150):
        u = 0  # 从1到k的累计出现概率的平均灰度级
        u_t = 0  # 从1到256的累计出现概率的平均灰度级
        σ2_0 = 0  # 类内方差
        σ2_1 = 0  # 类内方差
        σ2_t = 0  # 灰度级的总方差
        sum_0 = np.sum(hist[0:k + 1:], axis=0)
        sum_1 = np.sum(hist[k + 1:256:], axis=0)

        w_0 = np.sum(p[0:k + 1:])
        w_1 = np.sum(p[k + 1:256:])  # 各类的概率

        for i in range(k + 1):
            u = i * p[i] + u

        for i in range(len(hist)):
            u_t = i * p[i] + u_t

        u0 = u / w_0
        u1 = (u_t - u) / w_1  # 各类的平均灰度级

        for i in range(k + 1):
            σ2_0 = (p[i] / w_0) * np.square(i - u0) + σ2_0
        for i in range(k + 1, 256):
            σ2_1 = (p[i] / w_1) * np.square(i - u1) + σ2_1  # 两类的类内方差
        for i in range(256):
            σ2_t = p[i] * np.square(i - u_t) + σ2_t  # 总方差

        σ2_w = w_0 * σ2_0 + w_1 * σ2_1  # 类内方差
        σ2_b = w_0 * w_1 * np.square(u1 - u0)  # 类间方差

        M = σ2_b / σ2_t  # 衡量阈值k的好坏
        if M > best_M:
            best_M = M;
            best_k = k;
    return best_M, best_k


if __name__ == "__main__":
    img = cv.imread('lena.jpg')  # 读取图像（BGR）
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # 转灰度图像
    M, k = OTSU(gray)
    print(M, k)
    ret, thresh1 = cv.threshold(gray, k, 255, cv.THRESH_BINARY)
    cv.imshow("histogram", thresh1)
    cv.waitKey(0)