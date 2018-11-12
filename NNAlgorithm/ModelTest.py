import keras
from keras.models import Model, load_model
import numpy as np
from os import path, getcwd


d=getcwd()
test_data_x=np.load(path.join(d,'test_data_x.npy'))
model = load_model("Models//test_model.h5")

predictions=model.predict(test_data_x, verbose=1)
print(predictions)