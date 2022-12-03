import numpy as np
import numpy as np
# from tensorflow.keras.models import load_model
from tensorflow import keras
from keras.models import load_model
# from tensorflow import keras

import cv2

model=load_model("model.h5")

def prepare(image):
    IMG_SIZE = 224
    new_array = cv2.resize(image, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE,IMG_SIZE,3)

img = cv2.imread("cat.jpg").astype(np.float32)
prediction = model.predict(prepare(img))
print(prediction)