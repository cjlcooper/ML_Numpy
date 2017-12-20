import numpy as np

#matrix1
a = np.arange(9, dtype = np.float).reshape(3,3)
print a

#matrix2
b = np.arange(9, dtype = np.float)
b.shape = (3,3)
print b

#add
print np.add(a,b)

#subtract
print np.subtract(a,b)

#multiply
print np.multiply(a,b)

#divide
print np.divide(a,b)