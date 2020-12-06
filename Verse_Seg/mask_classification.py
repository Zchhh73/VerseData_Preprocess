from PIL import Image
import random
import glob
import matplotlib.pyplot as plt
import numpy as np

img_files = 'resized_data/xVer2016/train/mask/image001/93.png'

if __name__ == '__main__':
    '''
    for img_file in glob.glob(img_files):
        img = Image.open(img_file)
        img = np.array(img)
    '''
    img = Image.open(img_files)
    img = np.array(img)
    x, y = img.shape
    for i in range(x):
        for j in range(y):
            if img[i,j] == 200:
                print(img[i, j])
    print(img.shape)
    plt.figure('mask')
    plt.imshow(img)
    plt.show()
