#!/usr/bin/python
#
#
#

import numpy as np

matrixA = np.arange(100)
matrixA.shape = (10,10)
print matrixA

matrixB = np.arange(100)
matrixB.shape = (10,10)
print matrixB

matrixR = matrixA*matrixB
print matrixR