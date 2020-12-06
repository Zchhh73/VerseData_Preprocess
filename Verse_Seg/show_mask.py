import cv2
import os
import matplotlib.pyplot as plt


def union_image_mask(image_path, mask_path, num):
    '''
    将mask显示到original中
    :param image_path:
    :param mask_path:
    :param num:
    :return:
    '''

    image = cv2.imread(image_path)
    mask_2d = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
    # 显示
    cv2.imshow('2d', mask_2d)
    # 在opencv中，查找轮廓从黑色背景中找白色对象
    ret, thresh = cv2.threshold(mask_2d, 127, 255, 0)
    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
    cv2.imwrite(str(num) + '.bmp', image)
    cv2.imshow('mask', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ == '__main__':
    original = 's/original_1_7/15.bmp'
    mask = 'data/mask_1_7/15.bmp'
    union_image_mask(original, mask, 15)
