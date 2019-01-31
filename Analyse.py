import numpy as np

def analyse(chess_board):
    value_board = np.zeros((15, 15), dtype=np.float)
    for i in range(15):
        for j in range(15):
            if chess_board[i, j] != 0:
                # vertical(|)
                if i - 2 >= 0 and i + 2 <= 14:
                    coeff = np.random.uniform(1, 2)
                    vertical_sum = np.sum(chess_board[i-2:i+3, j])
                    value_board[i-2, j] += (vertical_sum - chess_board[i-2, j]) ** 2
                    value_board[i-1, j] += coeff * (vertical_sum - chess_board[i-1, j]) ** 2
                    value_board[i+1, j] += coeff * (vertical_sum - chess_board[i+1, j]) ** 2
                    value_board[i+2, j] += (vertical_sum - chess_board[i+2, j]) ** 2
                    if (chess_board[i - 1, j] == chess_board[i, j] and
                        chess_board[i + 1, j] == chess_board[i, j]):
                        value_board[i - 2, j], value_board[i + 2, j] = {
                            (0,0): (5000, 5000),
                            (chess_board[i, j],0): (0, 5000),
                            (0,chess_board[i, j]): (5000, 0),
                            (chess_board[i, j],chess_board[i, j]): (0, 0),
                        }.get((chess_board[i - 2, j], chess_board[i + 2, j]), (0,0))
                # horizontal(-)
                if j - 2 >= 0 and j + 2 <= 14:
                    coeff = np.random.uniform(1, 2)
                    horizontal_sum = np.sum(chess_board[i, j-2:j+3])
                    value_board[i, j-2] += (horizontal_sum - chess_board[i, j-2]) ** 2
                    value_board[i, j-1] += coeff * (horizontal_sum - chess_board[i, j-1]) ** 2
                    value_board[i, j+1] += coeff * (horizontal_sum - chess_board[i, j+1]) ** 2
                    value_board[i, j+2] += (horizontal_sum - chess_board[i, j+2]) ** 2
                    if (chess_board[i, j - 1] == chess_board[i, j] and
                        chess_board[i, j + 1] == chess_board[i, j]):
                        value_board[i, j - 2], value_board[i, j + 2] = {
                            (0,0): (5000, 5000),
                            (chess_board[i, j],0): (0, 5000),
                            (0,chess_board[i, j]): (5000, 0),
                            (chess_board[i, j],chess_board[i, j]): (0, 0),
                        }.get((chess_board[i, j - 2], chess_board[i, j + 2]), (0,0))
                # slash(\)
                if i - 2 >= 0 and j - 2 >= 0 and i + 2 <= 14 and j + 2 <= 14:
                    coeff = np.random.uniform(1, 2)
                    slash_sum = np.sum(np.diag(chess_board[i-2:i+3, j-2:j+3]))
                    value_board[i-2, j+2] += (slash_sum - chess_board[i-2, j+2]) ** 2
                    value_board[i-1, j+1] += coeff * (slash_sum - chess_board[i-1, j+1]) ** 2
                    value_board[i+1, j-1] += coeff * (slash_sum - chess_board[i+1, j-1]) ** 2
                    value_board[i+2, j-2] += (slash_sum - chess_board[i+2, j-2]) ** 2
                    if (chess_board[i - 1, j + 1] == chess_board[i, j] and
                        chess_board[i + 1, j - 1] == chess_board[i, j]):
                        value_board[i - 2, j + 2], value_board[i + 2, j - 2] = {
                            (0,0): (5000, 5000),
                            (chess_board[i, j],0): (0, 5000),
                            (0,chess_board[i, j]): (5000, 0),
                            (chess_board[i, j],chess_board[i, j]): (0, 0),
                        }.get((chess_board[i - 2, j + 2], chess_board[i + 2, j - 2]), (0,0))
                # backslash(/)
                if i - 2 >= 0 and j - 2 >= 0 and i + 2 <= 14 and j + 2 <= 14:
                    coeff = np.random.uniform(1, 2)
                    backslash_sum = np.sum(np.diag(np.fliplr(chess_board[i-2:i+3, j-2:j+3])))
                    value_board[i-2, j-2] += (backslash_sum - chess_board[i-2, j-2]) ** 2
                    value_board[i-1, j-1] += coeff * (backslash_sum - chess_board[i-1, j-1]) ** 2
                    value_board[i+1, j+1] += coeff * (backslash_sum - chess_board[i+1, j+1]) ** 2
                    value_board[i+2, j+2] += (backslash_sum - chess_board[i+2, j+2]) ** 2
                    if (chess_board[i - 1, j - 1] == chess_board[i, j] and
                        chess_board[i + 1, j + 1] == chess_board[i, j]):
                        value_board[i - 2, j - 2], value_board[i + 2, j + 2] = {
                            (0,0): (5000, 5000),
                            (chess_board[i, j],0): (0, 5000),
                            (0,chess_board[i, j]): (5000, 0),
                            (chess_board[i, j],chess_board[i, j]): (0, 0),
                        }.get((chess_board[i - 2, j - 2], chess_board[i + 2, j + 2]), (0,0))
                # avoid self
                value_board[i, j] = -10000
    return value_board