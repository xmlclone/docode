import torch
import torch.nn as nn
import torch.optim as optim

# 创建训练数据和标签
train_data = ["error1", "error2", "error3", "error4", "error5", "error6", "error7", "error8", "error9", "error0"]
train_labels = ["class1", "class2", "class1", "class2", "class34", "class56", "class78", "class9", "class0", "class1"]

# 创建一个简单的词袋模型
vocabulary = []
for data_point in train_data:
  vocabulary.extend(data_point.split())

vocabulary = list(set(vocabulary))
print(f"{vocabulary=}")

# 构建词汇表和标签的字典
word_to_idx = {word: idx for idx, word in enumerate(vocabulary)}
label_to_idx = {label: idx for idx, label in enumerate(set(train_labels))}

# 将数据转换为张量
train_data_indices = torch.tensor([[
    word_to_idx[word]
    for word in data_point.split()
  ] for data_point in train_data])

train_label_indices = torch.tensor(
  [label_to_idx[label] for label in train_labels]
)

# 定义神经网络
class Classifier(nn.Module):
  def __init__(self, vocab_size, embedding_dim, hidden_dim, output_dim):
    super(Classifier, self).__init__()
    self.embedding = nn.Embedding(vocab_size, embedding_dim)
    self.fc = nn.Linear(embedding_dim, hidden_dim)
    self.relu = nn.ReLU()
    self.output_layer = nn.Linear(hidden_dim, output_dim)
    
  def forward(self, x):
    embedded = self.embedding(x)
    hidden = self.fc(embedded.sum(dim=1))
    activated = self.relu(hidden)
    output = self.output_layer(activated)
    return output

# 设置模型参数
vocab_size = len(vocabulary)
embedding_dim = 10
hidden_dim = 5
output_dim = len(set(train_labels))

# 实例化模型、损失函数和优化器
model = Classifier(vocab_size, embedding_dim, hidden_dim, output_dim)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# 训练模型
num_epochs = 100
for epoch in range(num_epochs):
  optimizer.zero_grad()
  outputs = model(train_data_indices)
  loss = criterion(outputs, train_label_indices)
  loss.backward()
  optimizer.step()
  
  if (epoch + 1) % 100 == 0:
    print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch+1, num_epochs, loss.item()))

# 使用模型进行推断
def predict_error_class(error):
  input_indices = torch.tensor([[word_to_idx[word] for word in error.split()]])
  output = model(input_indices)
  predicted_class_idx = torch.argmax(output).item()
  predicted_class = list(label_to_idx.keys())[predicted_class_idx]
  return predicted_class

error = "error1"
predicted_class = predict_error_class(error)
print("Predicted class for error '{}': {}".format(error, predicted_class))

error = "error8"
predicted_class = predict_error_class(error)
print("Predicted class for error '{}': {}".format(error, predicted_class))