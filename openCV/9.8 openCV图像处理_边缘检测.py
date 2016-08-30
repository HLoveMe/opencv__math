# -*- coding: utf-8 -*-
import numpy as np
import matplotlib as mat
import matplotlib.pyplot as plt
import cv2

"""
    Canny: 最后变为二值化图片

        1:由于边缘检测很容易受到噪声影响,所以第一步是使用 5x5 的高斯滤波器 去除噪声
        2:对平滑后的图像使用 Sobel 算子计算水平方向和竖直方向的一阶导数(图 像梯度)(Gx 和 Gy)
            根据的懂得梯度图 找到边界的梯度
        3:非极大值抑制:在获得梯度的方向和大小之后,应该对整幅图像做一个扫描,去除那些非 边界上的点。
        4:滞后阈值

                    \            /A
            maxVal --\----------/-------
                      \____C___/

                     \       /
                      \__B__/
            minVal ----------------------


         A 高于阈值 maxVal 所以是真正的边界点,
         C 虽然低于 maxVal 但高于 minVal 并且与 A 相连,所以也被认为是真正的边界点。
         而 B 就会被抛弃,因 为他不仅低于 maxVal 而且不与真正的边界点相连。


         所以选择合适的 maxVal 和 minVal 对于能否得到好的结果非常重要。
"""

im =  cv2.imread("./abc.jpg",0)
im = cv2.Canny(im,80,180)
print
cv2.imshow("A",im)
cv2.waitKey(0)