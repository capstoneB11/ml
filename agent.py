import torch

from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

import base64

async def get_img():
    # model = torch.load('model/last.pt')
    # results =  model("test/img.jpeg")

    # img = Image.fromarray(results.render(labels=False)[0], 'RGB')
    image = Image.open('test/img.jpeg')
    img_str = base64.b64encode(bytes(image.tobytes()))
    return img_str


# Inference 


