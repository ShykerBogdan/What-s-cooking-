import keras
from keras.layers import Input, Dense, Activation, Dropout
from keras.models import Model
import numpy as np
from os import path, getcwd

def get_model():
    inp = Input((6714,))
    x = Dense(1024, activation='relu')(inp)
    x= Dropout(0.2)(x)
    x = Dense(512, activation='relu')(x)
    x= Dropout(0.2)(x)
    out = Dense(20, activation='softmax')(x)
    model = Model(inp, out)
    model.compile('adam', loss='mse', metrics=['acc'])
    return model


if __name__ == '__main__':
    print('loading...')
    d=getcwd()
    data_x=np.load(path.join(d,'data_x.npy'))
    data_y=np.load(path.join(d,'data_y.npy'))
    print('loading done.')
    model = get_model()
    model.fit(data_x, data_y,batch_size=8, epochs=10, initial_epoch=0, verbose=1)
    model.save("Models//test_model.h5")

