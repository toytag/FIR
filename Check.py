import numpy as np

def check(chess_board):
    for i in range(15):
        for j in range(15):
            if chess_board[i][j] != 0:
                # vertical(|)
                if i - 2 >= 0 and i + 2 <= 14:
                    if abs(np.sum(chess_board[i-2:i+3, j])) == 5:
                        return True
                # horizontal(-)
                if j - 2 >= 0 and j + 2 <= 14:
                    if abs(np.sum(chess_board[i, j-2:j+3])) == 5:
                        return True
                # diagnoal(\)
                if i - 2 >= 0 and i + 2 <= 14 and j - 2 >= 0 and j + 2 <= 14:
                    if abs(np.sum(np.diag(chess_board[i-2:i+3, j-2:j+3]))) == 5:
                        return True
                # diagonal(/)
                if i - 2 >= 0 and i + 2 <= 14 and j - 2 >= 0 and j + 2 <= 14:
                    if abs(np.sum(np.diag(np.fliplr(chess_board[i-2:i+3, j-2:j+3])))) == 5:
                        return True