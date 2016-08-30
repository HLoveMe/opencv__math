# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt



x =  np.linspace(0,10,1000)
y1 = np.sin(x)
y2 = np.cos(x**2)
y3=x-x


# 创建绘图对象  内部引用 之后的绘画会使用该对象(也可以不创建 内部会自动创建)    要想绘制多个指定num
"""
def figure(num=None,  # autoincrement if None, else integer from 1-N
           figsize=None,  #指定大小(8,6)-->(8*dpi,6*dpi)
           dpi=None,  # defaults 80
           facecolor=None,  # defaults to rc figure.facecolor
           edgecolor=None,  # defaults to rc figure.edgecolor
           frameon=True,
           FigureClass=Figure,
           **kwargs
           ):

"""

plt.figure(figsize=(8,4))
"""
    连点成线
    plot(y)   -->x(0,N-1)  /   plot(x,y)
    lines = plot(x1,y1,x2,y2)
    plot.setp(lines ,属性 )
    线style:
        ``'-'``             solid line style
        ``'--'``            dashed line style
        ``'-.'``            dash-dot line style
        ``':'``             dotted line style
        ``'.'``             point marker
        ``','``             pixel marker
        ``'o'``             circle marker
        ``'v'``             triangle_down marker
        ``'^'``             triangle_up marker
        ``'<'``             triangle_left marker
        ``'>'``             triangle_right marker
        ``'1'``             tri_down marker
        ``'2'``             tri_up marker
        ``'3'``             tri_left marker
        ``'4'``             tri_right marker
        ``'s'``             square marker
        ``'p'``             pentagon marker
        ``'*'``             star marker
        ``'h'``             hexagon1 marker
        ``'H'``             hexagon2 marker
        ``'+'``             plus marker
        ``'x'``             x marker
        ``'D'``             diamond marker
        ``'d'``             thin_diamond marker
        ``'|'``             vline marker
        ``'_'``             hline marker
        ================    ===============================
    color
        character   color
        ==========  ========
        'b'         blue
        'g'         green
        'r'         red
        'c'         cyan
        'm'         magenta
        'y'         yellow
        'k'         black
        'w'         white
    'g--':颜色+style   :plt.plot(x,y1,'g--',linewidth=2,label='sin(x)')
    linewidth:线宽
    label:解释

"""
plt.plot(x,y1,color='y',linewidth=2,label='sin(x)')
plt.plot(x,y2,'g--',label='cos(x^2)')
plt.plot(x,y3)

plt.ylim((-2,2))
plt.xlabel("->X")
plt.ylabel("Y")

plt.legend()
plt.show()

