import numpy as np

def prepareData(imArray, ambientImage):
	print(np.sum(imArray))
	for i in range(imArray.shape[2]):
		# imArray[:, :, i] -= ambientImage
		# test = imArray[:, :, i] - ambientImage
		# result = imArray[:, :, i] - test
		# comparison = imArray[:, :, i] == test
		# equal_arrays = comparison.all()
		# print(equal_arrays)
		# count = np.count_nonzero(result)
		# count = len([1 for x in result if x > 0])
		# print(imArray.shape[0], imArray.shape[1], imArray.shape[0] * imArray.shape[1], count) 

		# import matplotlib.pyplot as plt
		# plt.imshow(imArray[:, :, i], cmap='gray')
		# plt.show()
		# test = imArray[:, :, i] - imArray[:, :, i]/2
		# test = imArray[:, :, i] - ambientImage
		# test = imArray[:, :, i] - ambientImage
		# plt.imshow(test, cmap='gray')
		# plt.show()
		# test[test<0] = 0
		# print(np.amax(test))
		# max_intensity_value = np.amax(test)
		# test = test / max_intensity_value
		# print(np.amax(test))

		# plt.imshow(test, cmap='gray')
		# plt.show()
		# plt.imshow(ambientImage, cmap='gray')
		# plt.show()

		# print(np.sum(imArray[:, :, i]))
		imArray[:, :, i] -= ambientImage
		# print(np.sum(imArray[:, :, i]))
		max_intensity_value = np.amax(imArray[:, :, i])
		# print(max_intensity_value)
		imArray[:, :, i] /= max_intensity_value
		# print(np.sum(imArray[:, :, i]))

		print(np.sum(imArray))
	return imArray
	# return imArray