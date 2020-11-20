def image2vector(image):
	v = image.reshape(image.shape[0] * image.shape[1] * image.shape[2], 1)
	return v
image = np.random.rand(3,3,2)
print("image2vector(image) = " + str(image2vector(image)))
### END CODE HERE ###

