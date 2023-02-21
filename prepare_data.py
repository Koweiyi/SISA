from torchvision.datasets import MNIST
import torchvision.transforms as transforms
from torch.utils.data import DataLoader

train_data = MNIST(
    "./data",
    download=True,
    transform=transforms.Compose([
        transforms.Resize((32, 32)),
        transforms.ToTensor
    ]))
test_data = MNIST(
    "./data",
    download=False,
    train=False,
    transform=transforms.Compose([
        transforms.Resize((32, 32)),
        transforms.ToTensor
    ]))
print(train_data.data)
