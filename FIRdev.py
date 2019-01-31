import numpy as np
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D, UpSampling2D, BatchNormalization

import FIR
class ChessDev(FIR.Chess):
    def __init__(self):
        super().__init__()
        self.model = Sequential()
        self.model.add(Convolution2D(
            input_shape=(15, 15, 1),
            filters=32,
            kernel_size=5,
            padding='same',
            activation='tanh',
        ))
        self.model.add(BatchNormalization())
        self.model.add(Convolution2D(
            filters=64,
            kernel_size=5,
            padding='same',
            activation='tanh',
        ))
        self.model.add(BatchNormalization())
        self.model.add(Convolution2D(
            filters=128,
            kernel_size=5,
            padding='same',
            activation='tanh',
        ))
        self.model.add(MaxPooling2D(
            pool_size=3,
            padding='same',
        ))
        self.model.add(BatchNormalization())
        self.model.add(Convolution2D(
            filters=64,
            kernel_size=3,
            padding='same',
            activation='relu',
        ))
        self.model.add(BatchNormalization())
        self.model.add(Convolution2D(
            filters=16,
            kernel_size=3,
            padding='same',
            activation='relu',
        ))
        self.model.add(BatchNormalization())
        self.model.add(Convolution2D(
            filters=4,
            kernel_size=3,
            padding='same',
            activation='relu',
        ))
        self.model.add(BatchNormalization())
        self.model.add(Convolution2D(
            filters=1,
            kernel_size=3,
            padding='same',
            activation='softmax',
        ))
        self.model.add(BatchNormalization())
        self.model.add(UpSampling2D(size=3))

    def learn(self, batch_chess_board, batch_target_value_board):
        self.model.train_on_batch(batch_chess_board, batch_target_value_board)

    def nn_put(self):
        value_board = self.model.predict(self.chess_board.reshape(1, 15, 15, 1)).reshape(15, 15)
        return divmod(np.argmax(value_board), 15)

if __name__ == "__main__":
    chess = ChessDev()