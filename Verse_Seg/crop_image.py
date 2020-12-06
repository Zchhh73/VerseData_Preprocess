import cv2
import os

file_path = "slice_img/"
cropped_dir = "cropped_slice/"


#裁剪图片
if not os.path.exists(cropped_dir):
    os.makedirs(cropped_dir)

for _, _, images in os.walk(file_path):
    for i in range(len(images)):
        img = cv2.imread(os.path.join(file_path, images[i]))
        print("裁剪第" + str(i) + "张切片")
        cropped_img = img[186:838, 186:838]
        cv2.imwrite(cropped_dir+"cropped_" + str(i) + ".png", cropped_img)
print('裁剪完成')
