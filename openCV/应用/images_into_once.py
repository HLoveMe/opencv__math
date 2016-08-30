# -*- coding: utf-8 -*-
import numpy as np
import cv2

"""
    本例子实现图片签名的合并

    1:签名应该为纯黑色 255

    2:进行二值化时 选定的阈值为 254  原签名图片不应该包含纯黑色点

    3:需要的图片源为 (原图图片,多张签名图片)
"""


#原图
source=cv2.imread('/Users/zhuzihao/PycharmProjects/科学计算/openCV/应用/wei.png')
#签名图片
img_one=cv2.imread("/Users/zhuzihao/PycharmProjects/科学计算/openCV/应用/yuan1.png")+255
img_two=cv2.imread("/Users/zhuzihao/PycharmProjects/科学计算/openCV/应用/yuan2.png")+255

#判断源的大小是否一致
if img_one.shape!=img_two.shape:
    raise  Exception("图片源的shape必须一致")

#滤波
img1=cv2.medianBlur(img_one,5)
img2=cv2.medianBlur(img_two,5)

#灰度图片
img1 =  cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
img2 =  cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

#二值化
ret1,img1 = cv2.threshold(img1,254,255,cv2.THRESH_BINARY)
ret2,img2 = cv2.threshold(img2,254,255,cv2.THRESH_BINARY)

#mask
mask = img1 + img2

#查找轮廓
cons, h = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

#画实心轮廓
if source.shape!=img_one.shape:
    size = img_one.shape
    source=cv2.resize(source, dsize=(size[1],size[0]), interpolation=cv2.INTER_CUBIC)
    cv2.drawContours(source,cons,-1,(0,0,0),thickness=-1)
    cv2.imshow("Image",source)
    #输出
    # cv2.imwrite('./new_image.png',source)
    cv2.waitKey(0)
else:
    pass

