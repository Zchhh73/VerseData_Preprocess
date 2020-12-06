import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from skimage import morphology, color, data, filters

'''
参考：
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_watershed/py_watershed.html
https://blog.csdn.net/yuanpan/article/details/82011826
'''

image = 'cropped_slice/cropped_20.png'

img = cv2.imread(image, 2)
# gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)


# 去噪，对图像进行膨胀之后再进行腐蚀操作提取图像特征
kernel1 = np.ones((4, 4), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel1, iterations=1)
# 背景
sure_bg = cv2.dilate(opening, kernel1, iterations=1)

fig = plt.figure()
ax1 = fig.add_subplot(231)
ax1.imshow(img, cmap=plt.cm.gray)
ax2 = fig.add_subplot(232)
ax2.imshow(thresh, cmap=plt.cm.gray)
ax3 = fig.add_subplot(233)
ax3.imshow(opening, cmap=plt.cm.gray)
ax4 = fig.add_subplot(234)
ax4.imshow(sure_bg, cmap=plt.cm.gray)
# ax5 = fig.add_subplot(235)
# ax5.imshow(th4, cmap=plt.cm.gray)
plt.show()
print(img)
'''



image = color.rgb2gray(data.camera())
denoised = filters.rank.median(image, morphology.disk(2))  # 过滤噪声
#将梯度值低于10的作为开始标记点
markers = filters.rank.gradient(denoised, morphology.disk(5)) <10
markers = ndi.label(markers)[0]
gradient = filters.rank.gradient(denoised, morphology.disk(2)) #计算梯度
labels =morphology.watershed(gradient, markers, mask=image) #基于梯度的分水岭算法


fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(6, 6))
axes = axes.ravel()
ax0, ax1, ax2, ax3 = axes


ax0.imshow(image, cmap=plt.cm.gray, interpolation='nearest')
ax0.set_title("Original")
ax1.imshow(gradient, cmap=plt.cm.gray, interpolation='nearest')
ax1.set_title("Gradient")
ax2.imshow(markers, cmap=plt.cm.gray, interpolation='nearest')
ax2.set_title("Markers")
ax3.imshow(labels, cmap=plt.cm.gray, interpolation='nearest')
ax3.set_title("Segmented")
for ax in axes:
    ax.axis('off')

fig.tight_layout()
plt.show()
'''
