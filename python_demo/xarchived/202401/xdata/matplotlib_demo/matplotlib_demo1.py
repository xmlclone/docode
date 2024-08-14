"""
创建子图
"""


import matplotlib.pyplot as plt
import numpy as np


# 数据
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 2, 1, 2, 1]

# 创建一个包含两个子图的图表
plt.figure(figsize=(10, 4))

# 子图1
plt.subplot(1, 2, 1)
plt.plot(x, y1, label='Line A')
plt.title('Subplot 1')

# 子图2
plt.subplot(1, 2, 2)
plt.plot(x, y2, label='Line B')
plt.title('Subplot 2')

# 调整子图之间的间距
plt.tight_layout()

# 显示图表
plt.show()