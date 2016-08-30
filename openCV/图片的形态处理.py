# -*- coding: utf-8 -*-
import numpy as np

import cv2

img = cv2.imread("./b.png")
cv2.imshow("原图",img)

#定义Opencv结构体元素
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
#腐蚀图像
eroded = cv2.erode(img,kernel)
#显示腐蚀后的图像
cv2.imshow("Eroded Image",eroded)

#膨胀图像
dilated = cv2.dilate(img,kernel)
#显示膨胀后的图像
cv2.imshow("Dilated Image",dilated)


NpKernel=np.ones((3,3))
for i in range(3):
    NpKernel[1, i] = 1
    NpKernel[i, 1] = 1
#膨胀图像
dilated2 = cv2.dilate(img,NpKernel)
#显示膨胀后的图像
cv2.imshow("Dilated Image2",dilated2)


k = cv2.waitKey(0)&0xFF

cv2.destroyAllWindows()



