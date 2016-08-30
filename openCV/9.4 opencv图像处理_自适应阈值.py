# -*- coding: utf-8 -*-
import numpy as np
import matplotlib as mat
import matplotlib.pyplot as plt
import cv2

im = cv2.imread("./sd.jpg")
"""
        不同的阈值算法对不同的图片效果不同
"""
"""
Adaptive Method- 指定计算阈值的方法。
– cv2.ADPTIVE_THRESH_MEAN_C:阈值取自相邻区域的平 均值
– cv2.ADAPTIVE_THRESH_GAUSSIAN_C:阈值取值相邻区域 的加权和,权重为一个高斯窗口。
• Block Size - 邻域大小(用来计算阈值的区域大小)。
• C - 这就是是一个常数,阈值就等于的平均值或者加权平均值减去这个常数。
"""

gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

ax1 =plt.subplot(221)
ax1.imshow(gray,'gray')

ret,new1 =  cv2.threshold(gray,130,255,cv2.THRESH_BINARY)
ax2 =plt.subplot(222)
ax2.imshow(new1,'gray')


# cv2.ADAPTIVE_THRESH_MEAN_C  取相邻的平均值
# cv2.ADAPTIVE_THRESH_GAUSSIAN_C 取相邻加权和
"""
    源,最大值,自适应阈值如何选取,该点的显示处理方式,自适应阈值选取的范围, 得到结果后-2
    exam:
         cv2.ADAPTIVE_THRESH_MEAN_C--->求得平均值-->阈值

         cv2.THRESH_BINARY-->得到该点处理之后的值


"""
new2 = cv2.adaptiveThreshold(gray, 255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11, 2)
ax3 =plt.subplot(223)
ax3.imshow(new2,'gray')

new3 = cv2.adaptiveThreshold(gray, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11, 2)
ax4 =plt.subplot(224)
ax4.imshow(new2,'gray')


plt.show()