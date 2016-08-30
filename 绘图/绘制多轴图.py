# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

"""

    Figure,Axies=subplot(rows,cols,index) 默认(111)
    1,2
    3,4
    5,6
    =>subplot(324)===subplot(3,2,4)
"""
a=True
if  not a:
    for i, color in enumerate('rgbyck'):
        plt.subplot(320 + i + 1, axisbg=color)
        "调节间距"
        # plt.subplots_adjust(0-1)
    plt.legend()
    plt.show()
else:
    plt.subplot(221) # 第一行的左图
    plt.subplot(222) # 第一行的左图
    plt.subplot(212) # 第二整行
    plt.legend()
    plt.show()

    plt.subplot(121)
    plt.subplot(222)
    plt.subplot(224)
    plt.show()


