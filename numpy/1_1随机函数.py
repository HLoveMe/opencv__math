# -*- coding: utf-8 -*-
import numpy as np



# 得到shape=4,3,2 的数组 0.0 - 1.0
print np.random.rand(4,3,2)
# 得到1-10 shape=size的数组
print np.random.randint(1,10,size=(4,4))


# 通过随机种子得到随机数
png = np.random.RandomState(123)  #局部种子
print  png.randint(1,10,size=(2,2))
"""
    prng.chisquare(1, size=(2, 2)) # 卡方分布
    prng.standard_t(1, size=(2, 3)) # t 分布
    prng.poisson(5, size=10) # 泊松分布
"""

print "#设置全局种子"
# np.random.seed(1)



print "高级随机生成数据函数"
# 二项分布
# 每次n次 一次的0.5的概率 返回成功的 次数
print np.random.binomial(9,0.5,size=(2,2))
# 正态分布函数
values = np.random.normal(1000)


import numpy.linalg