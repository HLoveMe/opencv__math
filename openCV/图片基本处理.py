
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.colors
import matplotlib.pyplot as plt

import cv2


print "matplotlib 显示图片"
# img = cv2.imread("./a.jpg",0)
# # matplotlib.colors.Colormap
# plt.imshow(img,cmap='gray',interpolation='bicubic')
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.show()


print "框口显示"
# img = cv2.imread("./a.jpg")
# cv2.namedWindow('Image')
# cv2.imshow("Image",img)
# cv2.waitKey(0)
# # cv2.destroyAllWindows()
#
# img=img.copy()
# cv2.imwrite('./aa.jpg',img,[int(cv2.IMWRITE_JPEG_QUALITY),5])
# cv2.imwrite('./aaa.jpg',img,[int(cv2.IMWRITE_JPEG_QUALITY),95])


print "撒盐操作"
# def salt(img,n=8000):
#     # img = (800,600,3)
#     for o in range(n):
#         hang = int(img.shape[0] * np.random.random())
#         colum = int(img.shape[1] * np.random.random())
#         if img.ndim==3:
#             img[hang,colum]=200,0,0
#         else:
#             img[hang,colum]=0
#     return img
# img = cv2.imread("./b.png")
# print img.ndim
# img = salt(img)
# cv2.imshow("Salt",img)
#
#
# emptyimg = np.zeros(img.shape,dtype=img.dtype)
# for i in range(img.shape[0]):
#     for j in range(img.shape[1]):
#         emptyimg[i,j]=img[i][j][0]
# cv2.imshow("empytimg",emptyimg)
# cv2.waitKey(0)


# print  "通道分离"
# img = cv2.imread("./c.jpg")
# b,g,r = cv2.split(img)
# cv2.imshow("Blue", r)
# cv2.imshow("Red", g)
# cv2.imshow("Green", b)
#
#
#
# rr = np.zeros((img.shape[0],img.shape[1]),dtype= img.dtype)
# gg = np.zeros((img.shape[0],img.shape[1]),dtype=img.dtype)
# bb = np.zeros((img.shape[0],img.shape[1]),dtype=img.dtype)
# rr[:,:] = img[:,:,0]
# gg[:,:] = img[:,:,1]
# bb[:,:] = img[:,:,2]
# cv2.imshow("Blue2", bb)
# cv2.imshow("Red2", gg)
# cv2.imshow("Green2", rr)
#
# print "通道组合"
# new = cv2.merge([rr,gg,bb])
# cv2.imshow("new",new)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


print "计算并显示直方图"

image = cv2.imread("./c.jpg")
hist = cv2.calcHist([image],
    [0], #使用的通道
    None, #没有使用mask
    [256], #HistSize
    [0.0,255.0]) #直方图柱的范围
cv2.imshow("AA", hist)
cv2.waitKey(0)