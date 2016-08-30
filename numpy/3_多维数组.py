
# -*- coding: utf-8 -*-
import numpy as np
print  "多维数组"


a = np.random.randint(1,10,size=(6,6))
print a

# 取值   行 列
b = a[0,:]
print b
print a[:,2]

a =  np.arange(0,60,10)
print a
print  a.reshape((-1,1))
b = a.reshape((-1,1))+np.arange(0,6)
print b
print b[(0,1,2),(0,1,2)]    # (0,0)  (1,1)   (2,2)