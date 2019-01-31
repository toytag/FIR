import numpy as np

def analyse(chess_board):
    value_board = np.zeros((15, 15), dtype=np.float)
    for i in range(15):
        for j in range(15):
            if chess_board[i, j] != 0:
                # avoid self
                value_board[i, j] = -10000
                # vertical(|)
                if i - 2 >= 0 and i + 2 <= 14:
                    vertical_sum = np.sum(chess_board[i-2:i+3, j])
                    value_board[i-2, j] += (vertical_sum - chess_board[i-2, j]) ** 2
                    value_board[i-1, j] += 2 * (vertical_sum - chess_board[i-1, j]) ** 2
                    value_board[i+1, j] += 2 * (vertical_sum - chess_board[i+1, j]) ** 2
                    value_board[i+2, j] += (vertical_sum - chess_board[i+2, j]) ** 2
                # horizontal(-)
                if j - 2 >= 0 and j + 2 <= 14:
                    horizontal_sum = np.sum(chess_board[i, j-2:j+3])
                    value_board[i, j-2] += (horizontal_sum - chess_board[i, j-2]) ** 2
                    value_board[i, j-1] += 2 * (horizontal_sum - chess_board[i, j-1]) ** 2
                    value_board[i, j+1] += 2 * (horizontal_sum - chess_board[i, j+1]) ** 2
                    value_board[i, j+2] += (horizontal_sum - chess_board[i, j+2]) ** 2
                # diagonal(\)
                if i - 2 >= 0 and j - 2 >= 0 and i + 2 <= 14 and j + 2 <= 14:
                    slash_sum = np.sum(np.diag(chess_board[i-2:i+3, j-2:j+3]))
                    value_board[i-2, j+2] += (slash_sum - chess_board[i-2, j+2]) ** 2
                    value_board[i-1, j+1] += 2 * (slash_sum - chess_board[i-1, j+1]) ** 2
                    value_board[i+1, j-1] += 2 * (slash_sum - chess_board[i+1, j-1]) ** 2
                    value_board[i+2, j-2] += (slash_sum - chess_board[i+2, j-2]) ** 2
                # diagonal(/)
                if i - 2 >= 0 and j - 2 >= 0 and i + 2 <= 14 and j + 2 <= 14:
                    backslash_sum = np.sum(np.diag(np.fliplr(chess_board[i-2:i+3, j-2:j+3])))
                    value_board[i-2, j-2] += (backslash_sum - chess_board[i-2, j-2]) ** 2
                    value_board[i-1, j-1] += 2 * (backslash_sum - chess_board[i-1, j-1]) ** 2
                    value_board[i+1, j+1] += 2 * (backslash_sum - chess_board[i+1, j+1]) ** 2
                    value_board[i+2, j+2] += (backslash_sum - chess_board[i+2, j+2]) ** 2
    return value_board