import torch
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt
import pandas as pd
import os
from PIL import Image


training_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    # transform=ToTensor()
)

test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    # transform=ToTensor()
)


img_data = []
label_data = []
for idx, (image, label) in enumerate(training_data, 1):
    filename = f"{idx}.png"
    filepath = os.path.join(os.path.dirname(__file__), 'data', 'src_img', 'training_img', filename)
    image.save(filepath)
    # Image.fromarray(image).save(filepath)
    img_data.append(filename)
    label_data.append(label)
    idx += 1
    # break
df = pd.DataFrame({"img": img_data, "label": label_data})
df.to_csv('training_data.csv', index=False)


img_data = []
label_data = []
for idx, (image, label) in enumerate(test_data, 1):
    filename = f"{idx}.png"
    filepath = os.path.join(os.path.dirname(__file__), 'data', 'src_img', 'test_img', filename)
    image.save(filepath)
    # Image.fromarray(image).save(filepath)
    img_data.append(filename)
    label_data.append(label)
    idx += 1
    # break
df = pd.DataFrame({"img": img_data, "label": label_data})
df.to_csv('test_data.csv', index=False)


# figure = plt.figure(figsize=(8, 8))
# cols, rows = 3, 3
# for i in range(1, cols * rows + 1):
#     sample_idx = torch.randint(len(training_data), size=(1,)).item()
#     img, label = training_data[sample_idx]
    # figure.add_subplot(rows, cols, i)
    # plt.title(labels_map[label])
    # plt.axis("off")
    # plt.imshow(img.squeeze(), cmap="gray")
    # print(img.squeeze())
    # plt.imsave(f"{i}.png", img.squeeze(), cmap="gray")
# plt.show()