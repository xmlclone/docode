import torch


# tensor 张量


# .ndim 一般可以数左边或右边有几个[或]符号


scalar = torch.tensor(7)
print(f"{scalar.ndim=}, {scalar.shape=}, {scalar.size()=}, {scalar.item()=}")

vector = torch.tensor([7, 7])
print(f"{vector.ndim=}, {vector.shape=}, {vector.size()=}") # {vector.item()=}

matrix = torch.tensor([
    [1, 2],
    [11, 22]
])
print(f"{matrix.ndim=}, {matrix.shape=}, {matrix.size()=}")

tensor = torch.tensor([[
    [1, 2, 3],
    [11, 22, 33],
    [111, 222, 333]
]])
print(f"{tensor.ndim=}, {tensor.shape=}, {tensor.size()=}")

"""
# 可以看见shape和size()表示相同内容
scalar.ndim=0, scalar.shape=torch.Size([]), scalar.size()=torch.Size([]), scalar.item()=7
vector.ndim=1, vector.shape=torch.Size([2]), vector.size()=torch.Size([2])
matrix.ndim=2, matrix.shape=torch.Size([2, 2]), matrix.size()=torch.Size([2, 2])
tensor.ndim=3, tensor.shape=torch.Size([1, 3, 3]), tensor.size()=torch.Size([1, 3, 3])
"""

R = torch.rand(size=(1, 2, 3, 4))
print(R)
print(f"{R.device=}")


# 验证torch是否可以访问gpu
print(torch.cuda.is_available())