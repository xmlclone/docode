import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from transformers import AutoModelForSequenceClassification

# 定义模型
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.dropout = nn.Dropout2d()
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = nn.functional.relu(nn.functional.max_pool2d(self.conv1(x), 2))
        x = nn.functional.relu(nn.functional.max_pool2d(self.dropout(self.conv2(x)), 2))
        x = x.view(-1, 320)
        x = nn.functional.relu(self.fc1(x))
        x = self.fc2(x)
        return nn.functional.log_softmax(x, dim=1)

# 加载MNIST数据集
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))])
train_loader = torch.utils.data.DataLoader(datasets.MNIST('data', train=True, download=True, transform=transform),
                                           batch_size=64, shuffle=True)
test_loader = torch.utils.data.DataLoader(datasets.MNIST('data', train=False, transform=transform),
                                          batch_size=64, shuffle=True)

# # 定义优化器和损失函数
# model = Net()
# optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.5)
# criterion = nn.CrossEntropyLoss()

# # 训练模型
# for epoch in range(1, 3):
#     for batch_idx, (data, target) in enumerate(train_loader):
#         optimizer.zero_grad()
#         output = model(data)
#         loss = criterion(output, target)
#         loss.backward()
#         optimizer.step()
#     print('Epoch:', epoch, 'Loss:', loss.item())

# # 保存训练好的模型为二进制文件
# torch.save(model.state_dict(), 'mnist_model.bin')



# 加载本地模型文件
model = AutoModelForSequenceClassification.from_pretrained('mnist_model.bin')

# 在测试数据集上进行推断
model.eval()
correct = 0
total = 0

with torch.no_grad():
    for data, target in test_loader:
        output = model(data)
        _, predicted = torch.max(output.logits.data, 1)
        total += target.size(0)
        correct += (predicted == target).sum().item()

print('Accuracy on test set:', 100 * correct / total, '%')