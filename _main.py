import numpy as np
import cv2
from fastapi import FastAPI, File, UploadFile
import numpy as np
from tensorflow.keras.models import load_model
import tensorflow as tf

model=load_model("complete_model.h5")

app = FastAPI()

def prepare(image):
    IMG_SIZE = 224
    new_array = cv2.resize(image, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE,IMG_SIZE,3)

@app.post("/")
async def root(file: UploadFile = File(...)):
    global model
    content = await file.read()
    nparr = np.fromstring(content, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR).astype(np.float32)
    prediction = model.predict(prepare(img))
    return prediction