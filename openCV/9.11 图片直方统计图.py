# -*- coding: utf-8 -*-


import numpy  as np
import cv2
import matplotlib.pyplot as plt

"""
直方图数据:

def calcHist(images, channels, mask, histSize, ranges, hist=None, accumulate=None):

images: 源图片数组 [a,b,c]
channels:  [0]  表示灰度图
           [0],[1],[2]  彩色图  分别为 B,G,R
mask 掩码 必须有相同的size  如果只对部分进行统计 可以制作掩码
histSize:表示Bin数目 表示用多少点显示
        [256]   表示用  x [0-256]  如果统计所有像素点 表示一个x对应一个
        [16]           x [0-16]   如果统计所有像素点 表示  x B表示 256/16 个像素点的数量

ranges:统计的像素点点范围: [0,256]

得到 [0个数,1像素个数,.... ]

"""
im =  cv2.imread("./mm.jpg",0)
a = cv2.calcHist([im],[0],None,[256],[0,256])
# b = cv2.calcHist([im],[0],None,[25],[0,256])

"""
绘制直方图
    plt.hist()

"""
# 需要统计的数组
# data = im.ravel()
# 柱状图
# plt.hist(data,256,[0,256])
# plt.xlim(0,255)
# plt.ylim(0,2000)
# plt.show()



im = cv2.imread("./mm.jpg")
color=('b','g','r')



plt.xlim(0,300)
plt.ylim(0,2000)
for i ,color in enumerate(color):
    print i,color
    # 得到直方图数据
    """
        彩色图
        [0]--->b
        [1]--->g
        [2]--->r
    """
    hsi = cv2.calcHist([im],[i],None,[256],[0,256])
    plt.plot(hsi,color)
plt.show()


