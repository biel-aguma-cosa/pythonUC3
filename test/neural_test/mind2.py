import torch, torch.nn as nn


class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.fc1 = nn.Linear(15,64)
        self.fc2 = nn.Linear(64,64)
        self.fc3 = nn.Linear(64, 6)
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = torch.sigmoid(self.fc3(x))
        return x

# nn.HuberLoss()
# torch.optim.Adagrad()

model = NeuralNetwork()
criterion = nn.HuberLoss()
optimizer = torch.optim.Adagrad(model.parameters(), lr=0.01)

inputs = torch.randn((100, 15))
targets = torch.randint(0, 2, (100, 1)).float()
epochs = 20

for epoch in range(epochs):
    optimizer.zero_grad()
    outputs = model(inputs)
    loss = criterion(outputs, targets)
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 5 == 0:
        print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}")