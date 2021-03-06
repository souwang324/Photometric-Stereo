import numpy as np
from scipy import integrate
import math

def getSurface(surfaceNormals, method):
	print("surfaceNormals.shape:{}".format(surfaceNormals.shape))

	w = surfaceNormals.shape[1]
	h = surfaceNormals.shape[0]
	heightmap = np.zeros((h, w))
	g1xy = surfaceNormals[:,:,0]
	g2xy = surfaceNormals[:,:,1]
	g3xy = surfaceNormals[:,:,2]
	fx = g1xy / g3xy
	fy = g2xy / g3xy
	fxy = g2xy / fx
	fyx = g1xy / fy

	# integrability = abs(fxy-fyx)
	# print(integrability)
	# print("max:{}  min:{} avg:{}".format(np.amax(integrability), np.amin(integrability), np.average(integrability)))
	# integrability[integrability > np.average(integrability)] = 0
	# print(integrability)
	# print("max:{}  min:{} avg:{}".format(np.amax(integrability), np.amin(integrability), np.average(integrability)))
	# fx[integrability == 0] = 0
	# fy[integrability == 0] = 0
	if method == 'column':
		print("method: COL")
		heightmap[:,0] = np.cumsum(fy[:,0], axis=0)
		fx[:,0] = heightmap[:,0]
		heightmap = np.cumsum(fx, axis=1)

		return heightmap

	if method == 'row':
		print("method: ROW")
		heightmap[0,:] = np.cumsum(fx[0,:])
		fy[0,:] = heightmap[0,:]
		heightmap = np.cumsum(fy, axis=0)
		return heightmap

	if method == 'average':
		print("method: AVERAGE")
		map_col = np.zeros((h, w))
		map_col[:,0] = np.cumsum(fy[:,0], axis=0)
		fx[:,0] = map_col[:,0]
		map_col = np.cumsum(fx, axis=1)
		print("max:{}  min:{} avg:{}".format(np.amax(map_col), np.amin(map_col), np.average(map_col)))

		map_row = np.zeros((h, w))
		map_row[0,:] = np.cumsum(fx[0,:])
		fy[0,:] = map_row[0,:]
		map_row = np.cumsum(fy, axis=0)
		print("max:{}  min:{} avg:{}".format(np.amax(map_row), np.amin(map_row), np.average(map_row)))

		map_avg = (map_col + map_row) / 2
		print("max:{}  min:{} avg:{}".format(np.amax(map_avg), np.amin(map_avg), np.average(map_avg)))

		return map_avg

	if method == 'random':
		raise NotImplementedError("You should implement this.")
