import torch
import io
from typing import Annotated
from fastapi import FastAPI, File

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
from transformers import CLIPProcessor, CLIPModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# load model
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

@app.post("/image-to-text")
async def find_similarity(file: Annotated[bytes, File()], text: str):
    img = Image.open(io.BytesIO(file))
    img = img.convert("RGB")
    txt_list = text.split(",")
    if len(txt_list) == 1:
        return {"message": "please provide more than 1 text"}
    else:
        inputs = processor(text=txt_list, images=img, return_tensors="pt", padding=True)

        with torch.no_grad():
            outputs = model(**inputs)
        logits_per_image = outputs.logits_per_image # this is the image-text similarity score
        probs = logits_per_image.softmax(dim=1) # we can take the softmax to get the label probabilities

        text_dixt = { txt_list[i].strip(): probs[0][i].item() for i in range(len(txt_list)) }
        return text_dixt

@app.get("/health")
async def health():
    return {"message": "ok"}