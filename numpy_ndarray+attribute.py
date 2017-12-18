import numpy as np

#get shape of ndarray
#(row, column)
a = np.array([[1,2,3],[4,5,6]])  
print a.shape

#change ndarray shape
b = np.array([[1,2,3],[4,5,6]])
b.shape = (3,2)
print b

#get ndim of ndarray
c = np.arange(24)
c.shape = (4,6)
print c.ndim
print c

#get itemsize of ndarray
d = np.array([1,2,3,4,5])
print d.itemsize

#get flags of ndarray
e = np.array([1,2,3,4,5])
print e.flags