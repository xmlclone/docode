import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from torchtext.data.utils import get_tokenizer

# 自定义数据集类
class MyDataset(Dataset):
    def __init__(self, csv_file, tokenizer):
        # 读取csv文件，加载数据
        # 这里假设csv文件的第一列是文本数据，第二列是标签数据
        self.data = []
        self.tokenizer = tokenizer
        with open(csv_file, 'r') as f:
            for line in f:
                text, label, classify, _from = line.strip().split(',')
                try:
                    int(label)
                except:
                    continue
                self.data.append((text, label))
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        text, label = self.data[idx]
        print(self.tokenizer(text), int(label))
        # input()
        return self.tokenizer(text), int(label)
        

# 自定义模型类
class TextClassifier(nn.Module):
    def __init__(self, num_classes):
        super(TextClassifier, self).__init__()
        self.embedding = nn.Embedding(num_embeddings=vocab_size, embedding_dim=embed_dim)
        self.fc = nn.Linear(embed_dim, num_classes)
        
    def forward(self, x):
        embed = self.embedding(x)
        out = self.fc(embed)
        return out


# 设置参数
vocab_size = 10000  # 词汇表大小
embed_dim = 100  # 词嵌入维度
num_classes = 10  # 标签类别数量
batch_size = 32  # 批大小
learning_rate = 0.001  # 学习率
num_epochs = 10  # 训练轮数

# 加载数据集
tokenizer = get_tokenizer('basic_english')
dataset = MyDataset('text_training_data.csv', tokenizer)
# print(dataset)
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
# dataloader = DataLoader(dataset, batch_size=batch_size)

# 初始化模型
model = TextClassifier(num_classes)

# 定义损失函数和优化器
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# 训练模型
for epoch in range(num_epochs):
    for texts, labels in dataloader:
        # print(texts, labels)
        # 清除梯度
        optimizer.zero_grad()

        # 前向传播
        outputs = model(texts)

        # 计算损失
        loss = criterion(outputs, labels)

        # 反向传播和优化
        loss.backward()
        optimizer.step()

    print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item()}')

# 保存模型
torch.save(model.state_dict(), 'model.pth')