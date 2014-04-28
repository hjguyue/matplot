# coding:utf8

import numpy as np
# import random
# from matplotlib import pylab as pl
from matplotlib import pyplot as plt
# from xkcd import XKCDify

#画一条曲线图
plt.figure(figsize=(8,6))   #设置图形的尺寸，单位为英尺
x = np.random.randn(10)*10
y = np.pi*np.sin(x) + 8
x1 = np.arange(0,10,1)

#lines = plt.plot(x,y)
plt.plot(x,y, label = 'first line',color='red',linewidth = 2, marker = '*')
# plt.scatter(x,y, label = 'first line',color='red',linewidth = 2, marker = '*')
# plt.plot(x,y,'bo')
plt.title('Y=a*sin(x)+b')
plt.ylabel('Function-Y')
plt.xlabel('Var-X')
plt.legend()   #图形的右上角显示图形的标签，和上面的plt.plo(x,y,label='')有关
#plt.setp(lines,color = 'r',linewidth = 2.5)

plt.show()