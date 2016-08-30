# -*- coding: utf-8 -*-
import numpy as np
"""
https://www.douban.com/note/363857295/


1:a = np.array([1,23,4,5,65,3,1])
2:a= np.ones((2,2))
3:a = np.eye(8)    np.full(shape,value) 初始指定值得数组
4:a = np.logspace(1,2,12)
5:a = np.linspace(1,2,12)
6:a = np.fromstring(s,dtype=np.int8,count=8)
7:a = np.fromfunction(lambda x,y:(x+1)*(y+1),(9,9))
8:a = np.random.randint(1,10,size=(4,3))
      ex: np.random.normal(a,b,size)  正太分布随机数 a=0,b=1.0 为标准正太发布
      //http://www.mamicode.com/info-detail-507676.html
8:a= np.vstack((a,b))//hstack  拼接数组
8:b= np.vsplit/hsplit    切割数组
9:a = np.exp(a)  对 e进行指数计算
10:a = np.sum()/min/max
11: x= np.ogrid[0:5]// x,y = np.ogrid[0:10:1,0:1:10j]   默认产生的数组为shape = (-1,1)   x=np.arange(0,10,1) y = np.linespace(1,1,10)
12: x = np.add/subtract/multiply/(true_divide/floor_divide) (x,y,out) 加减乘除
13: x = np.hsplit(水平分割沿着y方向)    vsplit(垂直分割沿着x方向)
           dsplit(深度分割)
           split(分割,axis=0/1)
14:x = np.dot(a,b)
15:x.save/load 等 数组保存读取 文件操作




1:b.shape= (6,)  改变大小
1:b.ndim   维度 =len(shape)
2:a.reshape((-1,1)).repeat(9,axis=1)  重复操作
3:a.sum(axis=0/1)//a.min()//a.max()  计算某个方向上的
4:a.copy()  得到完全不同的一个数组
5: a.transpose()矩阵操作 (.T)
6:arr.item(index/(m,n)) 得到值
7:arr.itemset(index,value)
8: arr.ravel() 得到一维数组 [......]
"""

"""
    ------------   y
|               (0,9)
|
|
|
| (4,0)
x


"""

# 创建数组

a = np.array([1,23,4,5,65,3,1])
b = np.array([[1.0,2],[1,432],[313,43]])
print a
print b
# 得到数组类型
print a.dtype
print b.dtype

# 得到数组大小
print a.shape
print b.shape   # (3, 2) 三行  两列

#  改变数组大小
b.shape= (6,)
print b
b.shape = 2,-1   # -1 自动计算  -1,3
print b

print "ones 创建 数值都为1 的数组"

a= np.ones((2,2))
print a

print "eye  产生 N*N 二维数组  除了斜线 \ 为1   其他都为0"

a = np.eye(8)
print a



print "改变数组大小  并创建新的数组  但是共享内存"
c = b.reshape((2,-1))
print c
c[0,1]=100
print b

print "创建数组 并指定类型"
d = np.array([[1,212,21],[43,43,543]],dtype=np.complex)
print d


print "========通过方法 创建数组 arange()"
#   初始 终结 步长
a =  np.arange(1,10)
print a
a =  np.arange(0,1,0.1)
print a

print "========通过方法 创建数组 linspace()"
#  初始  终结  个数
a = np.linspace(1,2,12)
print  a

print "========通过方法 创建数组 logspace()"

#  初始10^1  终结10^2  个数 得到等比数列
"""
 logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None):
"""
a = np.logspace(1,2,12)
print  a

print "========通过方法 创建数组 fromstring() 得到数组"

s = "abcdesaHUIS    L"
a = np.fromstring(s,dtype=np.int8,count=8)
print a

ss = '1,431,21,212,12,12,12,1,2'
a=np.fromstring(ss,dtype=int,sep=",")
print a


print "========通过方法 创建数组 fromfunction() 得到数组"
def func(i):
    return i+1000

#  func函数    (19,21)(行,列)   --->(0,0) (0,1).....(18,20)
#     shape 对于func参数个数
a = np.fromfunction(func,(10,))  #
print a

a = np.fromfunction(lambda x,y:(x+1)*(y+1),(9,9))
print a

print "合并数组"
# 纵向合并
a = np.random.randint(1,10,(4,2))
b = np.random.randint(1,10,(4,2))
print  np.vstack((a,b))
print  np.hstack((a,b))

print "随机数组"

a =  np.random.rand(10)      # 0-1的数     一维 10个        rand(3,2)  0-1  3行 2列
print a
a = np.random.randint(1,10,size=(4,3))
print a

print "exp"
a = np.array([[1,2,3],[1,2,3],[1,2,3]])
a = np.exp(a)
print a




print "     =======================数组的自带操作=======================    "
print "数组的重复操作"
a = np.arange(1,10)
# print  a
# [
#  [0]
#  [1]
# ]
"""
    0
    0
    0
    1
    1
    1
# axis = 0  y轴
"""
"""
    0 0 0
    1 1 1
#  axis = 1 x轴
"""


print a.reshape((-1,1)).repeat(9,axis=1)

print "sum求和,min  max  指定x轴  y 轴"
a = np.arange(0,10)
print a.sum()
a = np.array([[1,2,3],[1,2,3],[1,2,3]])
"""
    1,2,3
    1,2,3
    1,2,3
"""
print a.sum(axis=0)#   |
print a.sum(axis=1)#   ——


a=  np.array([[[0,1,2],[3,4,5],[6,7,9],[9,10,11]],[[0,1,2],[3,4,5],[6,7,9],[9,10,11]]]).T
print a
print a.shape  # (3,4,2)  (最里层个数,....,最外层个数)
"""
[
    [
        [0,0]
        []
    ]
    ,
    [


    ]
    ,
    [

    ]
    .....
]

"""
