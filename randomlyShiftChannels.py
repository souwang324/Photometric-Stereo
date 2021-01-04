# This code is part of:
#
#   CMPSCI 370: Computer Vision, Spring 2018
#   University of Massachusetts, Amherst
#   Instructor: Subhransu Maji
#
#   Homework 1: Color images

import numpy as np

def randomlyShiftChannels(img, max_shift):
    '''Shifts the channels with respect to one another.o
    
    Randomly shifts the second and third channels of img within the
    max_shift range.
    '''
    assert(img.shape[2] == 3)

    # Randomly sample displacements in I and J coordinates between -max_shift:max_shift
    shift_i = np.random.randint(-max_shift[0], max_shift[0]+1, size=2)
    shift_j = np.random.randint(-max_shift[1], max_shift[1]+1, size=2)

    # print("rand_shift_i:{}, rand_shift_j:{}".format(shift_i, shift_j))

    #IMPORTANT: np.roll requires numpy 1.12.0 or newer
    #Replace the channels with the shifted versions
    img[:, :, 1] = np.roll(img[:, :, 1], [shift_i[0], shift_j[0]], axis=[0, 1])
    img[:, :, 2] = np.roll(img[:, :, 2], [shift_i[1], shift_j[1]], axis=[0, 1])

    #Record the true shifts
    gt_shift = np.array([shift_i, shift_j]).T
    
    return img, gt_shift

