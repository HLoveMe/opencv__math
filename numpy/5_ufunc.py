# -*- coding: utf-8 -*-

print "ufunc是universal function的缩写，它是一种能对数组的每个元素进行操作的函数。"

import numpy as np


a =  np.linspace(1,8*np.pi,25)
print a

print  "sin()函数  对[]计算比math快    但对于单个值 计算 sin(0.5)  比math慢"
b=np.sin(a)
print b



"a b 个数一致 结果的每次元素是    a  b  对应相操作"

a = np.arange(10)
b = np.arange(10,20)
print np.add(a,b)



print "计算法则"

np.arange(0,60,10).reshape((-1,1))+np.arange(0,5)
"""
A:让所有输入数组都向其中shape最长的数组看齐，shape中不足的部分都通过在前面加1补齐
B:输出数组的shape是输入数组shape的各个轴上的最大值
C:如果输入数组的某个轴和输出数组的对应轴的长度相同或者其长度为1时，这个数组能够用来计算，否则出错
D:当输入数组的某个轴的长度为1时，沿着此轴运算时都用此轴上的第一组值

np.arange(0,60,10)  --->[0,10,20,30,40,50]  shape (1,6)
np.arange(0,60,10).reshape((-1,1))     shape   (6,1)

np.arange(0,5)    shape  (5,0) A--->(1,5)

(6,1)+(1,5) B--->  (6,5)

 0                    0  0  0   0  0
10                   10 10 10  10 10
20                   20 20 20  20 20
30     D------->     30 30 30  30 30
40                   40 40 40  40 40
50                   50 50 50  50 50

            +
                             [0 1 2 3 4
                             0 1 2 3 4
0 1 2 3 4   D---->           0 1 2 3 4
                             0 1 2 3 4
                             0 1 2 3 4]











"""

print np.arange(0,60,10).reshape((-1,1))+np.arange(0,5)



import time
import math

print "sin计算"
#
# x = [i for i in range(100000)]
# start = time.clock()
# for i,v in enumerate(x):
#     x[i]=math.sin(v)
# print time.clock()-start
#
# x = [i for i in range(100000)]
# a = np.array(x)
# start = time.clock()
# b = np.sin(a)
# print time.clock()-start

"""

y = x1 + x2:	add(x1, x2 [, y])
y = x1 - x2:	subtract(x1, x2 [, y])
y = x1 * x2:	multiply (x1, x2 [, y])
y = x1 / x2:	divide (x1, x2 [, y]), 如果两个数组的元素为整数，那么用整数除法
y = x1 / x2:	true divide (x1, x2 [, y]), 总是返回精确的商
y = x1 // x2:	floor divide (x1, x2 [, y]), 总是对返回值取整
y = -x:	negative(x [,y])
y = x1**x2:	power(x1, x2 [, y])
y = x1 % x2:	remainder(x1, x2 [, y]), mod(x1, x2, [, y])

"""

print "加法计算"
a =  np.arange(0,4)
b = np.arange(1,5)
print np.add(a,b)
print  a+b


print "减法"
a =  np.arange(0,4)
b = np.arange(1,5)
print np.subtract(b,a)
print b-a

print "乘法"

a =  np.arange(0,4)
b = np.arange(1,5)
print np.multiply(a,b)
print a*b

print "除法"

"""
    如果x/y 都是整数  就按照整数除法
    x/y 返回精确商 np.true_divide(a,b)
    x//y  取整返回 floor_divide (x1, x2 ), 总是对返回值取整
"""
a =  np.arange(1,5)
b = np.arange(19,23)

print np.true_divide(b,a)
print b/a
print b//a

a =  np.arange(1.0,5.0)
b = np.arange(19.0,23.0)
print np.true_divide(b,a)
print b/a
print b//a


print "相反数"

a = np.arange(1,10)
print np.negative(a)
print -a

print "乘方"

a = np.arange(1,10)
b = np.array([2  for i in range(1,10)])

print np.power(a,b)
print a**b

print "取余"
a = np.arange(1,10)
b = np.array([2  for i in range(1,10)])
print b%a
print np.remainder(b,a)




print "自定义计算函数"

def triangle_wave(x, c, c0, hc):
    x = x - int(x)
    if x >= c: r = 0.0
    elif x < c0: r = x / c0 * hc
    else: r = (c-x) / (c-c0) * hc
    return r


