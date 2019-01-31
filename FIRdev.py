import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Convolution2D, Flatten, Reshape, BatchNormalization
from keras.optimizers import Adam

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
            activation='relu'
        ))
        self.model.add(Flatten())
        self.model.add(BatchNormalization())
        self.model.add(Dense(512, activation='relu'))
        self.model.add(BatchNormalization())
        self.model.add(Dense(256, activation='relu'))
        self.model.add(BatchNormalization())
        self.model.add(Dense(225, activation='relu'))
        self.model.add(Reshape(target_shape=(15, 15)))
        self.model.summary()
        self.model.compile(optimizer=Adam(lr=1e-2, decay=1e-4), loss='mse', metrics=['accuracy'])

    def nn_put(self):
        value_board = self.model.predict(self.chess_board.reshape(1, 15, 15, 1))
        return divmod(np.argmax(value_board), 15)

if __name__ == "__main__":
    chess = ChessDev()
    import pickle
    from FIRgui import Data
    with open('data.pkl', 'rb') as f:
        data = pickle.load(f)
    chess.model.fit(data.x[:1000].reshape(-1, 15, 15, 1), data.y[:1000], epochs=200, batch_size=100)
    # print(data.x.shape)  
    chess.model.save('m.model')