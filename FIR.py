import numpy as np
from Check import check
from Analyse import depth_analyse


class Chess:
    person_chess_pieces = 1
    computer_chess_pieces = -1
    
    def __init__(self):
        self.chess_board = np.zeros((15, 15), dtype=np.int8)
        self.score_board = np.zeros((15, 15), dtype=np.int32)
        self.first_player = np.random.choice([Chess.person_chess_pieces,
                                              Chess.computer_chess_pieces])
        self.winner = None

    def put_chess(self, identity, coordinate_x, coordinate_y):
        # raise an error if user's input coordinate has already been taken
        if self.chess_board[coordinate_x][coordinate_y] != 0:
            return True
        # otherwise put the chess
        if identity == self.person_chess_pieces:
            self.chess_board[coordinate_x][coordinate_y] = self.person_chess_pieces
        elif identity == self.computer_chess_pieces:
            self.chess_board[coordinate_x][coordinate_y] = self.computer_chess_pieces
        return False

    def analyse_put(self):
        # initialize score board
        self.score_board = np.zeros((15, 15), dtype=np.int32)
        # analyse the chess board and get the location
        coordinate = depth_analyse(self.chess_board, self.score_board, 
                                   np.random.choice([3, 5]))
        return coordinate[1], coordinate[2]

    def check_winner(self):
        return check(self.chess_board)


