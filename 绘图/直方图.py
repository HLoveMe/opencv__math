# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path


fig, ax = plt.subplots()

# 得到正太分布数据(不会重复)    size:个数
"""
      个数/\
          |
          |正太分布
          |
          |
    ------|-------->  值
          |
"""
data = np.random.randn(1000)
#  产生直方图数据  数据  bins:分为多少份  range:表示x轴范围(a.min(),a.max())  normed是否为标准正太分布
# histogram(a, bins=10, range=None, normed=False, weights=None, density=None):

# return  bins:ndarray x表示取的点 len = bins+1    [-2.2,-2.0....1.9,2.1] n+1个
#   直方图其实是一个一个Rect组合成的  10个直方图 需要 11个长边  | |

# return  n:ndarray 表示 [-2.2 -2.0] 范围类  a 中数据的个数....       n之和为size
# (normed=True the result is the value of the probability)
n, bins = np.histogram(data, 50)

# 直方体 所有左边 x
left = np.array(bins[:-1])
# 直方体 所有右边 x
right = np.array(bins[1:])
# 直方体 所有底部 y
bottom = np.zeros(len(left))
# 直方体 所有顶部 y
top = bottom + n


# 得到每个直方体的路径 数组表示
# shape = (size,4,2)
#  [[[]]] 直方图个数-->直方体-->直方体四个点-->点[左下,左上 右上 右下]
""""
    T   矩阵操作 transpose()
"""
XY = np.array([[left, left, right, right], [bottom, top, top, bottom]]).T

#  得到路径  Path
barpath = path.Path.make_compound_path_from_polys(XY)
#
patch = patches.PathPatch(
    barpath, facecolor='blue', edgecolor='gray', alpha=0.8)
print patch
# 增加
ax.add_patch(patch)   #  matplotlib.patches.Patch

ax.hist()

# x范围
ax.set_xlim(left[0], left[-1])
# y的范围
ax.set_ylim(bottom.min(), top.max())

# 显示
plt.show()



# print "======简化======"
#
# import numpy
# import pylab
# # mu, sigma = 2, 0.5   #正态分布函数  参数
# mu, sigma = 2, 0.5   #标准正态分布函数  参数
# v = numpy.random.normal(mu,sigma,1000)
# pylab.hist(v, bins=50, normed=True)
# pylab.show()