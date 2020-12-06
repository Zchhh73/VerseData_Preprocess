import cv2
import matplotlib.pyplot as plt
import os
import numpy as np

filename = 'cropped_slice/cropped_102.png'
'''
图像去噪
'''
img = cv2.imread(filename, 0)
# 中值滤波
median = cv2.medianBlur(img, 5)
# 滤波
filter1 = cv2.blur(img, (5, 5))
# 高斯滤波
filter2 = cv2.GaussianBlur(img, (5, 5), 1.5)
# 显示图片
fig = plt.figure()
# 131表示1行3列，第一个索引，以此类推
ax1 = fig.add_subplot(131)
ax1.imshow(img, cmap=plt.cm.gray)
ax2 = fig.add_subplot(132)
ax2.imshow(median, cmap=plt.cm.gray)
ax3 = fig.add_subplot(133)
ax3.imshow(filter2, cmap=plt.cm.gray)
plt.show()


def edge_demo(image):
    '''
    Canny边缘提取
    :param image:
    :return:
    '''
    # 1.高斯滤波器去噪
    blurred = cv2.GaussianBlur(image, (5, 5), 1.5)
    image = image.astype(np.uint8)
    # 2. 计算梯度幅值和方向
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    # xgrad = cv.Sobel(gray, cv.CV_16SC1, 1, 0) #x方向梯度
    # ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1) #y方向梯度
    # edge_output = cv.Canny(xgrad, ygrad, 50, 150)
    # 3.主体
    edge_output = cv2.Canny(image, 50, 150)
    cv2.imshow("Canny Edge", edge_output)
    # dst = cv2.bitwise_and(image, image, mask=edge_output)
    # cv2.imshow("Color Edge", dst)
    return edge_output


# 读取图片
src = cv2.imread(filename)
# 该4步为增强对比度
fi = src / 255.0
gamma = 2
out = np.power(fi, gamma)
out = out.astype(np.float32)
# 高斯滤波器
blurred = cv2.GaussianBlur(out, (5, 5), 1.5)
gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
# 自适应阈值
ret, thresh1 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 5)
# edge_output = cv2.Canny(blurred, 50, 150)
# canny = edge_demo(blurred)

# 显示图片
fig = plt.figure()
ax1 = fig.add_subplot(231)
ax1.imshow(src, cmap=plt.cm.gray)
ax2 = fig.add_subplot(232)
ax2.imshow(out, cmap=plt.cm.gray)
ax3 = fig.add_subplot(233)
ax3.imshow(blurred, cmap=plt.cm.gray)
ax4 = fig.add_subplot(234)
ax4.imshow(thresh1, cmap=plt.cm.gray)
# ax6 = fig.add_subplot(236)
# ax6.imshow(edge_output, cmap=plt.cm.gray)
plt.show()
