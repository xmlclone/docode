import torch
from transformers import BertTokenizer, BertForSequenceClassification
from torch.utils.data import DataLoader, RandomSampler
from transformers import AdamW
import pandas as pd


df = pd.read_csv('text_training_data.csv')

# 加载BERT tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# 加载预训练的BERT模型
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)

# 定义训练数据集
train_texts = df.text.tolist()
train_labels = df.label.tolist()

# 对训练数据进行编码和标记化处理
train_encodings = tokenizer(train_texts, truncation=True, padding=True)

class Dataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, index):
        item = {key: torch.tensor(val[index]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[index])
        return item

    def __len__(self):
        return len(self.labels)

# 创建数据加载器
train_dataset = Dataset(train_encodings, train_labels)
train_sampler = RandomSampler(train_dataset)
train_dataloader = DataLoader(train_dataset, sampler=train_sampler, batch_size=16)

# 设置训练参数
num_epochs = 10
optimizer = AdamW(model.parameters(), lr=1e-5)

# 开始训练
model.train()
for epoch in range(num_epochs):
    for batch in train_dataloader:
        optimizer.zero_grad()
        outputs = model(**batch)
        loss = outputs.loss
        loss.backward()
        optimizer.step()


# 对用户输入进行编码和标记化处理
input_encoding = tokenizer.encode_plus(
    "This movie is boring",
    add_special_tokens=True,
    max_length=128,
    padding='max_length',
    truncation=True,
    return_tensors='pt'
)

# 预测输出
model.eval()
with torch.no_grad():
    input_encoding = {key: val.to(model.device) for key, val in input_encoding.items()}
    outputs = model(**input_encoding)
    logits = outputs.logits
    predicted_label = torch.argmax(logits, dim=1)

print(predicted_label)



# 对用户输入进行编码和标记化处理
input_encoding = tokenizer.encode_plus(
    "Bad experience",
    add_special_tokens=True,
    max_length=128,
    padding='max_length',
    truncation=True,
    return_tensors='pt'
)

# 预测输出
model.eval()
with torch.no_grad():
    input_encoding = {key: val.to(model.device) for key, val in input_encoding.items()}
    outputs = model(**input_encoding)
    logits = outputs.logits
    predicted_label = torch.argmax(logits, dim=1)

print(predicted_label)