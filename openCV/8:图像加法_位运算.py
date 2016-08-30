# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.colors
import matplotlib.pyplot as plt
import cv2
"""
 注意:OpenCV 中的加法与 Numpy 的加法是有所不同的。
 OpenCV 的加法 是一种饱和操作  250+10=260-->255
 Numpy 的加法是一种模操作。    250+10=260-->4



 http://blog.csdn.net/jnulzl/article/details/47129887

 1:相加
 2:非运算
        0--->255
        255-->0
        100-->155
        155-->100
    cv2.bitwise_not(mask)
 3:异或
   cv2.bitwise_xor(Rectangle,Circle,mask=msak)

 4:或
     cv2.bitwise_or(Rectangle,Circle,mask=msak)

  5:and
    cv2.bitwise_and(Rectangle,Circle,mask=msak)


   mask=msak:
    make.shape=(im.shape[0],im.shape[1])
    mask:[[0,0,255,255,255..],
          [],
          []
          ...
         ]
    进行为运算时 mask 表示对原图 只在255值得位置进行and运算  0:地方值为 0


"""

print "图像相加"
#
# """
#     img = cv2.addWeighted(one,比例,two,比例,n)
#     one*比+two*(1-比) + n
# """
# img = cv2.addWeighted(img1,0.7,img2,0.3,0)
# cv2.imshow("A",img)
# cv2.waitKey(0)


print "位运算   uint8"


bg = cv2.imread('./a.jpg')
logo = cv2.imread('./logo.png')
logo = cv2.resize(logo,(60,74))
rows,cols,channel=logo.shape
#copy副本
roi = bg[0:rows,0:cols]

#原图进行灰色处理
img1gray = cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)

#二值处理   黑0白255两色
ret,mask = cv2.threshold(img1gray,175,255,cv2.THRESH_BINARY)

print mask
# 取 and
img1_bg = cv2.bitwise_and(roi,roi,mask = mask)

#取反操作
mask_inv = cv2.bitwise_not(mask)

img2_fg = cv2.bitwise_and(logo,logo,mask=mask_inv)

dst = cv2.add(img2_fg,img1_bg)

bg[0:rows, 0:cols ] = dst



def image_subjoin_logo(bgs,logo,loc=None,size=None,out=None):
    """
    :param bgs: 背景图
    :param logo: logo
    :param loc: logo起点位置 (0,0)
    :param size: optioal logo大小 设置会调整大小
    :param out:out 保存的文件路径
    :return: 返回图片
    """
    import  os
    if (os.path.isfile(bgs) or bgs is file) and (os.path.isfile(logo) or logo is file):
        logo = cv2.imread(logo)
        bg = cv2.imread(bgs)
        if loc is None:
            loc=(0,0)
        if size==None:
            size= (logo.shape[0],logo.shape[1])
            if size[0]>bg.shape[0] or size[1]>bg.shape[1]:
                print "背景图片尺寸 和 logo图片尺寸不匹配 logo尺寸太大"
                return None
        else:
            if size[0] > bg.shape[0] or size[1] > bg.shape[1]:
                print "背景图片尺寸 和 logo图片尺寸不匹配 size 参数不准确"
                return None

        logo=cv2.resize(logo,(size[1],size[0]))

        #调整loc参数
        locx=0
        locy=0
        if loc[0]+size[0]>bg.shape[0]:
            locy = bg.shape[0] - size[0]
        if loc[1] + size[1] > bg.shape[1]:
            locx = bg.shape[1] - size[1]

        roi = bg[locy:size[0]+locy,locx:size[1]+locx]
        print roi.shape
        grayimg = cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)
        ret,mask = cv2.threshold(grayimg,175,255,cv2.THRESH_BINARY)

        logo1 =  cv2.bitwise_and(roi,roi,mask=mask)

        mask_in = cv2.bitwise_not(mask)

        logo2 = cv2.bitwise_and(logo,logo,mask=mask_in)

        logo = cv2.add(logo1,logo2)

        bg[locy:size[0]+locy,locx:size[1]+locx]=logo

        if out:
            cv2.imwrite(out,bg)
        return bg


# image_subjoin_logo('./a.jpg','./logo.png',loc=(1000,1000),size=(74,60),out='./new.png')


