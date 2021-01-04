import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import glob
import os

from random import shuffle


def sph2cart(az, el, r):
    rcos_theta = r * np.cos(el)
    x = rcos_theta * np.cos(az)
    y = rcos_theta * np.sin(az)
    z = r * np.sin(el)
    return x, y, z


def loadFaceImages(pathname, subject_name, num_images):

    filename = os.path.join(pathname, subject_name+'_P00_Ambient.pgm')
    ambimage = io.imread(filename)
    h, w = ambimage.shape

    d = os.path.join(pathname, subject_name+'_P00A*.pgm')
    filenames = glob.glob(d)
    total_images = len(filenames)
    
    if num_images < total_images:
        shuffle(filenames)
        filenames = filenames[0:num_images]
    else:
        print ('Total available images is less than specified.\nProceeding with {} images.\n'.format(
            total_images))

    nimages = len(filenames)
    ang = np.zeros((2, nimages))
    imarray = np.zeros((h, w, nimages))

    for i in range(nimages):
        fn = filenames[i].split("/")[-1]

        m = fn.find('A')+1
        ang[0, i] = float(fn[m:m+4])
        m = fn.find('E')+1
        ang[1, i] = float(fn[m:m+3])
        imarray[:, :, i] = io.imread(filenames[i])
        # print("imarray.shape:{}".format(imarray.shape))
        # print(fn)
        # plt.imshow(imarray[:, :, i], cmap='gray')
        # plt.show()

    X, Y, Z = sph2cart(np.pi*ang[0, :]/180.0, np.pi*ang[1, :]/180.0, 1.0)
    lightdirs = np.concatenate((Y[np.newaxis, :], Z[np.newaxis, :], X[np.newaxis, :]), axis=0)
    lightdirs = lightdirs.T

    return ambimage, imarray, lightdirs


if __name__ == '__main__':
    ambImage, imArray, lightDirs = loadFaceImages('../data/photometricStereo/yaleB01', 'yaleB01', 64)
    plt.imshow(imArray[:, :, 0], cmap='gray')
    # plt.imshow(ambImage[:, :], cmap='gray')
    # plt.imshow(lightDirs, cmap='gray')
    plt.show()