# 1: 收到创建
x = np.linspace(0,2,100)
y = np.array([triangle_wave(t,0.6,0.4,1.0) for t in x])
print y

#2:使用np 创建   参数个数,返回值个数
mFunc = np.frompyfunc(lambda  one :triangle_wave(one,0.6,0.4,1.0),1,1)
print mFunc(x)

# def AAAA():
#     def triangle_wave(x, c, c0, hc):
#         x = x - int(x)
#         if x >= c:
#             r = 0.0
#         elif x < c0:
#             r = x / c0 * hc
#         else:
#             r = (c - x) / (c - c0) * hc
#         return r
#     return np.frompyfunc(lambda one:triangle_wave(one,0.6,0.4,1.0),1,1)
# print "=============="
# print AAAA()(x)





print " 当使用nfunc进行数组计算时  通常是数组的shape是一致的" \
      "如果shape不一致 就会进行广播处理"
'''
让所有输入数组都向其中shape最长的数组看齐，shape中不足的部分都通过在前面加1补齐
输出数组的shape是输入数组shape的各个轴上的最大值
如果输入数组的某个轴和输出数组的对应轴的长度相同或者其长度为1时，这个数组能够用来计算，否则出错
当输入数组的某个轴的长度为1时，沿着此轴运算时都用此轴上的第一组值
'''

a = np.arange(0,5)
b = np.arange(0,5).reshape((-1,1))
print a
print b
print a*b
print a+b



print "ufunc函数本身还有些方法"
print  np.add.reduce([1,2,3])







print "矩阵操作"
"""
 对于两个一维的数组，计算的是这两个数组对应下标元素的乘积和(数学上称之为内积)；
 对于二维数组，计算的是两个数组的矩阵乘积；
 对于多维数组，它的通用计算公式如下，即结果数组中的每个元素都是：数组a的最后一维上的所有元素与数组b的倒数第二位上的所有元素的乘积和：
"""
a = np.arange(12).reshape(2,3,2)
b = np.arange(12,24).reshape(2,2,3)
c = np.dot(a,b)  #最后一维必须长度一致
print  c
print c.shape

"""
对于两个一维数组，计算的是这两个数组对应下标元素的乘积和；
对于多维数组，它计算的结果数组中的每个元素都是：数组a和b的最后一维的内积，因此数组a和b的最后一维的长度必须相同
"""
#   数组(长度为2 每个元素为数组(长度为3 每个元素为数组(长度4)))
a = np.arange(24).reshape(2,3,4)
#   数组(长度为24每个元素为数组(长度为2 每个元素为数组(长度3)))
b = np.arange(24,48).reshape(3,2,4)
# print  np.inner(a,b) #最后一维必须长度一致

"""
只按照一维数组进行计算，如果传入参数是多维数组，则先将此数组展平为一维数组之后再进行运算。
outer乘积计算的列向量和行向量的矩阵乘积：
"""
print np.outer([4,5,6,7],[1,2,3])

"""
矩阵中更高级的一些运算可以在NumPy的线性代数子库linalg中找到
"""


print "文件操作"

a  = np.linspace(1,2,10).reshape(2,5)
print a
import os
path = os.path.join(os.path.dirname(__file__),"a.txt")
# 写入
a.tofile(path)

b = np.fromfile(path,dtype=np.float)# 读取出来  shape 要手动调整
print b
"""
numpy.load和numpy.save函数以NumPy专用的二进制类型保存数据，这两个函数会自动处理元素类型和shape等信息
"""

"""
保存多个数组到一个文件中
numpy.savez(file,a,b,other=c)
1:file后缀为 npz
2:numpy.load(file) 自动识别npz后缀文件  得到类似字典对象-->res
3:res['arr_0']--->a
  res['arr_1']--->b
  res['other']--->c
"""
# path = os.path.join(os.path.dirname(__file__),"a.npz")
# # np.savez(path,a,b)
# dic = np.load(path)
# print dic['arr_0']


"""
numpy.load和numpy.save函数以NumPy专用的二进制类型保存数据，这两个函数会自动处理元素类型和shape等信息
np.savetxt("a.txt", a) # 缺省按照'%.18e'格式保存数据，以空格分隔
np.loadtxt("a.txt")

np.savetxt('a.txt',arr,fmt="%f",delimiter='__') 文件 数组 格式 分割线
np.savetxt('a.txt',delemiter="__")
"""
