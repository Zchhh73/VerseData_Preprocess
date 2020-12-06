import imageio
import os

filespath = 'slice_img/1_L1_GT/'
outfilename = '1_L1.gif'
filenames = []
path_list = os.listdir(filespath)
path_list.sort(key=lambda x:int(x.split('.')[0]))
for img in path_list:
    image_file = filespath + img
    im = imageio.imread(image_file)
    filenames.append(im)

imageio.mimsave(outfilename, filenames, 'GIF', duration=0.1)
