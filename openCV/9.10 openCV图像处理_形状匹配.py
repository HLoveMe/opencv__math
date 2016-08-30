
# -*- coding: utf-8 -*-
import numpy as np
from matplotlib.pylab import plt
import cv2

def AA():
    st1=cv2.imread("./star1.jpg",0)
    st2=cv2.imread("./star2.jpg")
    st3=cv2.imread("./star3.jpg", 0)

    st2 = cv2.medianBlur(st2,5)

    st2 = cv2.cvtColor(st2,cv2.COLOR_BGR2GRAY)

    ret,st1=cv2.threshold(st1,175,255,cv2.THRESH_BINARY_INV)

    ret,st3=cv2.threshold(st3,175,255,cv2.THRESH_BINARY_INV)

    # ret, st2 = cv2.threshold(st2, 230, 255, cv2.THRESH_BINARY_INV)
    """
        由于第二张图片不能  直接进行二值化  阈值 不好确定
        这里先对灰度图 进行图形梯度查找 找到边缘图像   //Canny边缘检测
        在进行二值化 在进行轮廓查找
    """
    #使用轮廓梯度 得到图像轮廓
    ker = np.ones((3, 3), np.uint8)
    st2 = cv2.morphologyEx(st2, cv2.MORPH_GRADIENT, ker)
    #再次进行二值化
    ret, st2  = cv2.threshold(st2,18,255,cv2.THRESH_BINARY)
    #进行轮廓查找 会直接在st2上进行修改
    cons_2,h= cv2.findContours(st2,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    cons_2=cons_2[1] # 五星

    cons_1,h = cv2.findContours(st1,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    cons_1=cons_1[0]  #五星

    cons_3, h = cv2.findContours(st3, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    cons_3=cons_3[0]  #菱形

    """
        函数 cv2.matchShape() 可以帮我们比 两个形状或 廓的相似度。如 果 回值 小 匹  好。

        matchShapes(contour1, contour2, method, parameter)
                    轮廓线    轮廓线
        method:计算方式
            method=CV_CONTOURS_MATCH_I1
            method=CV_CONTOURS_MATCH_I2
            method=CV_CONTOURS_MATCH_I3
        parameter:0.0
             Method-specific parameter (not supported now).
    """
    #自己和自己比较
    print cv2.matchShapes(cons_3,cons_3,1,0.0)

    #相似的两个相互比较
    print cv2.matchShapes(cons_2, cons_1, 1, 0.0)
    print cv2.matchShapes(cons_2, cons_1, 3, 0.0)

    #不同的相比较
    print cv2.matchShapes(cons_3, cons_2, 1, 0.0)
    print cv2.matchShapes(cons_3, cons_1, 1, 0.0)






    st1 = cv2.imread("./star1.jpg", 0)
    st1 = cv2.cvtColor(st1, cv2.COLOR_GRAY2BGR)
    st2 = cv2.imread("./star2.jpg")
    st3 = cv2.imread("./star3.jpg", 0)
    st3 = cv2.cvtColor(st3, cv2.COLOR_GRAY2BGR)

    cv2.drawContours(st1, (cons_1,), 0, (0, 0, 255), -1)
    cv2.drawContours(st2, (cons_2,), 0, (0, 0, 255), -1)
    cv2.drawContours(st3, (cons_3,), 0, (0, 0, 255), -1)

    ax = plt.subplot(131)
    ax.imshow(st1[:, :, ::-1])
    ax.set_title("con1")

    ax = plt.subplot(132)
    ax.imshow(st2[:, :, ::-1])
    ax.set_title("con2")

    ax = plt.subplot(133)
    ax.imshow(st3[:, :, ::-1])
    ax.set_title("con3")


    plt.show()

AA()