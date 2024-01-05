import torch
import torch.nn as nn
import torch.optim as optim


# 数据准备
x_train = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
# 数据基本是上面x的2倍，下面训练的次数越多越符合这里的规律
y_train = torch.tensor([[2.0], [4.0], [6.0], [8.0]])


# 定义模型
class LinearRegression(nn.Module):
    def __init__(self):
        super(LinearRegression, self).__init__()
        self.linear = nn.Linear(1, 1)  # 输入维度为1，输出维度为1

    def forward(self, x):
        return self.linear(x)


def train(model: LinearRegression, filename, times=10):
    # 训练并保存模型
    # 定义损失函数和优化器
    criterion = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01)

    # 训练模型
    # num_epochs = 10
    for epoch in range(times):
        # 前向传播
        outputs = model(x_train)
        loss = criterion(outputs, y_train)

        # 反向传播和优化
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if (epoch + 1) % 100 == 0:
            print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch+1, times, loss.item()))

    torch.save(model.state_dict(), filename)


def re_train(model: LinearRegression, times):
    # 加载保存的模型，在没有进行新的训练情况下，得到的结果和上面保存模型得到的结果是一致的
    model.load_state_dict(torch.load('test1.pth'))
    model.train()
    train(model, 'test2.pth', times)


model = LinearRegression()
train(model, 'test1.pth', 3000)
# 测试模型
x_test = torch.tensor([[5.0], [6.0], [7.0]])
y_test = model(x_test)
print('Predictions:', y_test.data)


model = LinearRegression()
# 加载第一次训练的结果再次测试模型(和上面结果一致)
model.load_state_dict(torch.load('test1.pth'))
y_test = model(x_test)
print('Predictions:', y_test.data)


# 重新加载后在进行训练
model = LinearRegression()
re_train(model, 800)
model.load_state_dict(torch.load('test2.pth'))
y_test = model(x_test)
print('Predictions:', y_test.data)