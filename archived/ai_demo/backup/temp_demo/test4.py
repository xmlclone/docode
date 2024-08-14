import csv
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
from torch.nn.utils.rnn import pad_sequence

class TextDataset(Dataset):
    def __init__(self, text_list, label_list, vocab):
        self.text_list = text_list
        self.label_list = label_list
        self.vocab = vocab

    def __len__(self):
        return len(self.text_list)

    def __getitem__(self, idx):
        text = self.text_list[idx]
        label = self.label_list[idx]
        return torch.LongTensor([self.vocab[token] for token in text]), label

class RNNModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, output_dim):
        super(RNNModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.rnn = nn.RNN(embedding_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_dim)

    def forward(self, text):
        embedded = self.embedding(text)
        output, hidden = self.rnn(embedded)
        return self.fc(hidden.squeeze(0))

def read_csv_file(filename):
    text_list = []
    label_list = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                int(row[1])
            except:
                continue
            text_list.append(row[0].lower().split())
            label_list.append(int(row[1]))
    return text_list, label_list

def train(model, train_loader, optimizer, criterion):
    total_loss = 0
    total_correct = 0
    for batch_idx, (text, label) in enumerate(train_loader):
        optimizer.zero_grad()
        output = model(text)
        loss = criterion(output, label)
        total_loss += loss.item()
        total_correct += (output.argmax(1) == label).sum().item()
        loss.backward()
        optimizer.step()
    return total_loss / len(train_loader), total_correct / len(train_loader.dataset)

def predict(model, text, vocab):
    model.eval()
    with torch.no_grad():
        text_tensor = torch.LongTensor([vocab[token] for token in text])
        output = model(text_tensor.unsqueeze(0))
        return output.argmax().item()

# 参数设置
csv_file = 'text_training_data.csv'
vocab_file = 'vocab.txt'
batch_size = 64
embedding_dim = 64
hidden_dim = 128
output_dim = 5
learning_rate = 0.01
num_epochs = 10

# 读入数据
text_list, label_list = read_csv_file(csv_file)

# 构建词表
vocab = {}
with open(vocab_file, 'r', encoding="utf-8") as f:
    for line in f:
        token = line.strip()
        if token not in vocab:
            vocab[token] = len(vocab)

# 构建数据集和数据加载器
dataset = TextDataset(text_list, label_list, vocab)
data_loader = DataLoader(dataset, batch_size=batch_size, shuffle=True, collate_fn=lambda x: pad_sequence([item[0] for item in x], batch_first=True))

# 定义模型、优化器、损失函数
model = RNNModel(len(vocab), embedding_dim, hidden_dim, output_dim)
optimizer = optim.Adam(model.parameters(), lr=learning_rate)
criterion = nn.CrossEntropyLoss()

# 训练模型
for epoch in range(num_epochs):
    train_loss, train_acc = train(model, data_loader, optimizer, criterion)
    print('Epoch %d, train loss: %.4f, train acc: %.4f' % (epoch+1, train_loss, train_acc))

# 使用模型进行预测
text = 'syntax error'
label = predict(model, text.split(), vocab)
print('Input text: %s, predicted label: %d' % (text, label))