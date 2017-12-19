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

#the empty of ndarray
f = np.empty([4,6], dtype = int)
print f

#the zeros of ndarray
g = np.zeros((5,6), dtype = int)
print g

#the ones of ndarray
h = np.ones((2,3), dtype = float)
print h

#-----------------
#
# ndarray data from there
#
#-----------------

#asarray
x = [1,2,3]
A = np.asarray(x, dtype = int)
print A

#frombuffer
tmp = 'Hello Man'
B = np.frombuffer(tmp, dtype = 'S1')
print B

#fromiter
