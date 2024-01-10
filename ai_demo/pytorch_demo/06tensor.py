import torch
from torch import nn


X = torch.ones(5)
print(X)

X = torch.zeros(3)
print(X)

X = torch.randn(2, 3)
print(X)


# 可以理解为1维数组，里面有10个元素
X = torch.rand(10)
print(X)


# 可以理解为2维数组，最内层数据个数为3，外层数据个数为2，类似下面
[
    [1, 2, 3],
    [4, 5, 6]
]
X = torch.rand(2, 3)
print(X)


# 可以理解为3维数组，
# 即几位数组是根据传递了几个整数，而不是整数的数字，整数的数字表示每个维度元素的数量
# 可以从右往左表示低维度到高维度数据的数量
[
    [
        [1, 2, 3, 4],
        [11, 22, 33, 44],
        [111, 222, 333, 444]
    ], #2个
    [
        [1, 2, 3, 4], #3个 最里面是4个
        [11, 22, 33, 44],
        [111, 222, 333, 444]
    ]
]
X = torch.rand(2, 3, 4)
print(X)


# 生成一个2维数组，每个维度有3个元素，元素的内容都是4
X = torch.full((3, 3), 4)
print(X)


# 生成一个自定义的张量
X = torch.tensor([
    [
        [[1, 2], [2, 3], [3, 4], [4, 5]],
        [[11, 22], [22, 33], [33, 44], [44, 55]],
        [[111, 123], [222, 223], [333, 334], [444, 445]]
    ],
    [
        [[1, 2], [2, 3], [3, 4], [4, 5]],
        [[11, 22], [22, 33], [33, 44], [44, 55]],
        [[111, 123], [222, 223], [333, 334], [444, 445]]
    ],
    [
        [[1, 2], [2, 3], [3, 4], [4, 5]],
        [[11, 22], [22, 33], [33, 44], [44, 55]],
        [[111, 123], [222, 223], [333, 334], [444, 445]]
    ]
])
# X.ndim=4, X.size()=torch.Size([3, 3, 4, 2])
print(f"{X}\n{X.ndim=}, {X.size()=}")

flatten = nn.Flatten()(X)
# Flatten 会把原始张量展平为一个2维数组，数组里面有原始张量的第一个大小个数据3，每个数据是原始张量后续数据的乘积3*4*2
# flatten.ndim=2, flatten.size()=torch.Size([3, 24]), flatten.dtype=torch.int64
print(f"{flatten}\n{flatten.ndim=}, {flatten.size()=}, {flatten.dtype=}")

relu = nn.ReLU()(flatten)
print(f"{relu}\n{relu.ndim=}, {relu.size()=}, {relu.dtype=}")

# 必须是一个ndim为2的张量，即一般是通过Flatten后的数据，记住上面经过Flatten后的Size(3, 24)
# in_features  表示输入数据的Size(3, 24)里面的24，一般用原始张量的size除第一个的乘积，比如上面的3*4*2
# out_features 表示输出的Size(x, y)里面的y，其中x和输入的数据保持一致，即3，比如下面把y设置为了4，则输出的size为Size(3, 4)
linear = nn.Linear(3*4*2, 4)(flatten.float())
# linear.ndim=2, linear.size()=torch.Size([3, 4]), linear.dtype=torch.float32
print(f"{linear}\n{linear.ndim=}, {linear.size()=}, {linear.dtype=}")

# linear的权重参数默认类型是float32的，如果上面不经过float的转换，是无法直接进行linear操作的，故上面使用了flatten.float()
# linear = nn.Linear(24, 4)
# linear.weight = nn.Parameter(linear.weight.to(torch.int64))
# linear = linear(flatten)
# print(f"{linear}\n{linear.ndim=}, {linear.size()=}")

# ReLU会把小于0的置为0，否则保持不变
relu = nn.ReLU()(linear)
print(f"{relu}\n{relu.ndim=}, {relu.size()=}, {relu.dtype=}")

# Softmax表示对数据进行归一化，已2*2的数据为例，dim=0时表示对列的数据进行归一化，即列的数据之和为1，每列都会处理而不是只处理一列
# 如果dim=1表示行的数据之和为1，每行都会处理而不是只处理一行
X = torch.tensor([[1, 2], [3, 4]])
softmax = nn.Softmax(dim=0)(X.float())
print(f"{softmax}\n{softmax.ndim=}, {softmax.size()=}, {softmax.dtype=}")


# TODO:
print(f"{X}\n{nn.Flatten()(X)}\n{X.argmax()=}, {X.argmax(1)=}")


x = torch.tensor([1, 2, 3, 4])
y = torch.tensor([2, 3, 4, 5])
z = torch.matmul(x, y)
print(f"{z=}")