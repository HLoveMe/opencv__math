
# -*- coding: utf-8 -*-
import numpy as np
a = np.arange(1,20,2)
print  a[5]
print  a[2:5]
print a[:-1]
print a[1:-1:2]

# 赋值

a[3:5] = 100,1
print a


print "通过下标取得数据之后的数组 和之前的共享同一内存"

b = np.arange(1,100,3)
c =  b[2:8]
c[1]=1000
print b

print "使用整数序列 获取数据"
a = np.arange(1,100,4)        #<type 'numpy.ndarray'>

# 1:使用序列为下标与原数组不共享内存
b = a[[1,4,6,9]]
b[1]=99
print b
print a

c =  a[np.arange(1,10)]
print c

print " 布尔数组"

a = np.random.rand(10)
print a
b = a>0.5
print b
print  a[a>0.7]   #  得到true对应的值
