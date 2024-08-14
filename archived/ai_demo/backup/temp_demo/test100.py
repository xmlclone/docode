import torch
import torch.nn as nn
import torch.optim as optim
from torchtext.transforms import ToTensor
from torch.utils.data import Dataset, DataLoader
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")

class TextClassifier(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, num_classes):
        super(TextClassifier, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.rnn = nn.LSTM(embedding_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, num_classes)

    def forward(self, x):
        embedded = self.embedding(x)
        output, _ = self.rnn(embedded)
        last_hidden_state = output[:, -1, :]
        logits = self.fc(last_hidden_state)
        return logits

# 定义自定义数据集
class TextClassificationDataset(Dataset):
    def __init__(self, texts, labels):
        self.texts = texts
        self.labels = labels

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        text = self.texts["input_ids"][idx]
        label = self.labels[idx]
        return text, label

# 定义训练函数
def train(model, dataloader, criterion, optimizer, device):
    model.train()
    running_loss = 0.0
    for texts, labels in dataloader:
        texts = texts.to(device)
        labels = labels.to(device)
        
        optimizer.zero_grad()
        logits = model(texts)
        loss = criterion(logits, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item() * texts.size(0)
    
    epoch_loss = running_loss / len(dataloader.dataset)
    return epoch_loss

# 设置超参数
vocab_size = 10000
embedding_dim = 100
hidden_dim = 128
num_classes = 5
batch_size = 64
num_epochs = 10
learning_rate = 0.001

# 创建模型实例
model = TextClassifier(vocab_size, embedding_dim, hidden_dim, num_classes)

# 创建数据集
texts = ["I love this movie", "This book is boring", "Great experience", "Terrible service"]
labels = [1, 0, 1, 0]
encoded_input = tokenizer(texts, return_tensors="pt", padding=True)
dataset = TextClassificationDataset(encoded_input, labels)
testdataset = TextClassificationDataset(encoded_input, labels)

# 创建数据加载器
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
testdataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# 定义损失函数和优化器
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# 设置设备（GPU 或 CPU）
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 将模型移动到设备上
model.to(device)

# 开始训练循环
for epoch in range(num_epochs):
    train_loss = train(model, dataloader, criterion, optimizer, device)
    print(f"Epoch {epoch+1}/{num_epochs}, Training Loss: {train_loss:.4f}")


model.eval()
x, y = testdataset[0][0], labels[1]
with torch.no_grad():
    x = x.to(device)
    pred = model(x)
    predicted, actual = pred[0].argmax(0), y
    print(f'Predicted: "{predicted}", Actual: "{actual}"')