import numpy as np
import scipy

def photometricStereo(imarray, lightdirs):
	width = imarray[:,:,0].shape[1]
	height = imarray[:,:,0].shape[0]

	albedoImage = np.zeros((height, width))
	surfaceNormals = np.zeros((height, width, 3))

	print("w,h:{},{}".format(width, height))
	for y in range(height):
		for x in range(width):
			Ij = imarray[y,x,:]
			# scipy.linalg.lstsq returns solution of Ax = B
			Gxy, res, rnk, s = scipy.linalg.lstsq(lightdirs, Ij)
			# print(Gxy, res, rnk, s)
			Albedo_xy = np.linalg.norm(Gxy)
			Normal_xy = Gxy / Albedo_xy
			albedoImage[y][x] = Albedo_xy
			surfaceNormals[y][x] = Normal_xy

	return albedoImage, surfaceNormals
