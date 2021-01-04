# This code is part of:
# 
#   CMPSCI 670: Computer Vision
#   University of Massachusetts, Amherst
#   Instructor: Subhransu Maji
# 
# Evaluation code for photometric stereo
# 
# Your goal is to implement the three functions prepareData(), 
# photometricStereo() and getSurface() to estimate the albedo and shape of
# the objects in the scene from multiple images. 
# 
# Start with setting subjectName='debug' which sets up a toy scene with
# known albedo and height which you can compare against. After you have a
# good implementation of this part, set the subjectName='yaleB01', etc. to
# run your code against real images of people. 
# 
# Credits: The homework is adapted from a similar one developed by
# Shvetlana Lazebnik (UNC/UIUC)


import os
import time
import numpy as np
import matplotlib.pyplot as plt 
import skimage.io as io

from utils import *
from getSurface import *
from photometricStereo import *
from loadFaceImages import *
from toyExample import *
from prepareData import *
from displayOutput import *
from plotSurfaceNormals import *

subjectName = 'yaleB07' #'debug' #debug, yaleB01, yaleB02, yaleB05, yaleB07
numImages = 128
writeOutput = True
data_dir = os.path.join('..', 'data')
out_dir = os.path.join('..', 'output', 'photometricStereo')
image_dir = os.path.join(data_dir, 'photometricStereo', subjectName)
# integrationMethod = 'column'
# integrationMethod = 'row'
integrationMethod = 'average'
# integrationMethod = 'rand'
mkdir(out_dir)

if subjectName == 'debug':
    imageSize = (64, 64)
    (ambientImage, imArray, lightDirs, trueAlbedo, trueSurfaceNormals, trueHeightMap) = toyExample(imageSize, numImages)
else:
    (ambientImage, imArray, lightDirs) = loadFaceImages(image_dir, subjectName, numImages)




# plt.imshow(ambientImage, cmap='gray')
# plt.show()
imArray = prepareData(imArray, ambientImage)
(albedoImage, surfaceNormals) = photometricStereo(imArray, lightDirs)
# print("albedoImage:({}), surfaceNormals:({})".format(albedoImage.shape, surfaceNormals.shape))
# plt.imshow(albedoImage, cmap='gray')
# plt.show()
# plt.imshow(surfaceNormals[:,:,0], cmap='jet')
# plt.show()
# plt.imshow(surfaceNormals[:,:,1], cmap='jet')
# plt.show()
n = np.sum(np.array(surfaceNormals[:,:,2]) < 0, axis=0)
print(n)
# plt.imshow(surfaceNormals[:,:,2], cmap='jet')
# plt.show()
# heightMap = getSurface(surfaceNormals, integrationMethod)
# heightMap = getSurface(surfaceNormals, 'column')
# displayOutput(albedoImage, heightMap)
# heightMap = getSurface(surfaceNormals, 'row')
# displayOutput(albedoImage, heightMap)
# heightMap = getSurface(surfaceNormals, 'average')
# displayOutput(albedoImage, heightMap)
heightMap = getSurface(surfaceNormals, 'rand')
displayOutput(albedoImage, heightMap)

# plotSurfaceNormals(surfaceNormals)

if subjectName == 'debug':
    displayOutput(trueAlbedo, trueHeightMap)
    # plotSurfaceNormals(trueSurfaceNormals)


if writeOutput:
    imageName = os.path.join(out_dir, '{}_albedo.jpg'.format(subjectName))
    io.imsave(imageName, albedoImage)

    imageName = os.path.join(out_dir, '{}_normals_color.jpg'.format(subjectName))
    io.imsave(imageName, surfaceNormals)

    imageName = os.path.join(out_dir, '{}_normals_x.jpg'.format(subjectName))
    io.imsave(imageName, surfaceNormals[:, :, 0])

    imageName = os.path.join(out_dir, '{}_normals_y.jpg'.format(subjectName))
    io.imsave(imageName, surfaceNormals[:, :, 1])

    imageName = os.path.join(out_dir, '{}_normals_z.jpg'.format(subjectName))
    io.imsave(imageName, surfaceNormals[:, :, 2])

