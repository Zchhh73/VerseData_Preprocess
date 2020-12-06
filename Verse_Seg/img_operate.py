'''
图像运算
'''
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os


def image_union(original, mask):
    src1 = cv2.imread(original, cv2.IMREAD_UNCHANGED)
    src2 = cv2.imread(mask, cv2.IMREAD_UNCHANGED)

    # result = cv2.addWeighted(src1, 1, src2, 0, 0)
    result = src1 * src2
    newimg_name = original.split('/')[-1]
    print(newimg_name + '正在保存')
    cv2.imwrite('slice_img/1_L1_GT/' + newimg_name, result)
    print(newimg_name + '保存成功')
    # cv2.imshow('original', src1)
    # cv2.imshow('mask', src2)
    # cv2.imshow('result', result)
    # cv2.waitKey()
    # cv2.destroyAllWindows()


if __name__ == '__main__':
    original_path = 'slice_img/1_Original/'
    mask_path = original_path.replace('Original', 'L1')
    for imgs in os.listdir(original_path):
        img_file = original_path + imgs
        mask_file = mask_path + imgs
        # print(img_file,mask_file)
        image_union(img_file, mask_file)
