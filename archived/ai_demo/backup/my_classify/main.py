import torch
import pandas as pd

from transformers import BertTokenizer, BertForSequenceClassification
from torch.utils.data import DataLoader, RandomSampler
from torch.utils.data import Dataset
# from transformers import AdamW
from torch.optim import AdamW


pt_save_directory = "./pt_save_pretrained"
num_labels = 10
max_length = 128 *4
# model_name = "bert-base-uncased"
model_name = "bert-base-multilingual-cased"


class TextDataset(Dataset):
    def __init__(self, train_csv_file):
        self.df = pd.read_csv(train_csv_file, encoding="gbk")
        self.train_texts = self.df.text.tolist()
        self.train_labels = self.df.label.tolist()
        tokenizer = BertTokenizer.from_pretrained(model_name)
        self.train_encodings = tokenizer(self.train_texts, truncation=True, padding=True)

    def __getitem__(self, index):
        item = {key: torch.tensor(val[index]) for key, val in self.train_encodings.items()}
        item['labels'] = torch.tensor(self.train_labels[index])
        return item

    def __len__(self):
        return len(self.train_labels)
    

def train_task(dataloader: DataLoader, model: BertForSequenceClassification, optimizer: AdamW):
    size = len(dataloader.dataset)
    model.train()
    for batch, data in enumerate(dataloader):
        optimizer.zero_grad()
        outputs = model(**data)
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        if batch % 2 == 0:
            loss, current = loss.item(), (batch + 1) * len(data['input_ids'])
            print(f"loss: {loss:>7f}  [{current:>3d}/{size:>3d}]")


def test_task(dataloader: DataLoader, model: BertForSequenceClassification, load_model=False):
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    model.eval()
    test_loss, correct = 0, 0
    if load_model:
        tokenizer: BertTokenizer = BertTokenizer.from_pretrained(pt_save_directory)
    else:
        tokenizer = BertTokenizer.from_pretrained(model_name)
    with torch.no_grad():
        for data in dataloader:
            for input_str, label in zip(data["input_ids"], data['labels']):
                output = tokenizer.decode(input_str)
                input_encoding = tokenizer.encode_plus(
                    output,
                    add_special_tokens=True,
                    max_length=max_length,
                    padding='max_length',
                    truncation=True,
                    return_tensors='pt'
                )
                input_encoding = {key: val for key, val in input_encoding.items()}
                outputs = model(**input_encoding)
                logits = outputs.logits
                predicted_label = torch.argmax(logits, dim=1)
                correct += (1 if predicted_label.item() == label.item() else 0)
    test_loss /= num_batches
    correct /= size
    print(f"Test Accuracy: {(100*correct):>0.1f}%\n")
    

def train(epochs=10, batch_size=2, save_model=False, load_model=False):
    if load_model:
        tokenizer: BertTokenizer = BertTokenizer.from_pretrained(pt_save_directory)
        model: BertForSequenceClassification = BertForSequenceClassification.from_pretrained(pt_save_directory, num_labels=num_labels)
    else:
        tokenizer = BertTokenizer.from_pretrained(model_name)
        model: BertForSequenceClassification = BertForSequenceClassification.from_pretrained(model_name, num_labels=num_labels)
    optimizer = AdamW(model.parameters(), lr=1e-5)

    train_dataset = TextDataset("text_training_data.csv")
    train_sampler = RandomSampler(train_dataset)
    train_dataloader = DataLoader(train_dataset, sampler=train_sampler, batch_size=batch_size)

    test_dataset = TextDataset("text_test_data.csv")
    test_sampler = RandomSampler(test_dataset)
    test_dataloader = DataLoader(train_dataset, sampler=test_sampler, batch_size=batch_size)
    
    for epoch in range(epochs):
        print(f"Epoch {epoch+1}\n-------------------------------")
        train_task(train_dataloader, model, optimizer)
        test_task(test_dataloader, model, load_model=load_model)

    if save_model:
        tokenizer.save_pretrained(pt_save_directory)
        model.save_pretrained(pt_save_directory)
        print(f"Saved Model State to {pt_save_directory}")


def pred(input_str):
    classfiy = [
        "疑似产品问题", #0
        "脚本问题", #1
        "测试框架错误", #2
        "UI元素定位异常", #3
        "未知错误"  #4
    ]
    
    tokenizer: BertTokenizer = BertTokenizer.from_pretrained(pt_save_directory)
    input_encoding = tokenizer.encode_plus(
        input_str,
        add_special_tokens=True,
        max_length=max_length,
        padding='max_length',
        truncation=True,
        return_tensors='pt'
    )
    model: BertForSequenceClassification = BertForSequenceClassification.from_pretrained(pt_save_directory, num_labels=num_labels)
    model.eval()
    with torch.no_grad():
        input_encoding = {key: val for key, val in input_encoding.items()}
        outputs = model(**input_encoding)
        logits = outputs.logits
        predicted_label = torch.argmax(logits, dim=1)
    return classfiy[int(predicted_label.item())]


# train(save_model=True)

for text in pd.read_csv("text_training_data.csv", encoding="gbk").text.tolist():
    print(pred(text))

# train(load_model=True, save_model=True)
# print(pred("Error in file '/data/teststone/TestCases/rainbowstone_video/TestCases/video_NBA/连续/球队通、联盟通-V4.54.0/安卓端三方连续联盟通.robot': Setting variable '${externalOrderId}' failed: Resolving variable '${__Random(00001,99999,)}' failed: Variable '${__Random}' not found.."))
# print(pred("Resolving variable '${xiaoming)}' failed"))
# print(pred("Bad experience"))