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

	if method == 'column':
		print("method: COLUMN")
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

		map_row = np.zeros((h, w))
		map_row[0,:] = np.cumsum(fx[0,:])
		fy[0,:] = map_row[0,:]
		map_row = np.cumsum(fy, axis=0)

		map_avg = (map_col + map_row) / 2
		return map_avg

	if method == 'rand':
		print("method: RANDOM")
		tries = 30
		import time
		start_time = time.time()
		print("calcultaing randompaths...", end="")
		for y in range(h):
			for x in range(w):
				total_integral = 0
				for t in range(tries):
					integral = 0
					path = randompath([y, x])
					for p in range(1, len(path)):
						new_dir = [a-b for a,b in zip (path[p], path[p-1])]
						new_y = path[p][0]
						new_x = path[p][1]
						if new_dir[0] == 1:
							integral += fy[new_y][new_x]
						else:
							integral += fx[new_y][new_x]
					total_integral += integral
					# print("try {}: {}".format(t, integral), end=" ")
				# print("  avg:{}".format(total_integral/tries))
				# print()
				heightmap[y][x] = total_integral / tries
		time_elapsed = time.time() - start_time
		mins = time_elapsed // 60
		seconds = time_elapsed % 60
		print(" elapsed {} mins {:.2f} seconds.".format(mins, seconds))
		return heightmap


def randompath(end):
    # path = [start]
    current = [0, 0]
    path = [current]
    while current[0] <= end[0] and current[1] <= end[1]:
        if current[0] == end[0]:	# reached at desired y location
            for i in range(end[1] - current[1]):
                new_path = [x+y for x,y in zip (current, [0, 1])]
                path.append(new_path)
                current = new_path
            return path
        elif current[1] == end[1]:	# reached at desired x location
            for i in range(end[0] - current[0]):
                new_path = [x+y for x,y in zip (current, [1, 0])]
                path.append(new_path)
                current = new_path
            return path
        
        rand_d = np.random.randint(2)
        d = 'down' if rand_d == 1 else 'right'
        if d == 'down':
            new_path = [x+y for x,y in zip (current, [1, 0])]
        else:
            new_path = [x+y for x,y in zip (current, [0, 1])]
        path.append(new_path)
        current = new_path
    return path