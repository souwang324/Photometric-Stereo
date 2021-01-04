import numpy as np
import os
import errno
import matplotlib.pyplot as plt 

def imread(path):
    img = plt.imread(path).astype(float)
    
    #Remove alpha channel if it exists
    if img.ndim > 2 and img.shape[2] == 4:
        img = img[:, :, 0:3]
    #Puts images values in range [0,1]
    if img.max() > 1.0:
        img /= 255.0

    return img


def mkdir(dirpath):
    if not os.path.exists(dirpath):
        try:
            os.makedirs(dirpath)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
    else:
        print("Directory {} already exists.".format(dirpath))

    
