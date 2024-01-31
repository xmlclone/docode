"""
https://zhuanlan.zhihu.com/p/650289570
https://zhuanlan.zhihu.com/p/669895626
https://pypi.org/project/matplotlib/


pip install matplotlib
"""


import matplotlib.pyplot as plt
import numpy as np


# 数据
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 创建折线图
# # 创建第一个图表
# plt.figure(1)
plt.plot(x, y, color='green', linestyle='--', marker='o', label='Label A')

# # 创建散点图
# plt.scatter(x, y)

# # 创建条形图
# plt.bar(x, y)

# # 数据
# data = [2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7, 7, 8]
# # 创建直方图
# plt.hist(data, bins=5)

# 添加标题
plt.title('My First Matplotlib Plot')

# 添加轴标签
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')

# 添加图例
plt.legend(['Legend A'])

# TODO: 设定背景颜色
plt.axes().set_facecolor('lightgray')

# 添加注释和文本
plt.annotate('Max Value', xy=(5, 10), xytext=(4.5, 8),
             arrowprops=dict(facecolor='red', shrink=0.05))
plt.text(1, 2, 'Start Point', fontsize=10, color='blue')

# # 可以一次性创建多个图表，注意上面也要使用 plt.figure(1)
# plt.figure(2)
# plt.plot(x, y, color='green', linestyle='--', marker='o', label='Label A')

# 显示图表
plt.show()