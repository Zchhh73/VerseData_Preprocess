import SimpleITK as sitk
import nibabel as nib
import imageio
import numpy as np
import os



# 源文件位置(需要自己设置)
filepath = 'F:\\data\\train\\verse401\\verse401_verse201_CT-iso_seg.nii.gz'
# 输出保存位置(需要自己设置)
savepicdir = 'slice_img/xVer2020/mask/case088/'


def uint16to8(imgs, lower_percent=0.001, higher_percent=99.999):
    # uint16转uint8,将0~65535缩放到0~255
    out = np.zeros_like(imgs, dtype=np.uint8)
    n = imgs.shape[0]
    for i in range(n):
        a = 0  # np.min(band)
        b = 255  # np.max(band)
        c = np.percentile(imgs[i, :, :], lower_percent)
        d = np.percentile(imgs[i, :, :], higher_percent)
        t = a + (imgs[i, :, :] - c) * (b - a) / (d - c)
        t[t < a] = a
        t[t > b] = b
        out[i, :, :] = t
    return out



if __name__ == '__main__':
    if not os.path.exists(savepicdir):
        os.makedirs(savepicdir)
    itk_img = sitk.ReadImage(filepath)
    img = sitk.GetArrayFromImage(itk_img)
    out = uint16to8(img)
    z, x, y = out.shape
    for k in range(z):
        print('正保存第{}张切片'.format(k))
        slice = out[k, :, :]
        imageio.imwrite(os.path.join(savepicdir, '{}.png'.format(k)), slice)
    print('保存完成')
