# -*- coding: utf-8 -*-
import numpy as np
import matplotlib as mat
import matplotlib.pyplot as plt
import cv2

"""
    OpenCV 提供了三种不同的梯度滤波器,或者说高通滤波器:Sobel, Scharr 和 Laplacian。我们会意义介绍他们。

    Sobel/Scharr 其实就是求一阶或二阶导数。Scharr 是对 Sobel(使用 小的卷积核求解求解梯度角度时)的优化。
    Laplacian 是求二阶导数。

    当滤波指定深度之后 得到的效果不同
    可使用 laplacian=cv2.convertScaleAbs(laplacian) 转为np.uint8
    当装为uint8颜色可能被截取
"""

def AA():
    im = cv2.imread("./sz.jpg",0)
    """
        dx,dy表示x,y轴几次求导 ksize=卷积核奇数 1,3,5,7 --> 5,5
        Sobel(src, ddepth, dx, dy, dst=None, ksize=None, scale=None, delta=None, borderType=None): # real signature unknown; restored from __doc__
    """
    new_x = cv2.Sobel(im,cv2.CV_64F,1,0,ksize=5)

    new_y = cv2.Sobel(im,cv2.CV_64F,0,1,ksize=5)
    """
      Laplacian(src, ddepth, dst=None, ksize=None,...)

    """
    im=cv2.GaussianBlur(im,(5,5),0)
    laplacian = cv2.Laplacian(im,cv2.CV_64F)

    # cv2.imshow("KK",laplacian)
    plt.subplot(2, 2, 1), plt.imshow(im, cmap='gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray')
    plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 3), plt.imshow(new_x, cmap='gray')
    plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 4), plt.imshow(new_y, cmap='gray')
    plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])


    cv2.imshow("A",cv2.addWeighted(new_x,0.5,new_y,0.5,0))
    cv2.waitKey(0)
    plt.show()

def CC():
    im = cv2.imread("./pk.jpg",0)
    im = cv2.GaussianBlur(im,(5,5),0)
    im=cv2.Laplacian(im,-1,ksize=5)
    cv2.imshow("A",im)
    cv2.waitKey(0)
    pass
AA()