import numpy as np
import random
import cv2 as cv


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

def gasuss_noise(image, mean=0, var=0.001):
    '''
        添加高斯噪声
        mean : 均值
        var : 方差
    '''
    image = np.array(image/255, dtype=float)
    noise = np.random.normal(mean, var ** 0.5, image.shape)
    out = image + noise
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = np.clip(out, low_clip, 1.0)
    out = np.uint8(out*255)
    #cv.imshow("gasuss", out)
    return out

def max_min_value_filter(image, ksize=3, mode=1):
    """
    :param image: 原始图像
    :param ksize: 卷积核大小
    :param mode:  最大值：1 或最小值：2
    :return:
    """
    img = image.copy()
    rows, cols, channels = img.shape
    if channels == 3:
        img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    padding = (ksize-1) // 2
    new_img = cv.copyMakeBorder(img, padding, padding, padding, padding, cv.BORDER_CONSTANT, value=255)
    for i in range(rows):
        for j in range(cols):
            roi_img = new_img[i:i+ksize, j:j+ksize].copy()
            min_val, max_val, min_index, max_index = cv.minMaxLoc(roi_img)
            if mode == 1:
                img[i, j] = max_val
            elif mode == 2:
                img[i, j] = min_val
            else:
                raise Exception("please Select a Mode: max(1) or min(2)")
    cv.imshow("max_min_filter", img)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':

    img = cv.imread("./1/lena.jpg")
    cv.imshow("test", img)
    img1 = sp_noise(img, 0.05)
    cv.imshow("salt_noise", img1)
    img3 = cv.blur(img1, (5, 5))
    img4 = cv.medianBlur(img1, 5)
    img_min = max_min_value_filter(img1, ksize=5, mode=1)
    img_max = max_min_value_filter(img1, ksize=5, mode=2)
    cv.imshow("min_blur", img_min)
    cv.imshow("max_blur")
    cv.imshow("mean_blur", img3)
    cv.imshow("medianBlur", img4)

    cv.waitKey(0)