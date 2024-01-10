import torch
from torch import nn


device = 'cpu'


class NeuralNetwork(nn.Module):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(4, 4),
            nn.ReLU(),
            nn.Linear(4, 6),
            nn.ReLU(),
            nn.Linear(6, 8)
        )

    def forward(self, x):
        print(f"org {x=}")
        x = self.flatten(x)
        print(f"flattend {x=}\n {x.ndim=} {x.size()=}")
        logits = self.linear_relu_stack(x)
        print(f"linear: {logits=}\n {logits.ndim=} {logits.size()=}")
        return logits
    

model = NeuralNetwork()
print(model)

X = torch.full((2, 2, 2), 3, dtype=torch.float32)
print(f"org {X=} {X.ndim=} {X.size()=}")
logits = model(X)
pred_probab = nn.Softmax(dim=1)(logits)
y_pred = pred_probab.argmax(1)
print(f"Predicted class: {y_pred}")