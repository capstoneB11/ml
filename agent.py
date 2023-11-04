import torch

from PIL import Image
import io

import base64

from firestore import GetImageFromFirestore

async def detect(idRef = None):
    # Load model
    model = torch.hub.load("", 'custom', path="./runs/train/exp5/weights/last.pt", source="local")
    
    # Load image
    img_enc = GetImageFromFirestore(idRef=idRef)
    img_decoded = Image.open(io.BytesIO(base64.b64decode(img_enc)))

    # with open('./test/img.jpeg', "rb") as binary_file:
    #     binary_data = binary_file.read()
    #     encoded_data = base64.b64encode(binary_data).decode()

    # Run model
    results =  model(img_decoded)
    num_boxes = len(results.xyxy[0])

    # Render Image
    img = Image.fromarray(results.render(labels=False)[0], 'RGB')
    img_io = io.BytesIO()
    img.save(img_io, format='PNG')

    # Encode Image
    base64_image = base64.b64encode(img_io.getvalue()).decode()
    base64_image = "data:image/png;base64," + base64_image

    data = { 'image' : base64_image, 'count' : num_boxes}

    return data
# Inference 


