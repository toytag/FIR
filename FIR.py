import numpy as np


class Chess:
    def __init__(self):
        self.chess_board = np.zeros((15, 15), dtype=np.int8)
        self.person_chess_pieces = 1
        self.computer_chess_pieces = -1

    @property
    def first_player(self):
        return np.random.choice([self.person_chess_pieces, self.computer_chess_pieces])

    def put_chess_pieces(self, identity, coordinate_x, coordinate_y):
        if identity == self.person_chess_pieces:
            self.chess_board[coordinate_x][coordinate_y] = self.person_chess_pieces
        elif identity == self.computer_chess_pieces:
            self.chess_board[coordinate_x][coordinate_y] = self.computer_chess_pieces

    def analysis(self):
        pass

    def check_winner(self):
        pass

    def display_chess_board(self):
        pass


def main():
    chess = Chess()
    print '%s' % ('You First'
                  if chess.first_player == chess.person_chess_pieces
                  else 'Computer First')


if __name__ == '__main__':
    main()