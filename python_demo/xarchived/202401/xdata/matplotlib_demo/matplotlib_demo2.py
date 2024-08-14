import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Subplot

# 模拟真实数据集
cities = ['City A', 'City B', 'City C']
temperature = [28, 32, 25]
humidity = [60, 45, 75]

# 创建多图表
ax1: Subplot
ax2: Subplot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# 子图1：气温条形图
ax1.bar(cities, temperature, color=['red', 'blue', 'green'])
ax1.set_title('Temperature in Cities')
ax1.set_ylabel('Temperature (°C)')

# 子图2：湿度饼图
ax2.pie(humidity, labels=cities, autopct='%1.1f%%', colors=['gold', 'lightcoral', 'lightskyblue'])
ax2.set_title('Humidity in Cities')

# 调整布局
plt.tight_layout()

# 显示图表
plt.show()