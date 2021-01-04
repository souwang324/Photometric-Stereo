import numpy as np


def alignChannels(img, max_shift):
	BLUE = 0
	GREEN = 1
	RED = 2

	# Check if image is large enough to crop
	if img.shape[0] > (max_shift[0]*20) and img.shape[1] > (max_shift[1]*20):
		p = 0.15	# percentage of crop
		crop_x = int(img.shape[1] * p)
		crop_y = int(img.shape[0] * p)
		# print("img: {}*{}  crop:{},{} for better alignment!!!".format(img.shape[1], img.shape[0], crop_x, crop_y))
		img = img[crop_y:-crop_y, crop_x:-crop_x]
		# print("img: {}*{}".format(img.shape[1], img.shape[0]))

	b = img[:,:,BLUE]
	g = img[:,:,GREEN]
	r = img[:,:,RED]

	# align green to blue
	best_g_shift = np.zeros((2, 1))
	min_g_ssd = 999999999
	for x in range(-max_shift[0], max_shift[0]+1):
		for y in range(-max_shift[1], max_shift[1]+1):
			g_shift = np.roll(g, [x, y], axis=[0, 1])
			s = ssd(g_shift, b)
			if s < min_g_ssd:
				min_g_ssd = s
				best_g_shift = np.array([x, y])

	# align red to blue
	best_r_shift = np.zeros((2, 1))
	min_r_ssd = 999999999
	for x in range(-max_shift[0], max_shift[0]+1):
		for y in range(-max_shift[1], max_shift[1]+1):
			r_shift = np.roll(r, [x, y], axis=[0, 1])
			s = ssd(r_shift, b)
			if s < min_r_ssd:
				min_r_ssd = s
				best_r_shift = np.array([x, y])

	pred_shift = np.array([best_g_shift, best_r_shift])
	img[:, :, GREEN] = np.roll(img[:, :, GREEN], [pred_shift[0, 0], pred_shift[0, 1]], axis=[0, 1])
	img[:, :, RED] = np.roll(img[:, :, RED], [pred_shift[1, 0], pred_shift[1, 1]], axis=[0, 1])
	return img, pred_shift

def ssd(imgA, imgB):
	diff = imgA.ravel() - imgB.ravel()    # ravel() is faster than flatten() since there's no copy
	return np.dot(diff, diff)