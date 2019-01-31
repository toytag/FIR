import numpy as np
from Check import check
from Analyse import analyse


class Chess:
    person = 1
    computer = -1
    def __init__(self):
        self.chess_board = np.zeros((15, 15), dtype=np.int8)
        self.first_player = Chess.computer
        self.round_counter = 0
        # from keras.models import load_model
        # self.model = load_model('m.model')

    def put_chess(self, identity, x, y):
        if self.chess_board[x, y] != 0:
            return False
        if identity == self.person:
            self.chess_board[x, y] = self.person
        elif identity == self.computer:
            self.chess_board[x, y] = self.computer
        self.round_counter += 1
        return True

    def analyse(self):
        return divmod(np.argmax(analyse(self.chess_board)), 15)
        # return divmod(np.argmax(self.model.predict(self.chess_board.reshape(1, 15, 15, 1))), 15)

    def check_winner(self):
        return check(self.chess_board)