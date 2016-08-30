
# -*- coding: utf-8 -*-


import numpy as np


person =  np.dtype({
    'names':['name','age','weight'],
    'formats':['S32','i','f']           #char[32]
})

a = np.array([("朱子豪",32,75.5),("周密",22,52)],dtype=person)
print a['name']

#b = a[0]  b 和 a共享内存
b=a[0]
print b

print b[0]
print b['name']

print a[:]['age']

print  id(a)==id(b)

