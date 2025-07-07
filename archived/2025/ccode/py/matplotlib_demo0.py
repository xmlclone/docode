import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体（根据系统安装的字体调整）
plt.rcParams['font.sans-serif'] = ['PingFang SC', 'STHeiti', 'Songti SC']  # 微软雅黑也可以用 'Microsoft YaHei'
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 创建示例数据
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
categories = ['苹果', '香蕉', '橙子', '葡萄', '芒果']
sales = [45, 32, 28, 15, 40]
sizes = [15, 30, 25, 10, 20]

# 创建画布和子图布局
plt.figure(figsize=(12, 8))

# ---------------------------
# 1. 折线图（商品销量趋势）
# ---------------------------
plt.subplot(2, 2, 1)  # 2行2列第1个位置
plt.plot(x, y1, label='正弦曲线', color='royalblue', linestyle='--', linewidth=2)
plt.plot(x, y2, label='余弦曲线', color='coral', linestyle='-')
plt.title('三角函数曲线对比')
plt.xlabel('X轴')
plt.ylabel('Y轴')
plt.grid(True, linestyle=':')
plt.legend()

# ---------------------------
# 2. 散点图（商品价格分布）
# ---------------------------
plt.subplot(2, 2, 2)
np.random.seed(42)
prices = np.random.randn(50) * 5 + 20
sizes = np.random.randint(50, 200, 50)
colors = np.random.rand(50)
plt.scatter(x=np.arange(50), y=prices, s=sizes, c=colors, 
           cmap='viridis', alpha=0.7, edgecolor='black')
plt.colorbar(label='颜色值')
plt.title('随机商品价格分布')
plt.xlabel('商品编号')
plt.ylabel('价格（元）')

# ---------------------------
# 3. 柱状图（水果销量对比）
# ---------------------------
plt.subplot(2, 2, 3)
bars = plt.bar(categories, sales, color=['#2ca02c', '#ff7f0e', '#d62728', '#9467bd', '#8c564b'])
plt.title('水果季度销量对比')
plt.ylabel('销量（吨）')

# 添加数据标签
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height}',
             ha='center', va='bottom')

# ---------------------------
# 4. 饼图（市场份额分布）
# ---------------------------
# plt.subplot(2, 2, 4)
# explode = (0.1, 0, 0, 0, 0)  # 突出显示第一项
# plt.pie(sizes, labels=categories, autopct='%1.1f%%', 
#         startangle=90, explode=explode, 
#         shadow=True, colors=plt.cm.Pastel1.colors)
# plt.title('水果市场份额分布')

# 调整布局并显示
plt.tight_layout()
# plt.savefig('matplotlib_demo.png', dpi=150)  # 保存图片
plt.show()