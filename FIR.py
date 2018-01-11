import numpy as np
from Check import check
from Analyse import analyse
from pprint import pprint


class CoordinateError(Exception):
    def __init__(self, info):
        self.info = "YOU" if info == Chess.person_chess_pieces else "COMPUTER"
    def __str__(self):
        return self.info


class Chess:
    person_chess_pieces = 2
    computer_chess_pieces = -2
    
    def __init__(self):
        self.chess_board = np.zeros((15, 15), dtype=np.int8)
        self.score_board = None
        self.first_player = None
        self.winner = None

    def put_chess(self, identity, coordinate_x, coordinate_y):
        # raise an error if user's input coordinate has already been taken
        if self.chess_board[coordinate_x][coordinate_y] != 0:
            raise CoordinateError(self.chess_board[coordinate_x][coordinate_y])
        if identity == self.person_chess_pieces:
            self.chess_board[coordinate_x][coordinate_y] = self.person_chess_pieces
        elif identity == self.computer_chess_pieces:
            self.chess_board[coordinate_x][coordinate_y] = self.computer_chess_pieces

    def analyse(self):
        # initialize score board
        self.score_board = np.zeros((15, 15))
        # analyse the chess board
        analyse(self.chess_board, self.score_board)
        score_ls = self.score_board.reshape(15 * 15).tolist()
        # find max score point
        location = score_ls.index(max(score_ls))
        # calculate its location
        coordinate_x, coordinate_y = location // 15, location % 15
        # put the chess
        self.put_chess(self.computer_chess_pieces, coordinate_x, coordinate_y)
        # show it to the user
        print("\nComputer at:", coordinate_x, coordinate_y, "\n")

    def check_winner(self):
        for i in range(15):
            for j in range(15):
                if check(self.chess_board, i, j):
                    return True

    def display_chess_board(self):
        for i in range(15):
            for j in range(15):
                print('.' if self.chess_board[i][j] == 0 
                          else self.chess_board[i][j], end='  ')
            print()
    
    def display_score_board(self):
        for i in range(15):
            for j in range(15):
                print('.' if self.score_board[i][j] == 0 
                          else self.score_board[i][j], end='\t')
            print()


def main():
    chess = Chess()
    chess.first_player = np.random.choice([chess.person_chess_pieces,
                                           chess.computer_chess_pieces])
    print('%s' % ('You First'
                  if chess.first_player == chess.person_chess_pieces
                  else 'Computer First'))

    if chess.first_player == chess.computer_chess_pieces:
        chess.put_chess(chess.computer_chess_pieces, 7, 7)
        chess.display_chess_board()

    # main loop
    while True:
        # user's move
        coordinate = list(map(int,
                              filter(lambda x: x.isdigit(),
                                     input("Row and Column: (seperate by space)\n").split())))
        try:
            chess.put_chess(chess.person_chess_pieces, coordinate[0], coordinate[1])
        except IndexError:
            print("Invalid input, please try again")
            continue
        except CoordinateError as err:
            print(f"This coordinate has been taken by {err}, please try again")
            continue
        if chess.check_winner():
            print("Winner is YOU")
            break

        # computer's move
        chess.analyse()
        # chess.display_chess_board()
        # print()
        # chess.display_score_board()
        if chess.check_winner():
            print("Winner is COMPUTER")
            break


if __name__ == '__main__':
    main()
