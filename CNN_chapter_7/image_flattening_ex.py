import numpy as np

# A simple 2D grayscale image (Each pixel has only one numerical value to represent)

image_gray = np.array(
	[[1,2,3],
	[4,5,6],
	[0,5,8]]
)

print(image_gray.shape)

image_gray_flattened = image_gray.flatten()
print("Flattened 1D array (grayscale)")
print(image_gray_flattened)
print(image_gray_flattened.shape)

test_shape = np.array([1,2,3])
print(test_shape.shape)
# (3,) 
# Absence of the second element means this is a 1D array

image_rgb = np.array([
	[[255,255,255], [255, 7,5]],
	[[243, 234, 109], [23, 45, 67]],
	[[12, 34, 0], [12, 45, 34]]
])
# shape
print(image_rgb.shape)
image_rgb_flattened = image_rgb.flatten()
print("Flattened RGB image: ")
print(image_rgb_flattened)
print("Shape: ", image_rgb_flattened.shape)