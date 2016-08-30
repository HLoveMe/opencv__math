# -*- coding: utf-8 -*-
import numpy as np
import matplotlib as mat
import matplotlib.pyplot as plt
import cv2


"""
    形态学操作是根据图像形状进行的简单操作。
    一般情况下对二值化图像进 行的操作

    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))//cv2.MORPH_RECT/cv2.MORPH_ELLIPSE/cv2.MORPH_CROSS

    腐蚀:
        cv2.erode(src,结构化元素)
        这对于去除 白噪声很有用,也可以用来断开两个连在一块的物体等
    膨胀:
        cv2.dilate()
        一般在去 噪声时先用腐蚀再用膨胀.膨胀也可以用来连接两个分开的物体。

    开运算:先进性腐蚀再进行膨胀 去除白点
    闭运算:先膨胀再腐蚀   去除黑点
        cv2.morphologyEx(img,cv2.MORPH_OPEN/ cv2.MORPH_CLOSE,ker)

    形态学梯度:结果看上去就像前景物体的轮廓。
        cv2.morphologyEx(img,cv2.MORPH_GRADIENT,ker)
"""


def AA():
    im = cv2.imread('./test.png')
    ker = np.ones((3,3),np.uint8)
    new = cv2.erode(im,ker)
    cv2.imshow("原",im)
    cv2.imshow("腐蚀",new)
    cv2.waitKey(0)



def BB():
    im = cv2.imread("./test.png")
    ker = np.ones((3, 3), np.uint8)
    new = cv2.dilate(im,ker)
    cv2.imshow("A",im)
    cv2.imshow("new",new)
    cv2.waitKey(0)

def CC(name="形态学梯度"):
    im = cv2.imread("./test.png")
    ker = np.ones((3, 3), np.uint8)
    new = cv2.morphologyEx(im,cv2.MORPH_GRADIENT,ker)
    cv2.imshow("A", im)
    cv2.imshow("new", new)
    cv2.waitKey(0)
CC()