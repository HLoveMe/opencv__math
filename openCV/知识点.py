# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.colors
import matplotlib.pyplot as plt
import cv2
a=1

"""
    1:ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    2:brew tap homebrew/science
    3:brew install opencv
      安装到/  /usr/local/Cellar/opencv/2.4.10/
    4:吧opencv 安装路径下 /usr/local/Cellar/opencv/2.21.21/bin/python/site-.page 下 文件copy到  python/site-..下
"""
"""
    1:读取图片
        cv2.imread(file,[模式])
    2:创建
        emptyImage = np.zeros(img.shape, np.uint8)
        2.1
            调整:cv2.resize(img,(a,b),方式:)
                CV_INTER_NN - 最近邻插值,
                CV_INTER_LINEAR - 双线性插值 (缺省使用)
                CV_INTER_AREA - 使用象素关系重采样。当图像缩小时候，该方法可以避免波纹出现。当图像放大时，类似于 CV_INTER_NN 方法..
                CV_INTER_CUBIC - 立方插值.
    3:拷贝
        mage2 = img.copy();
    4:保存
        1:jpg  第三个参数可选 对于JPEG，其表示的是图像的质量，用0-100的整数表示，默认为95
            cv2.imwrite("D:\\cat2.jpg", img,[int(cv2.IMWRITE_JPEG_QUALITY), 95])
        2:png  从0到9,压缩级别越高，图像尺寸越小。默认级别为3
            cv2.imwrite("./cat2.png", img, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])

"""


"""
    图像通道  对于BRG图片有  RGB,R,G,B四种通道

    example:
        BRG图片 shape=(hang,column,3)
                [[[r,g,b],[r,g,b],[r,g,b],[r,g,b]...]]
        单通道:R shape(hang,column)
                [[r,r,r,r....]]

"""
"""
                算法
    1:二值算法
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







"""
                视频

   cap = cv2.VideoCapture(0)  得到设备  0 1 等代表摄像头 文件名这是视频文件
   cap.isOpen()               检查是否打开
   cap.open()                 打开设备
   cap.read()   -->bool,ndarray   表明是否读取到数据/读取到的数据
   cap.get(proid  0-18)  得到设备的某些信息
   cap.set(id,value)

cv2.cv.


0:CV_CAP_PROP_POS_MSEC 当前视频的position
1:CV_CAP_PROP_POS_FRAMES
2:CV_CAP_PROP_POS_AVI_RATIO  得到视频相对位置  0 : 相对头   1:相对结尾
3:CV_CAP_PROP_FRAME_WIDTH
4:CV_CAP_PROP_FRAME_HEIGHT
5:CV_CAP_PROP_FPS         FPS
6:CV_CAP_PROP_FRAME_COUNT   总帧数
7:CV_CAP_PROP_FORMAT   格式
8:CV_CAP_PROP_BRIGHTNESS 亮度 仅仅用于相机
.CV_CAP_PROP_CONTRAST  对比度 仅仅用于相机
.CV_CAP_PROP_SATURATION  饱和度 仅仅用于相机
.CV_CAP_PROP_HUE     色彩 仅仅用于相机
.CV_CAP_PROP_GAIN Gain of the image (only for cameras).
.CV_CAP_PROP_EXPOSURE Exposure (only for cameras).
.CV_CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB.
.CV_CAP_PROP_WHITE_BALANCE Currently unsupported
.CV_CAP_PROP_RECTIFICATION Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend cur- rently)
"""

arr = np.array([[255,255,4,5,0],[255,0,0,4,3]],dtype=np.uint8)
print arr
new = cv2.bitwise_not(arr)
print new