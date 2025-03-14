import numpy as np


# 从列表创建一维数组
arr1 = np.array([1, 2, 3, 4, 5])
print("一维数组:", arr1)

# 创建二维数组（矩阵）
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("二维数组:\n", arr2)

# 创建全零数组
zeros = np.zeros((3, 3))  # 3x3 零矩阵
print("全零数组:\n", zeros)

# 创建全一数组
ones = np.ones((2, 4))     # 2x4 全一矩阵
print("全一数组:\n", ones)

# 创建等差数列
lin_arr = np.linspace(0, 10, 5)  # 0到10之间等分5个数
print("等差数列:", lin_arr)

# 创建随机数组
rand_arr = np.random.rand(3, 2)  # 3x2 的 [0,1) 均匀分布随机数
print("随机数组:\n", rand_arr)

print('=' * 100)

# 数组形状
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("数组维度:", arr.ndim)     # 2
print("形状:", arr.shape)       # (2, 3)
print("元素总数:", arr.size)    # 6
print("数据类型:", arr.dtype)   # int32 或 float64 等
print('=' * 100)

# 数组切片
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("第一行:", arr[0])          # [1 2 3]
print("第二行第三列:", arr[1, 2])  # 6
print("列切片:\n", arr[:, 1])     # 所有行的第2列 [2 5 8]
print("子矩阵:\n", arr[1:, :2])   # 第2-3行，第1-2列 [[4,5], [7,8]]
print('=' * 100)

# 形状操作
arr = np.arange(12)
print("原始数组:", arr)          # [0 1 2 ... 11]
# 调整为 3x4 矩阵
reshaped = arr.reshape(3, 4)
print("调整形状后:\n", reshaped)
# 展平为一维数组
flattened = reshaped.flatten()
print("展平后:", flattened)
print('=' * 100)

# 向量计算
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("加法:", a + b)   # [5 7 9]
print("乘法:", a * 2)    # [2 4 6]
print("点积:", np.dot(a, b))  # 1*4 + 2*5 + 3*6 = 32
print("平方根:", np.sqrt(a))  # [1.  1.414 1.732]
print('=' * 100)

# 矩阵计算
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
result = np.matmul(matrix1, matrix2)  # 或使用 @ 运算符
print("矩阵乘法结果:\n", result)
print('=' * 100)

# 统计函数
data = np.random.randint(0, 100, 10)  # 生成10个0-99的随机整数
print("原始数据:", data)
print("平均值:", np.mean(data))
print("最大值:", np.max(data))
print("最小值位置:", np.argmin(data))
print("排序后:", np.sort(data))
print("标准差:", np.std(data))
print('=' * 100)

# 广播机制
a = np.array([[1, 2], [3, 4]])
b = np.array([10, 20])
# b 被广播为 [[10,20], [10,20]]
result = a + b
print("广播加法:\n", result)
print('=' * 100)