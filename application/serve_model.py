from io import BytesIO

import numpy as np
import tensorflow as tf
from PIL import Image
from keras.models import load_model

model = None


def load():
    model = load_model("cnn_50epochs_imgsize128.h5")
    print("Model loaded")
    return model


def predict(image: Image.Image):
    global model
    if model is None:
        model = load()
        
    image = np.asarray(image.resize((128, 128)))[..., :3]
    image = np.expand_dims(image, 0)
    image = image / 127.5 - 1.0
    
    prediction = model.predict(image)
    
    response = []
    for i, res in enumerate(prediction):
        resp = {}
        resp["class"] = res[1]
        resp["confidence"] = f"{res[2]*100:0.2f} %"
        
        response.append(resp)
    
    return response


def read_imagefile(file) -> Image.Image:
    image = Image.open(BytesIO(file))
    return image
        