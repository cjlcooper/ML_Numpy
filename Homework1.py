import numpy as np
import math

# basic sigmoid function
def basic_sigmoid(x):
	s = 1.0 / (1.0 + math.exp(-x))
	return s

print basic_sigmoid(3)

# np exp function
def sigmoid(x):
	s = 1.0 / (1.0 + np.exp(-x))
	return s

x1 = np.array([1,2,3])
print sigmoid(x1)

# image to vector function
def image2Vector(image):
	#reshape of matrix
	v = image.reshape(image.shape[0] * image.shape[1] * image.shape[2],1)
	return v

# softx max function
def softmax(x):
	x_exp = np.exp(x)
	x_sum = np.sum(x_exp, axis=1, keepdims=True)
	s = x_exp / x_sum
	return s

x2 = np.array([
	[9,2,5,0,0],
	[7,5,0,0,0]])
print softmax(x2)

# Vectorization
