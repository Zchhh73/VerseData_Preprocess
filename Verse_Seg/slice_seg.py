import cv2
import os
import matplotlib.pyplot as plt

filename = 'cropped_slice/cropped_102.png'
img_dir = 'cropped_slice/'
thresh_dir = 'seg_thresh/'

if not os.path.exists(thresh_dir):
    os.makedirs(thresh_dir)

img = cv2.imread(filename, 0)
# 去噪
median = cv2.medianBlur(img, 5)
# 阈值分割
ret, thresh1 = cv2.threshold(median, 127, 255, cv2.THRESH_BINARY)  # 黑白
fig = plt.figure()
ax1 = fig.add_subplot(131)
ax1.imshow(img, cmap=plt.cm.gray)
ax2 = fig.add_subplot(132)
ax2.imshow(median, cmap=plt.cm.gray)
ax3 = fig.add_subplot(133)
ax3.imshow(thresh1, cmap=plt.cm.gray)
plt.show()

# cv2.imshow('thresh1', thresh1)
# cv2.waitKey(0)
'''
#读取文件夹下所有内容
for _, _, imgs in os.walk(img_dir):
    for i in range(len(imgs)):
        # 阈值分割
        img = cv2.imread(os.path.join(img_dir, str(imgs[i])), 0)
        ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)  # 黑白
        # ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)  # 黑白二值反转
        # print(os.path.join(img_dir,str(img[i])))
        print(ret)
        cv2.imshow('thresh'+str(i), thresh1)
        cv2.waitKey(0)
# cv2.destroyAllWindows()
'''
