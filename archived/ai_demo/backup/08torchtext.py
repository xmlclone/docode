import torch
import pandas as pd

from torch import (
    nn,
    Tensor
)
from torch.utils.data import (
    Dataset,
    DataLoader
)
from transformers import (
    AutoTokenizer,
    BertTokenizerFast
)


device = (
    "cuda"
    if torch.cuda.is_available()
    else "mps"
    if torch.backends.mps.is_available()
    else "cpu"
)
learn_rate = 1e-3
tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
input_tensor_features = 6


class CustomTextDataset(Dataset):
    def __init__(self, annotations_file, transform=None, target_transform=None):
        self.df = pd.read_csv(annotations_file)
        self.transform = transform
        self.target_transform = target_transform
        self.encoded_text = tokenizer(self.df.text.tolist(), return_tensors="pt", padding=True)

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        text: Tensor = self.encoded_text['input_ids'][idx].float().unsqueeze(0)
        # input(f"{text}\n{text.ndim=}, {text.size()=}, {text.dtype=}")
        label = self.df.iloc[idx, 1]
        if self.transform:
            text = self.transform(text)
        if self.target_transform:
            label = self.target_transform(label)
        return text, label
    

class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(input_tensor_features, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10)
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits


def train_task(dataloader: DataLoader, model: NeuralNetwork, loss_fn, optimizer):
    size = len(dataloader.dataset)
    model.train()
    for batch, (X, y) in enumerate(dataloader):
        X, y = X.to(device), y.to(device)

        # Compute prediction error
        pred = model(X)
        loss = loss_fn(pred, y)

        # Backpropagation
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

        if batch % 100 == 0:
            loss, current = loss.item(), (batch + 1) * len(X)
            print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")


def test_task(dataloader: DataLoader, model: NeuralNetwork, loss_fn):
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    model.eval()
    test_loss, correct = 0, 0
    with torch.no_grad():
        for X, y in dataloader:
            X, y = X.to(device), y.to(device)
            pred = model(X)
            test_loss += loss_fn(pred, y).item()
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()
    test_loss /= num_batches
    correct /= size
    print(f"Test Error: \n Accuracy: {(100*correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")


def train(epochs=10, batch_size=64, save_to_file=None, load_retrain_file=None):
    training_data = CustomTextDataset(annotations_file="text_training_data.csv")
    test_data = CustomTextDataset(annotations_file="text_test_data.csv")
    # print(f"{training_data=}")
    train_dataloader = DataLoader(training_data, batch_size=batch_size, shuffle=True)
    test_dataloader = DataLoader(test_data, batch_size=batch_size, shuffle=True)

    model = NeuralNetwork().to(device)
    if load_retrain_file:
        model.load_state_dict(torch.load(load_retrain_file))

    loss_fn = nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=learn_rate)
    for t in range(epochs):
        print(f"Epoch {t+1}\n-------------------------------")
        train_task(train_dataloader, model, loss_fn, optimizer)
        test_task(test_dataloader, model, loss_fn)
    print("Done!")

    if save_to_file:
        torch.save(model.state_dict(), save_to_file)
        print("Saved PyTorch Model State to model.pth")


train(save_to_file="text_model.pth")

