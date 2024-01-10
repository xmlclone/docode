import os
import pandas as pd
from torchvision.io import read_image, write_png, ImageReadMode
from torch.utils.data import Dataset
from torchvision.transforms import ToTensor
import torch
from torch import nn
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
from PIL import Image


device ='cpu'

class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10)
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits
    

class CustomImageDataset(Dataset):
    def __init__(self, annotations_file, img_dir, transform=None, target_transform=None):
        self.img_labels = pd.read_csv(annotations_file)
        self.img_dir = img_dir
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        return len(self.img_labels)

    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.img_labels.iloc[idx, 0])
        image = Image.open(img_path)
        label = self.img_labels.iloc[idx, 1]
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_transform(label)
        return image, label
    
    
model = NeuralNetwork().to(device)
model.load_state_dict(torch.load("model2.pth"))

classes = [
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle boot",
]

test_data = CustomImageDataset(
    annotations_file="test_data.csv",
    img_dir=os.path.join(os.path.dirname(__file__), 'data', 'src_img', 'test_img'),
    transform=ToTensor(),
)

model.eval()

error = 0
for idx, (x, y) in enumerate(test_data):
# x, y = test_data[0][0], test_data[0][1]
    with torch.no_grad():
        x = x.to(device)
        pred = model(x)
        predicted, actual = classes[pred[0].argmax(0)], classes[y]
        # print(f'Predicted: "{predicted}", Actual: "{actual}"')
        if predicted != actual:
            error += 1
print(error)