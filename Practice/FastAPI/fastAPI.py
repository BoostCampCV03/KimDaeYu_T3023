from typing import Optional
from fastapi import FastAPI
import torch

from Models.CycleGAN import *


if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")


G_AB, G_BA = GeneratorResNet(3), GeneratorResNet(3)
G_AB, G_BA = torch.load("./Models/weights/G_AB.pt"), torch.load("./Models/weights/G_BA.pt")
D_A, D_B = None, None

Models = [D_A, D_B, G_AB, G_BA]
# Path = ["D_A.pt","D_B.pt","G_AB.pt","G_BA.pt"]
# for m, p in zip(Models,Path):
#     m = torch.load("./Models/weights/"+ p)
#     m.eval()

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}