import cv2
import numpy as np

imageflie = 'cropped_slice/cropped_102.png'


def threshold_demo(image):
    # 全局阈值
    img = cv2.imread(image, 0)
    # gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)  # 把输入图像灰度化
    # 直接阈值化是对输入的单通道矩阵逐像素进行阈值分割。
    ret, binary = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
    print("threshold value {}".format(ret))
    cv2.namedWindow("binary0", cv2.WINDOW_NORMAL)
    cv2.imshow("binary0", binary)
    cv2.waitKey(0)


def local_threshold(image):
    # 局部阈值
    img = cv2.imread(image, 0)
    # gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)  # 把输入图像灰度化
    # 自适应阈值化能够根据图像不同区域亮度分布，改变阈值
    binary = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 10)
    median_binary = cv2.medianBlur(binary, 5)
    cv2.namedWindow("binary1", cv2.WINDOW_NORMAL)
    cv2.imshow('binary', binary)
    cv2.waitKey(0)
    cv2.imshow("median_binary", median_binary)
    cv2.waitKey(0)


def pengzhang(image):
    #膨胀算法
    kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (40, 40))
    iPengzhang = cv2.morphologyEx(image, cv2.MORPH_ERODE, kernel2)
    cv2.namedWindow("pengzhang", cv2.WINDOW_NORMAL)
    cv2.imshow('pengzhang', iPengzhang)
    cv2.waitKey(0)


if __name__ == '__main__':
    threshold_demo(imageflie)

    # local_threshold(imageflie)
