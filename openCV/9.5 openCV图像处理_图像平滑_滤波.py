# -*- coding: utf-8 -*-
import numpy as np
import matplotlib as mat
import matplotlib.pyplot as plt
import cv2


"""
对 2D 图像实施低通滤波(LPF),高通滤波 (HPF)等。
-->LPF 帮助我们去除噪音,模糊图像。
-->HPF 帮助我们找到图像的边缘


src.depth() = CV_8U,         ddepth = -1/CV_16S/CV_32F/CV_64F
src.depth() = CV_16U/CV_16S, ddepth = -1/CV_32F/CV_64F
src.depth() = CV_32F,        ddepth = -1/CV_32F/CV_64F
src.depth() = CV_64F,        ddepth = -1/CV_64F


filter2D(src, ddepth, kernel, dst=None, anchor=None, delta=None, borderType=None): # real signature unknown; restored from __doc__
    低通滤波:平滑图像
        归一化块滤波器(平均)
            cv2.boxFilter(img,-1,(n,n))//源,-1表示输出和原图像深度一致,核
            cv2.blur(img,(n,m))
        中值滤波-去除噪音:
            cv2.medianBlur(image,n) /n核的大小 5
        高斯滤波:
            cv2.GaussianBlur(img,(n,n),0)  //X方向上的高斯核标准偏差。
            某个像素点 受到的影响 离得越远 影响越小
        双边滤波（Bilateral filter) 双边滤波同时使用了空间高斯权重和灰度相似性高斯权重
            可以保边去噪的滤波器
            cv2.bilateralFilter(img,d,’p1’,’p2’)
            函数有四个参数需要，d是领域的直径，后面两个参数是空间高斯函数标准差和灰度值相似性高斯函数标准差
"""


"""
    LPF
"""
def AA(title='同一滤波'):
    im = cv2.imread("./logo.png")
    kernel = np.ones((5,5),np.float32)/25
    dst = cv2.filter2D(im,-1,kernel=kernel)

    plt.subplot(121), plt.imshow(im), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(dst), plt.title('Averaging')
    plt.xticks([]), plt.yticks([])
    plt.show()
    cv2.blur()

def BB(name='归一化'):
    im = cv2.imread("./c.jpg")
    new1 = cv2.blur(im,(5,3))
    new2 = cv2.boxFilter(im,-1,(5,5))
    cv2.imshow("A",new1)
    cv2.imshow("B", new2)
    cv2.waitKey(0)
    pass

def CC(name="中指滤波"):
    im = cv2.imread('./a.jpg')
    for i in range(1000):
        rows = int(np.random.rand()*im.shape[0])
        cols = int(np.random.rand() * im.shape[1])
        if im.ndim==3:
            im[rows][cols]=[255,255,255]
        else:
            im[rows][cols] = 255
    cv2.imshow("A",im)

    new = cv2.medianBlur(im,5)
    cv2.imshow("B",new)
    cv2.waitKey(0)

BB()

