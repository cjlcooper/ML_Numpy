import numpy as np

#*************************
#
# ndimin:set ndarray min dimensions,such as ndmin=1
#
#*************************

#crate a nd array
a = np.array([1,2,3])
print a

#create a two dimension array
b = np.array([[1, 2], [3, 4]])
print b

#set ndmin
c = np.array([1,2,3,4,5,6],ndmin=2)
print c
