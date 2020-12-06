from PIL import Image
import glob
import os


def ResizeImage(filename, outdir, width=512, height=512):
    img = Image.open(filename)
    out = img.resize((width, height), Image.BILINEAR)
    outname = os.path.basename((filename))
    out.save(os.path.join(outdir, outname))
    print(outname, '保存完成')


if __name__ == '__main__':
    filedir = 'slice_img/xVer2016/train/mask/image003/*.png'
    outdir = 'resized_data/xVer2016/train/mask/image003/'
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    for filename in glob.glob(filedir):
        ResizeImage(filename, outdir)
