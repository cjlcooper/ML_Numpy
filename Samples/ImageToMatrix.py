import os
import numpy as np

class GetMatrix():
	def getMatirx(self):
		matirx = np.mat([1,2,3,4])
		matirx.shape = (2,2)
		print matirx
		
getMat = GetMatrix()
getMat.getMatirx()