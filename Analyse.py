import numpy as np

def depth_analyse(chess_board, score_board, depth):
    cb_backup = chess_board.copy()
    sb_backup = score_board.copy()
    stop_being_silly(cb_backup, sb_backup)
    analyse(cb_backup, sb_backup)
    top_score_ls = get_top3(sb_backup.ravel())
    if depth == 1:
        return top_score_ls[0]
    ls = []
    for option in top_score_ls:
        cb_backup[option[1]][option[2]] = -1 if depth%2 == 1 else 1
        counter_option = depth_analyse(cb_backup, score_board, depth - 1)
        ls.append(option[0] - counter_option[0])
        cb_backup = chess_board.copy()
    return top_score_ls[ls.index(max(ls))]

def analyse(chess_board, score_board):
    for i in range(15):
        for j in range(15):
            if chess_board[i, j] != 0:
                # avoid self
                score_board[i, j] = -10000
                # vertical(|)
                if i - 2 >= 0 and i + 2 <= 14:
                    vertical_sum = np.sum(chess_board[i-2:i+3, j])
                    score_board[i-2, j] += (vertical_sum - chess_board[i-2, j]) ** 2
                    score_board[i-1, j] += 2 * (vertical_sum - chess_board[i-1, j]) ** 2
                    score_board[i+1, j] += 2 * (vertical_sum - chess_board[i+1, j]) ** 2
                    score_board[i+2, j] += (vertical_sum - chess_board[i+2, j]) ** 2
                # horizontal(-)
                if j - 2 >= 0 and j + 2 <= 14:
                    horizontal_sum = np.sum(chess_board[i, j-2:j+3])
                    score_board[i, j-2] += (horizontal_sum - chess_board[i, j-2]) ** 2
                    score_board[i, j-1] += 2 * (horizontal_sum - chess_board[i, j-1]) ** 2
                    score_board[i, j+1] += 2 * (horizontal_sum - chess_board[i, j+1]) ** 2
                    score_board[i, j+2] += (horizontal_sum - chess_board[i, j+2]) ** 2
                # diagnoal(\)
                if i - 2 >= 0 and j - 2 >= 0 and i + 2 <= 14 and j + 2 <= 14:
                    slash_sum = np.sum(np.diag(chess_board[i-2:i+3, j-2:j+3]))
                    score_board[i-2, j+2] += (slash_sum - chess_board[i-2, j+2]) ** 2
                    score_board[i-1, j+1] += 2 * (slash_sum - chess_board[i-1, j+1]) ** 2
                    score_board[i+1, j-1] += 2 * (slash_sum - chess_board[i+1, j-1]) ** 2
                    score_board[i+2, j-2] += (slash_sum - chess_board[i+2, j-2]) ** 2
                # diagonal(/)
                if i - 2 >= 0 and j - 2 >= 0 and i + 2 <= 14 and j + 2 <= 14:
                    backslash_sum = np.sum(np.diag(np.fliplr(chess_board[i-2:i+3, j-2:j+3])))
                    score_board[i-2, j-2] += (backslash_sum - chess_board[i-2, j-2]) ** 2
                    score_board[i-1, j-1] += 2 * (backslash_sum - chess_board[i-1, j-1]) ** 2
                    score_board[i+1, j+1] += 2 * (backslash_sum - chess_board[i+1, j+1]) ** 2
                    score_board[i+2, j+2] += (backslash_sum - chess_board[i+2, j+2]) ** 2

def stop_being_silly(chess_board, score_board):
    for i in range(15):
        for j in range(15):
            if chess_board[i, j] != 0:
                # vertical
                if i - 2 >= 0 and i + 2 <= 14:
                    if (chess_board[i - 1, j] == chess_board[i, j] and
                        chess_board[i + 1, j] == chess_board[i, j]):
                        score_board[i - 2, j], score_board[i + 2, j] = {
                            (0,0): (5000, 5000),
                            (chess_board[i, j],0): (0, 5000),
                            (0,chess_board[i, j]): (5000, 0),
                            (chess_board[i, j],chess_board[i, j]): (0, 0),
                        }.get((chess_board[i - 2, j], chess_board[i + 2, j]), (0,0))
                # horizontal
                if j - 2 >= 0 and j + 2 <= 14:
                    if (chess_board[i, j - 1] == chess_board[i, j] and
                        chess_board[i, j + 1] == chess_board[i, j]):
                        score_board[i, j - 2], score_board[i, j + 2] = {
                            (0,0): (5000, 5000),
                            (chess_board[i, j],0): (0, 5000),
                            (0,chess_board[i, j]): (5000, 0),
                            (chess_board[i, j],chess_board[i, j]): (0, 0),
                        }.get((chess_board[i, j - 2], chess_board[i, j + 2]), (0,0))
                # slash
                if i - 2 >= 0 and i + 2 <= 14 and j - 2 >= 0 and j + 2 <= 14:
                    if (chess_board[i - 1, j + 1] == chess_board[i, j] and
                        chess_board[i + 1, j - 1] == chess_board[i, j]):
                        score_board[i - 2, j + 2], score_board[i + 2, j - 2] = {
                            (0,0): (5000, 5000),
                            (chess_board[i, j],0): (0, 5000),
                            (0,chess_board[i, j]): (5000, 0),
                            (chess_board[i, j],chess_board[i, j]): (0, 0),
                        }.get((chess_board[i - 2, j + 2], chess_board[i + 2, j - 2]), (0,0))
                # backslash 
                if i - 2 >= 0 and i + 2 <= 14 and j - 2 >= 0 and j + 2 <= 14:
                    if (chess_board[i - 1, j - 1] == chess_board[i, j] and
                        chess_board[i + 1, j + 1] == chess_board[i, j]):
                        score_board[i - 2, j - 2], score_board[i + 2, j + 2] = {
                            (0,0): (5000, 5000),
                            (chess_board[i, j],0): (0, 5000),
                            (0,chess_board[i, j]): (5000, 0),
                            (chess_board[i, j],chess_board[i, j]): (0, 0),
                        }.get((chess_board[i - 2, j - 2], chess_board[i + 2, j + 2]), (0,0))

def get_top3(score_ls):
    top_score_ls = []
    for _ in range(3):
        location = score_ls.argmax()
        x, y = divmod(location, 15)
        top_score_ls.append([score_ls[location], x, y])
        score_ls[location] = 0
    return top_score_ls