import cv2 as cv
import numpy as np
import random
import math

# 计算psnr
def psnr1(img1, img2):
    mse = np.mean((img1/1.0 - img2/1.0) ** 2)
    if mse < 1.0e-10:
        return 100
    return 10 * math.log10(255.0 ** 2 / mse)

def sp_noise(image,prob):
    '''
    添加椒盐噪声
    prob:噪声比例
    '''
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

def adaptiveProcess(img, width, height, k_size_min, k_size_max):
    pixels = []
    for i in range(-k_size_min // 2, k_size_min // 2 + 1):
        for j in range(-k_size_min // 2, k_size_min // 2 + 1):
            pixels.append(img[height + i][width + j])
    print(pixels)



if __name__ == '__main__':
    img = cv.imread("./22.jpg")

    cv.imshow("original", img)
    img_salt = sp_noise(img, 0.05)
    img_median = cv.medianBlur(img_salt, 5)
    mean = np.mean(img)
    mean_s = np.mean(img_salt)
    mean_m = np.mean(img_median)
    print("原始图像均值:", mean)
    print("噪声图像均值:", mean_s)
    print("去噪图像均值", mean_m)

    mse_m = np.mean((img/1.0 - img_median/1.0) ** 2)
    mse_m_s = np.mean((img_median/1.0 - img_salt/1.0) ** 2)
    mse_s = np.mean((img/1.0 - img_salt/1.0) ** 2)
    print()
    print("原始图像与去噪图像的MSE:", mse_m)
    print("噪点图像与去噪图像的MSE:", mse_m_s)
    print("原始图像与噪点图像的MSE:", mse_s)

    psnr_m = psnr1(img, img_median)
    psnr_m_s = psnr1(img_median, img_salt)
    psnr_s = psnr1(img_salt, img)
    print()
    print("原始图像与去噪图像的MSE:", psnr_m)
    print("噪点图像与去噪图像的MSE:", psnr_m_s)
    print("原始图像与噪点图像的MSE:", psnr_s)

    cv.imshow("sp", img_salt)
    cv.imshow("blur", img_median)
    cv.waitKey(0)
