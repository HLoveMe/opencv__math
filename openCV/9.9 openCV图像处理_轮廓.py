# -*- coding: utf-8 -*-
import numpy as np
import matplotlib as mat
import matplotlib.pyplot as plt
import cv2

"""

• 为了更加准确  使用二值化图像。在寻找 廓之前     值化处理
或者 Canny  界检测。
• 查找 廓的函数会修改原始图像。如果你在找到 廓之后 想使用原始图
   像的  你应 将原始图像存储到其他变 中。
• 在 OpenCV 中 查找 廓就像在黑色背景中找白色物体。你找的物体应是白色而背景应是黑色。

"""

"""
    cv2.findContours(image, mode, method[, contours[, hierarchy[, offset]]]) → contours, hierarchy
    在计算过程 会在原图上修改  请自行保存原图

    image:单通道图片(二值化,Canny界检测)
    mode:
        cv2.RETR_EXTERNAL 表示只检测外轮廓
        cv2.RETR_LIST 检测的轮廓不建立等级关系
        cv2.RETR_CCOMP 建立两个等级的轮廓，上面的一层为外边界，里面的一层为内孔的边界信息。如果内孔内还有一个连通物体，这个物体的边界也在顶层。
        cv2.RETR_TREE 建立一个等级树结构的轮廓。
    method:
        cv2.CHAIN_APPROX_NONE 存储所有的轮廓点，
        cv2.CHAIN_APPROX_SIMPLE 压缩水平方向，垂直方向，对角线方向的元素，只保留该方向的终点坐标，例如一个矩形轮廓只需4个点来保存轮廓信息


    contours:list[np.ndarray]
    hiararchy结果，这是一个ndarray，其中的元素个数和轮廓个数相同，
            每个轮廓contours[i]对应4个hierarchy元素hierarchy[i][0] ~hierarchy[i][3]，
            分别表示后一个轮廓、前一个轮廓、父轮廓、内嵌轮廓的索引编号，如果没有对应项，则该值为负数。



    形态梯度:也可以找到边缘
        cv2.morphologyEx(img,cv2.MORPH_GRADIENT,ker)

"""
def AA(a="查找轮廓"):
    im = cv2.imread("./mm.jpg")
    new = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    #去噪点
    new=cv2.GaussianBlur(new, (5, 5), 0)
    # 二值化
    ret,new = cv2.threshold(new,150,255,cv2.THRESH_BINARY_INV)
    cv2.imshow("A", new)

    contours, hierarchy =   cv2.findContours(new,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # contours = sorted(contours,key=lambda one:len(one),reverse=True)
    cv2.drawContours(im,contours,3,(255,0,0),thickness=1)
    cv2.imshow("B", im)
    cv2.waitKey(0)


def BB(a="查找轮廓"):
    im = cv2.imread("./jd.jpg")
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    #先去除噪点
    gray = cv2.medianBlur(gray,5)
    #二值化  黑色背景
    ret,new = cv2.threshold(gray,200,255,cv2.THRESH_BINARY_INV)
    cv2.imshow("Q",gray)
    cv2.imshow("AA",new)

    cons, h = cv2.findContours(new, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(im,cons,-1,(0,0,255),1)
    print len(cons)
    cv2.imshow("QAA", im)
    cv2.waitKey(0)


def CC(name="求得重心 周长 面积"):
    im = cv2.imread('./jd.jpg',0)
    im = cv2.medianBlur(im,5)
    ret, new = cv2.threshold(im, 200, 255, cv2.THRESH_BINARY_INV)
    cons, h = cv2.findContours(new, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    res =  cv2.moments(cons[2])
    print res
    cx = int(res['m10'] / res['m00'])
    cy = int(res['m01'] / res['m00'])
    print "重心",cx,cy

    area = cv2.contourArea(cons[2])
    print "面积",area

    per = cv2.arcLength(cons[2], True)

    print "周长",per

def DD():
    "轮廓近似"
    im = cv2.imread('./js.png', 0)
    ax =plt.subplot(221)
    ax.imshow(im,'gray')
    im = cv2.medianBlur(im, 5)

    ret, new = cv2.threshold(im, 200, 255, cv2.THRESH_BINARY)

    cons, h = cv2.findContours(new, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    im = cv2.imread('./aaa.jpg')
    cv2.drawContours(im,cons,-1,(0,0,255),3)
    ax = plt.subplot(222)
    ax.imshow(im[:,:,::-1])




    print "取近似轮廓"
    """
        轮廓数据,
        指定逼近精度的参数。这是原始曲线与它的近似值之间的最大距离。
        是否是闭合轮廓
    """

    """
        epsilon 决定是否得到自己想要的结果

    """
    arc = cv2.arcLength(cons[0],True)
    #周长的0.1
    res = cv2.approxPolyDP(cons[0],arc*0.1,True)

    im = cv2.imread('./aaa.jpg')
    cv2.drawContours(im,[res],-1,(0,0,255),3)
    ax = plt.subplot(223)
    ax.imshow(im[:,:,::-1])



    # 周长的0.01
    res = cv2.approxPolyDP(cons[0], arc * 0.01, True)
    im = cv2.imread('./aaa.jpg')
    cv2.drawContours(im, [res], -1, (0, 0, 255), 3)
    ax = plt.subplot(224)
    ax.imshow(im[:, :, ::-1])
    plt.show()


def EE(a="得到与轮廓相关的形状"):
    a=1
    """
    boundingRect 得到外包含的矩形
    minAreaRect 得到最小矩形
    minEnclosingTriangle 得到闭合三角形
    minEnclosingCircle  得到外切圆
    """
    im = cv2.imread("./jd.jpg",0)
    im2=cv2.medianBlur(im,5)
    ret, new = cv2.threshold(im2, 200, 255, cv2.THRESH_BINARY)
    cons,h =cv2.findContours(new,cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    print len(cons)

    cv2.drawContours(im,cons,2,(0,0,255),1)
    """
        得到包含轮廓未旋转的矩形
    """
    x,y,w,h= cv2.boundingRect(cons[2])
    cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,255))

    """
        得到包含轮廓最小的矩形 有旋转的
        ((x,y),(w,h),角度)
    """
    box =  cv2.minAreaRect(cons[2])
    #得到矩形四个点
    res = cv2.cv.BoxPoints(box)

    for i in range(len(res)):
        if i==3:
            cv2.line(im, (int(res[3][0]),int(res[3][1])), (int(res[0][0]),int(res[0][1])), (0, 0, 255), 1)
        else:
            cv2.line(im, (int(res[i][0]),int(res[i][1])),(int(res[i+1][0]),int(res[i+1][1])),(0,0,255),1)

    """
        外切圆  minEnclosingCircle
        中点  半径
    """
    res = cv2.minEnclosingCircle(cons[2])
    cv2.circle(im,(int(res[0][0]),int(res[0][1])),int(res[1]),(0,0,255),1)



    """
        内切椭圆
        中点,长短轴,旋转角度
    """
    res = cv2.fitEllipse(cons[2])
    cv2.ellipse(im, res, (0, 0, 255), 2)
    cv2.imshow("A",im)
    cv2.waitKey(0)


def FF(a="凸缺陷"):
    a=1
    """"
        • points 我们 传入的 廓
        • hull  输出
        • clockwise 方向标志。如果 置为 True  出的凸包是 时 方向的。 否则为 时 方向。
        • returnPoints   值为 True。它会 回凸包上点的坐标。如果 置 为 False 就会 回与凸包点对应的 廓上的点。
    return
        returnPoints:
            True:得到的是点集合
            Fasle:得到的是轮廓中的索引集合

            .      .
            /\    /\
           /  \  /  \
          /    \/    \

    """

    im = cv2.imread("./lx.jpg",0)
    im = cv2.medianBlur(im,5)
    ret ,new = cv2.threshold(im,230,255,cv2.THRESH_BINARY_INV)
    cons,h=cv2.findContours(new,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    #得到凸性缺陷点 在轮廓中索引集合
    """
        [[[ 544  671  609 5769]]
        [[   0  128   57 5751]]
        [[ 131  265  189 5859]]
        [[ 265  409  334 5632]]
        [[ 409  540  480 6037]]]

        个数为 凸性缺陷点的个数
        (a,b,c,d)
            a,b,c 分别是三个点 在轮廓集合中的索引  d 是 distance between the farthest point and the convex hull

            a      b
            /\    /\
           /  \  /  \
          /    \/    \
                c
    """
    hull = cv2.convexHull(cons[1],returnPoints=False)
    print len(cons[1])
    print hull
    for i in range(len(hull)):

        print cons[1][hull[i]]  #得到具体点

    defects = cv2.convexityDefects(cons[1], hull)


    im = cv2.imread("./lx.jpg")
    for i in range(len(defects)):
        a,b,c,d=defects[i][0]
        one=cons[1][a][0]
        two=cons[1][b][0]
        #划线
        cv2.line(im,(one[0],one[1]),(two[0],two[1]),(255,0,0),1)
        #瞄点
        point =  cons[1][c][0]
        cv2.circle(im,(point[0],point[1]),4,(0,255,0),-1)

    cv2.imshow("A",im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pass

FF()
