# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.colors
import matplotlib.pyplot as plt
import cv2
"""
    进行几何变换时   size/np=(宽,高)

"""

im = cv2.imread("./c.jpg")
def AAA():
    """
           缩放
    """
    height, width = im.shape[:2]
    new=cv2.resize(im,dsize=None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
    # new = cv2.resize(im, (height * 2, width * 2), interpolation=cv2.INTER_CUBIC)
    cv2.imshow("A",im)
    cv2.imshow("放大缩小", new)
    cv2.waitKey(100000)

def BB():
    x = 100
    y = 50
    """
        cv2.warpAffine(im,M,size)
        源,平移位置,输出图片大小(宽,高)
        [
            1,0,x
            0,1,y
        ]

    """
    M = np.float32([[1, 0, x], [0, 1, y]])
    # 变化函数  根据M类型进行不同变换
    tar = cv2.warpAffine(im, M, im.shape[:2][::-1])
    cv2.imshow("平移", tar)
    cv2.waitKey(100000)


def CC():
    rows,cols,channel=im.shape
    # 得到变换矩阵
    """
        旋转点,角度(逆时针),缩放比例
    """
    M = cv2.getRotationMatrix2D((cols/2,rows/2),-45,1)
    dst = cv2.warpAffine(im,M,(cols,rows))
    cv2.imshow("旋转", dst)
    cv2.waitKey(100000)

def DD():
    global  im
    im = im[:, :, ::-1]
    cols,rows , channel = im.shape
    """
        仿射变化 会改变图片旋转
    """

    # 得到原始点
    old = np.float32([[50,50],[200,50],[50,200]])
    # 仿射变化之后的点
    new = np.float32([[10,100],[190,40],[100,235]])

    # 得到变化矩阵
    M =  cv2.getAffineTransform(old,new)

    # 进行变化
    dst = cv2.warpAffine(im,M,(cols,rows))

    ax1 = plt.subplot(121)
    ax1.imshow(im)
    ax1.set_title("AA")
    ax2= plt.subplot(122)
    ax2.imshow(dst)
    plt.show()

def FF():
    im=cv2.imread("./pk.jpg")
    """
        透视变化:
            将图片投影到一个新的视平面(ViewingPlane)，也称作投影映射
    """
    # 取的变换的四点  任意三点不在一个直线上
    old = np.float32([[183,71],[164,155],[308,105],[283,184]])
    new = np.float32([[0, 0], [0,300], [ 500,0], [ 500,300]])
    #得到透视变化矩阵
    M = cv2.getPerspectiveTransform(old,new)
    """
        进行透视变换
    """
    dst = cv2.warpPerspective(im,M,(500,300))
    ax1 = plt.subplot(211)
    ax1.imshow(im)
    ax2=plt.subplot(212)
    ax2.imshow(dst)
    plt.show()

AAA()