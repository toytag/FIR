import numpy as np


class CoordinateError(Exception):
    def __init__(self, info):
        self.info = "YOU" if info == 1 else "COMPUTER"

    def __str__(self):
        return self.info


class Chess:
    def __init__(self):
        self.chess_board = np.zeros((15, 15), dtype=np.int8)
        self.person_chess_pieces = 1
        self.computer_chess_pieces = 2
        self.first_player = None
        self.winner = None

    def put_chess(self, identity, coordinate_x, coordinate_y):
        if self.chess_board[coordinate_x][coordinate_y] != 0:
            raise CoordinateError(self.chess_board[coordinate_x][coordinate_y])
        if identity == self.person_chess_pieces:
            self.chess_board[coordinate_x][coordinate_y] = self.person_chess_pieces
        elif identity == self.computer_chess_pieces:
            self.chess_board[coordinate_x][coordinate_y] = self.computer_chess_pieces

    def analysis(self):
        pass

    def check_winner(self):
        for i in range(15):
            for j in range(15):
                if self.chess_board[i][j] != 0:
                    try:
                        if (self.chess_board[i - 2][j] == self.chess_board[i][j] and
                                self.chess_board[i - 1][j] == self.chess_board[i][j] and
                                self.chess_board[i + 1][j] == self.chess_board[i][j] and
                                self.chess_board[i + 2][j] == self.chess_board[i][j]):
                            return self.chess_board[i][j]
                        elif (self.chess_board[i - 2][j - 2] == self.chess_board[i][j] and
                              self.chess_board[i - 1][j - 1] == self.chess_board[i][j] and
                              self.chess_board[i + 1][j + 1] == self.chess_board[i][j] and
                              self.chess_board[i + 2][j + 2] == self.chess_board[i][j]):
                            return self.chess_board[i][j]
                        elif (self.chess_board[i - 2][j + 2] == self.chess_board[i][j] and
                              self.chess_board[i - 1][j + 1] == self.chess_board[i][j] and
                              self.chess_board[i + 1][j - 1] == self.chess_board[i][j] and
                              self.chess_board[i + 2][j - 2] == self.chess_board[i][j]):
                            return self.chess_board[i][j]
                        elif (self.chess_board[i][j - 2] == self.chess_board[i][j] and
                              self.chess_board[i][j - 1] == self.chess_board[i][j] and
                              self.chess_board[i][j + 1] == self.chess_board[i][j] and
                              self.chess_board[i][j + 2] == self.chess_board[i][j]):
                            return self.chess_board[i][j]
                    except IndexError:
                        pass

    def display_chess_board(self):
        for i in range(15):
            for j in range(15):
                print(self.chess_board[i][j], end=' ')
            print()


def main():
    chess = Chess()
    chess.first_player = np.random.choice([chess.person_chess_pieces,
                                           chess.computer_chess_pieces])
    print('%s' % ('You First'
                  if chess.first_player == chess.person_chess_pieces
                  else 'Computer First'))
    # mainloop
    while True:
        coordinate = list(map(int,
                              filter(lambda x: x.isdigit(),
                                     input("Row and Column: (seperated by space)\n").split())))
        try:
            chess.put_chess(chess.person_chess_pieces, coordinate[0], coordinate[1])
        except IndexError:
            print("Invalid input, please try again")
            continue
        except CoordinateError as err:
            print(f"This coordinate has been taken by {err}, please try again")
            continue
        chess.display_chess_board()
        chess.winner = chess.check_winner()
        if chess.winner:
            print("Winner is", "YOU" if chess.winner == 1 else "COMPUTER")
            break


if __name__ == '__main__':
    main()
