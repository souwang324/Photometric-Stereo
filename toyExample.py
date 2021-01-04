import numpy as np
import matplotlib.pyplot as plt

def toyExample(imageSize, numImages):
    
    imageSize = np.array(imageSize)

    ambientImage = np.zeros(imageSize)
    imArray = np.zeros((imageSize[0], imageSize[1], numImages))
    trueAlbedo = np.zeros((imageSize[0], imageSize[1]))

    #Generate the scene
    r = np.floor(np.min(imageSize)/2)-1
    ctr = np.ceil(imageSize/2)
    cy = int(ctr[0])
    cx = int(ctr[1])

    #Lay down a meshgrid to compute the x and y coordinates
    xx, yy = np.meshgrid(np.arange(imageSize[1]), np.arange(imageSize[0]))
    dd = r*r - (xx-cx)**2 - (yy-cy)**2
    bg = dd <= 0
    dd[bg] = 0
    trueHeightMap = np.sqrt(dd)

    #Normals for the foregroud are based on the point on the hemisphere
    distance = np.sqrt((xx-cx)**2 + (yy-cy)**2 + trueHeightMap**2)
    nx = -(xx-cx)/distance
    ny = -(yy-cy)/distance
    nz = trueHeightMap/distance

    #Normals for the background are [0 0 1]
    nx[bg] = 0
    ny[bg] = 0
    nz[bg] = 1

    trueSurfaceNormals = np.concatenate((nx[:, :, np.newaxis],
            ny[:, :, np.newaxis], nz[:, :, np.newaxis]), axis=2)

    #Albedo (checkered pattern)
    trueAlbedo[0:cy, 0:cx] = 1
    trueAlbedo[0:cy, cx:] = 0.3
    trueAlbedo[cy:, 0:cx] = 0.3
    trueAlbedo[cy:, cx:] = 1
    trueAlbedo[bg] = 0.5

    #Generate random samples of light directions and images
    lightDirs = np.random.randn(numImages, 3)
    lightDirs[:, 2] = np.abs(lightDirs[:, 2])
    l2norm = np.sqrt(np.sum(lightDirs**2, axis=1))
    lightDirs = lightDirs/l2norm[:, np.newaxis]
    normalArray = trueSurfaceNormals.reshape((imageSize[0]*imageSize[1], 3))
    for i in range(numImages):
        img = trueAlbedo.flatten() * normalArray.dot(lightDirs[i, :])
        imArray[:, :, i] = img.reshape(imageSize)

    imArray = np.maximum(imArray, 0)

    return (ambientImage, imArray, lightDirs, trueAlbedo, trueSurfaceNormals, trueHeightMap)


if __name__ == '__main__':
    ambient, imarray, lightdirs, truealbedo, normals, height = toyExample((128, 128), 10)
