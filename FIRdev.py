import numpy as np
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D, UpSampling2D, BatchNormalization

import FIR
class ChessDev(FIR.Chess):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    chess = ChessDev()

    model = Sequential()
    model.add(Convolution2D(
        input_shape=(15, 15, 1),
        filters=32,
        kernel_size=5,
        padding='same',
        activation='tanh',
    ))
    model.add(BatchNormalization())
    model.add(Convolution2D(
        filters=64,
        kernel_size=5,
        padding='same',
        activation='tanh',
    ))
    model.add(BatchNormalization())
    model.add(Convolution2D(
        filters=128,
        kernel_size=5,
        padding='same',
        activation='tanh',
    ))
    model.add(MaxPooling2D(
        pool_size=3,
        padding='same',
    ))
    model.add(BatchNormalization())
    model.add(Convolution2D(
        filters=64,
        kernel_size=3,
        padding='same',
        activation='relu',
    ))
    model.add(BatchNormalization())
    model.add(Convolution2D(
        filters=16,
        kernel_size=3,
        padding='same',
        activation='relu',
    ))
    model.add(BatchNormalization())
    model.add(Convolution2D(
        filters=4,
        kernel_size=3,
        padding='same',
        activation='relu',
    ))
    model.add(BatchNormalization())
    model.add(Convolution2D(
        filters=1,
        kernel_size=3,
        padding='same',
        activation='softmax',
    ))
    model.add(BatchNormalization())
    model.add(UpSampling2D(size=(3, 3)))
    model.summary()

    print(model.predict(chess.chess_board.reshape(1, 15, 15, 1)).reshape(15, 15))