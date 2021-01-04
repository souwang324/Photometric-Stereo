import numpy as np

def prepareData(imArray, ambientImage):
	# import matplotlib.pyplot as plt 
	for i in range(imArray.shape[2]):
		# plt.imshow(imArray[:,:,i], cmap='gray')
		# plt.show()
		imArray[:, :, i] -= ambientImage
		max_intensity_value = np.amax(imArray[:, :, i])
		imArray[:, :, i] /= max_intensity_value
		# plt.imshow(imArray[:,:,i], cmap='gray')
		# plt.show()

	return imArray
