import numpy as np

def randompath(start, end):
	import numpy as np
	path = [start]
	current = start
	while current[0] < end[0] and current[1] < end[1]:
		rand_d = np.random.randin(2)
		d = 'down' if rand_d == 1 else 'right'
		if d == 'down':
			new_path = current + [0, 1]
		else:
			new_path = current + [1, 0]
		path.append(new_path)
	print(path)
