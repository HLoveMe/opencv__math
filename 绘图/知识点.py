# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path
source="http://matplotlib.org/gallery.html"
print "属性"
"""
        绘制出来的矩形,线段,范围(容器)都是Artist后者其子类
    ----------------------------------------------------------
    |                                                        Figure:Artist绘制对象
    |
    |
    |
    |
    |
    |
    |                                                         dpi
    |                                                        |
    |                                                        |
    |                                                        |
    |       Y---------------        ---------------          |
    |        |  Axes:Artist|      |     Axes      |          |
    |        |             |      |               |          |
    |        |   各种图形为  |      |               |          |
    |        |    Artist   |      |               |          |
    |        |             |      |               |          |
    |         --------------->  ---------------             |
    |             Axis:Artis                                 |
    ----------------------------------------------------------
"""

"""
    参数配置
    import matplotlib
    matplotlib.matplotlib_fname() //得到配置文件路径

    import matplotlib
    print matplotlib.rcParams  //得到配置
        更改只会影响当前绘制 //matplotlib.rc("lines", marker="x", linewidth=2, color="red")
    matplotlib.rcdefaults() //恢复默认配置
"""

"""


    matplotlib API包含有三层：
        backend_bases.FigureCanvas : 图表的绘制领域
        backend_bases.Renderer : 知道如何在FigureCanvas上如何绘图
        artist.Artist : 知道如何使用Renderer在FigureCanvas上绘图

    Artists  1:简单类型的Artists为标准的绘图元件，例如Line2D、 Rectangle、 Text、AxesImage 等等
             2:容器类型则可以包含许多简单类型的Artists，使它们组织成一个整体，例如Axis、 Axes、Figure等。

        直接使用Artists创建图表的标准流程如下：
            1:创建Figure绘图对象
            2:用Figure对象创建一个或者多个Axes(表示一个区域)或者Subplot对象//add_subplot(211)/fig.add_axes([0.1, 0.1, 0.7, 0.3])
            3:调用Axies等对象的方法创建各种简单类型的Artists (ax.plot([1,2,3],[1,2,1])创建线Line) 设置 xy轴说明等等属性

        Artists属性:
                alpha : 透明度，值在0到1之间，0为完全透明，1为完全不透明
                animated : 布尔值，在绘制动画效果时使用
                axes : 此Artist对象所在的Axes对象，可能为None
                clip_box : 对象的裁剪框
                clip_on : 是否裁剪
                clip_path : 裁剪的路径
                contains : 判断指定点是否在对象上的函数
                figure : 所在的Figure对象，可能为None
                label : 文本标签
                picker : 控制Artist对象选取
                transform : 控制偏移旋转
                visible : 是否可见
                zorder : 控制绘图顺序

    容器 Figure:Artist
        1:创建容器fig=plt.figure()/fig,axes=plt.subplots()
        2:增加子图AxesSubplot:Axes=fig.add_subplot(211)/Axes=fig.add_axes([0.1, 0.1, 0.7, 0.3])
        3:操作:add_subplot, add_axes, delaxes

        axes : Axes对象列表
        patch : 作为背景的Rectangle对象
        images : FigureImage对象列表，用来显示图片
        legends : Legend对象列表
        lines : Line2D对象列表
        patches : patch对象列表

        由于Figure:Artist 所以Figure也可以拥有自己的Line Rect等等   坐标[0,0,1,1]
            fig = plt.figure()
            line1 = Line2D([0,1],[0,1], transform=fig.transFigure, figure=fig, color="r")
            line2 = Line2D([0,1],[1,0], transform=fig.transFigure, figure=fig, color="g")
            fig.lines.extend([line1, line2])
            fig.show()


    容器:Axes:Artist

        1:创建
            fig = plt.figure()
            ax = fig.add_subplot(111)//fig.add_axes([0.1, 0.1, 0.7, 0.3])
        2:添加内容
            ax.plot(x,y,'g--')
            ax.add_patch()
            ax.set_title()

        属性:
             artists : Artist对象列表
             patch : 作为Axes背景的Patch对象，可以是Rectangle或者Circle
             collections : Collection对象列表
             images : AxesImage对象列表
             legends : Legend对象列表
             lines : Line2D对象列表
             patches : Patch对象列表
             texts : Text对象列表
             xaxis : XAxis对象
             yaxis : YAxis对象
        方法:

               Axes的方法	所创建的对象	     添加进的列表
               annotate	      Annotate	        texts
               bars	          Rectangle	        patches
               errorbar	    Line2D, Rectangle	lines,patches
               fill	           Polygon	          patches
               hist	           Rectangle	      patches
               imshow	       AxesImage	     images
               legend	        Legend	         legends
               plot         	Line2D          	lines
               scatter	      PolygonCollection	Collections
               text	            Text	             textsX


    容器:Axis:Artist(XAxis X轴,YAxis Y轴)
        Axis容器包括坐标轴上的刻度线、刻度文本、坐标网格以及坐标轴标题等内容


        1: axis = plt.gca().xaxis  / yaxis
        2: axis.get_ticklocs() 得到  刻度列表[0,1,2,3]
           axis.get_ticklabels() 得到标签列表 ['0','1','2','3']
           axis.get_ticklines(minor=True/False)   得到主/副刻度线 Line2D
         设置轴文字:
            plt.xlabel("->X")
            axis.set_xlabel("->XX")
            axis.xaxis.set_label_text("->X_X")
         设置刻度
            主刻度:
                axis.xaxis.set_major_locator(MultipleLocator(np.pi/4))    #刻度为pi/4
                axis.xaxis.set_major_formatter( FuncFormatter( pi_formatter) )    #刻度专为你自定义的内容  def pi_formatter(刻度,第个数)
            副刻度:
                axis.xaxis.set_minor_locator(MultipleLocator(np.pi/20))

            设置标度 | 属性
                for line in axis.get_ticklines():
                    line.set_color("g")
                    line.set_markersize(25)
                    line.set_markeredgewidth(3)

        3:plt.xticks([]), plt.yticks([])/plt.axis('off')   去掉x/y 轴 所有标度/文字


"""


""""
    1:图形绘画对象为 Figure
        在 plt.figure()/plt.gcf()返回

    2:Figure 对象有个axes属性 表示 图表子图集合
        plt.gca() 当前子图(每个子图 又有属于自己的属性)

    3:在绘制线段 图形时 得到Line2D对象
        lines = plt.plot(x,y2,'g--',label='cos(x^2)')

    4:属性操作
       plt.getp(obj,[color....]) 得到对象的属性  / 无属性名参数 表示 得到所有属性
       plt.setp(obj,color='r',....)

       plt.getp(plt.gca())   //得到当前子图的所有属性

"""

"""
    路径: Path:Artist
    图形:使用路径初始化
        1:Shadow 阴影
        2:Rectangle 矩形   Polygon 多边形
        3:RegularPolygon 正多边形
        4:PathPatch  聚合路径图形(多个图形组合)
        5:Wedge
        6:Arrow   YAArrow
        7:FancyArrow(Polygon)
        8:Ellipse 椭圆  A scale-free ellipse.
        9:FancyBboxPatch
        10:FancyArrowPatch

使用路径(点) 来绘制
XY = np.array([[[1,2],[2,3],[3,3],[4,2],[3,1],[2,1]]]) //六边形
barpath = path.Path.make_compound_path_from_polys(XY)
patch = patches.PathPatch(
    barpath, facecolor='blue', edgecolor='gray', alpha=0.8)
print patch
ax.add_patch(patch)

矩形
patch = patches.Rectangle([1,1],width=3,height=1,facecolor='r')
ax.add_patch(patch)

"""
