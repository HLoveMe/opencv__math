# -*- coding: utf-8 -*-
import numpy as np
import matplotlib as mat
import matplotlib.pyplot as plt
import cv2

"""
        源,阈值 指定值,模式
        ret,mask = cv2.threshold(img,175,255,cv2.THRESH_BINARY)

        THRESH_BINARY = 0L
                 指定值    source(x,y)>阈值
            n =
                   0            其他
        THRESH_BINARY_INV = 1L
                    0       source(x,y)>阈值
            n =
                  指定值          其他

        THRESH_TRUNC

                 指定值           source(x,y)>指定值
            n =
                source(x,y)        其他

        THRESH_TOZERO = 3L
                  source(x,y)      source(x,y)>阈值
            n =
                       0                其他
        THRESH_TOZERO_INV = 4L

                  source(x,y)           其他
            n =
                       0               source(x,y)>阈值
"""

def AA():
    im = cv2.imread("./logo.png")

    rows, cols, c = im.shape
    """
        转灰色图
    """
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    ax1 = plt.subplot(321)
    ax1.imshow(gray, 'gray')
    plt.title("gray")
    plt.xticks([])
    plt.yticks([])
    """
        阈值  1
    """
    ret, new1 = cv2.threshold(gray, 175, 255, cv2.THRESH_BINARY)

    ax2 = plt.subplot(322)
    ax2.imshow(new1, 'gray')
    plt.title("THRESH_BINARY")
    plt.xticks([])
    plt.yticks([])

    """
        阈值  2
    """
    ret, new1 = cv2.threshold(gray, 175, 255, cv2.THRESH_BINARY_INV)

    ax3 = plt.subplot(323)
    ax3.imshow(new1, 'gray')
    plt.title("THRESH_BINARY_INV")
    plt.xticks([])
    plt.yticks([])

    """
        阈值  3
    """
    ret, new1 = cv2.threshold(gray, 175, 255, cv2.THRESH_TRUNC)

    ax4 = plt.subplot(324)
    ax4.imshow(new1, 'gray')
    plt.title("THRESH_TRUNC")
    plt.xticks([])
    plt.yticks([])

    plt.show()


def OTSU():
    """
        使用系统默认的最优阈值
    """
    im = cv2.imread("./sd.jpg")

    rows, cols, c = im.shape
    """
        转灰色图
    """
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    """
        设置最低为0
        在处理方法后加上cv2.THRESH_OTSU
        返回值:ret 就是阈值  (设置后就是设置的  没有设置就是计算出来的最优)
    """

    ret1, new1 = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY)

    ret2,new2=cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    print ret1,ret2
    ax1=plt.subplot(121)
    ax1.imshow(new1,"gray")

    ax2 = plt.subplot(122)
    ax2.imshow(new2,'gray')
    plt.show()

OTSU()
