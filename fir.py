import numpy as np


class fir:
    BLACK = 1
    WHITE = -1

    def __init__(self):
        self.chess_board = np.zeros((15, 15), dtype=np.int8)
        self.round_counter = 0

    def put_chess(self, identity, x, y):
        if self.chess_board[x, y] != 0:
            return False
        self.chess_board[x, y] = identity
        self.round_counter += 1
        return True

    def analyse(self):
        return divmod(np.argmax(analyse(self.chess_board)), 15)

    def check_winner(self):
        return check(self.chess_board)


def analyse(chess_board):
    value_board = np.zeros((15, 15), dtype=np.float)
    for i in range(15):
        for j in range(15):
            if chess_board[i, j] != 0:
                # vertical(|)
                if i - 2 >= 0 and i + 2 <= 14:
                    vertical_sum = np.sum(chess_board[i-2:i+2+1, j])
                    for k in [-2, -1, 1, 2]:
                        value_board[i+k, j] += (vertical_sum - chess_board[i+k, j]) ** 2 / abs(k)
                    # three continuous identical
                    if (chess_board[i-1, j] == chess_board[i, j] and
                        chess_board[i+1, j] == chess_board[i, j]):
                        value_board[i-2, j], value_board[i+2, j] = {
                            (0,0): (5000, 5000),
                            (chess_board[i, j],0): (0, 5000),
                            (0,chess_board[i, j]): (5000, 0),
                            (chess_board[i, j],chess_board[i, j]): (0, 0),
                        }.get((chess_board[i-2, j], chess_board[i+2, j]), (0, 0))
                # horizontal(-)
                if j - 2 >= 0 and j + 2 <= 14:
                    horizontal_sum = np.sum(chess_board[i, j-2:j+2+1])
                    for k in [-2, -1, 1, 2]:
                        value_board[i, j+k] += (horizontal_sum - chess_board[i, j+k]) ** 2 / abs(k)
                    # three continuous identical
                    if (chess_board[i, j-1] == chess_board[i, j] and
                        chess_board[i, j+1] == chess_board[i, j]):
                        value_board[i, j-2], value_board[i, j+2] = {
                            (0,0): (5000, 5000),
                            (chess_board[i, j],0): (0, 5000),
                            (0,chess_board[i, j]): (5000, 0),
                            (chess_board[i, j],chess_board[i, j]): (0, 0),
                        }.get((chess_board[i, j-2], chess_board[i, j+2]), (0, 0))
                # slash(\)
                if i - 2 >= 0 and j - 2 >= 0 and i + 2 <= 14 and j + 2 <= 14:
                    slash_sum = np.sum(np.diag(chess_board[i-2:i+2+1, j-2:j+2+1]))
                    for k in [-2, -1, 1, 2]:
                        value_board[i+k, j-k] += (slash_sum - chess_board[i+k, j-k]) ** 2 / abs(k)
                    # three continuous identical
                    if (chess_board[i-1, j+1] == chess_board[i, j] and
                        chess_board[i+1, j-1] == chess_board[i, j]):
                        value_board[i-2, j+2], value_board[i+2, j-2] = {
                            (0,0): (5000, 5000),
                            (chess_board[i, j],0): (0, 5000),
                            (0,chess_board[i, j]): (5000, 0),
                            (chess_board[i, j],chess_board[i, j]): (0, 0),
                        }.get((chess_board[i-2, j+2], chess_board[i+2, j-2]), (0, 0))
                # backslash(/)
                if i - 2 >= 0 and j - 2 >= 0 and i + 2 <= 14 and j + 2 <= 14:
                    backslash_sum = np.sum(np.diag(np.fliplr(chess_board[i-2:i+2+1, j-2:j+2+1])))
                    for k in [-2, -1, 1, 2]:
                        value_board[i+k, j] += (backslash_sum - chess_board[i+k, j+k]) ** 2 / abs(k)
                    # three continuous identical
                    if (chess_board[i-1, j-1] == chess_board[i, j] and
                        chess_board[i+1, j+1] == chess_board[i, j]):
                        value_board[i-2, j-2], value_board[i+2, j+2] = {
                            (0, 0): (5000, 5000),
                            (chess_board[i, j], 0): (0, 5000),
                            (0, chess_board[i, j]): (5000, 0),
                            (chess_board[i, j], chess_board[i, j]): (0, 0),
                        }.get((chess_board[i-2, j-2], chess_board[i+2, j+2]), (0, 0))
    value_board[chess_board != 0] = 0
    return value_board

def check(chess_board):
    for i in range(15):
        for j in range(15):
            if chess_board[i, j] != 0:
                # vertical(|)
                if i - 2 >= 0 and i + 2 <= 14:
                    if np.sum(chess_board[i-2:i+3, j]) == 5:
                        return fir.BLACK
                    elif np.sum(chess_board[i-2:i+3, j]) == -5:
                        return fir.WHITE
                # horizontal(-)
                if j - 2 >= 0 and j + 2 <= 14:
                    if np.sum(chess_board[i, j-2:j+3]) == 5:
                        return fir.BLACK
                    elif np.sum(chess_board[i, j-2:j+3]) == -5:
                        return fir.WHITE
                # diagonal(\)
                if i - 2 >= 0 and i + 2 <= 14 and j - 2 >= 0 and j + 2 <= 14:
                    if np.sum(np.diag(chess_board[i-2:i+3, j-2:j+3])) == 5:
                        return fir.BLACK
                    if np.sum(np.diag(chess_board[i-2:i+3, j-2:j+3])) == -5:
                        return fir.WHITE
                # diagonal(/)
                if i - 2 >= 0 and i + 2 <= 14 and j - 2 >= 0 and j + 2 <= 14:
                    if np.sum(np.diag(np.fliplr(chess_board[i-2:i+3, j-2:j+3]))) == 5:
                        return fir.BLACK
                    if np.sum(np.diag(np.fliplr(chess_board[i-2:i+3, j-2:j+3]))) == -5:
                        return fir.WHITE
    return None