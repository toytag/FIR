import numpy as np

def analyse(chess_board, score_board):
    for i in range(15):
        for j in range(15):
            if chess_board[i][j] != 0:
                # avoid self
                score_board[i][j] = -1000
                # vertical
                if i - 2 >= 0 and i + 2 <= 14:
                    vertical_sum = chess_board[i - 2][j] + chess_board[i - 1][j] + \
                                chess_board[i][j] + chess_board[i + 1][j] + chess_board[i + 2][j]
                    score_board[i - 2][j] += (vertical_sum - chess_board[i - 2][j]) ** 2
                    score_board[i - 1][j] += 2 * (vertical_sum - chess_board[i - 1][j]) ** 2 + 2
                    score_board[i + 1][j] += 2 * (vertical_sum - chess_board[i + 1][j]) ** 2 + 2
                    score_board[i + 2][j] += (vertical_sum - chess_board[i + 2][j]) ** 2
                # horizontal
                if j - 2 >= 0 and j + 2 <= 14:
                    horizontal_sum = chess_board[i][j - 2] + chess_board[i][j - 1] + \
                                    chess_board[i][j] + chess_board[i][j + 1] + chess_board[i][j + 2]
                    score_board[i][j - 2] += (horizontal_sum - chess_board[i][j - 2]) ** 2
                    score_board[i][j - 1] += 2 * (horizontal_sum - chess_board[i][j - 1]) ** 2 + 2
                    score_board[i][j + 1] += 2 * (horizontal_sum - chess_board[i][j + 1]) ** 2 + 2
                    score_board[i][j + 2] += (horizontal_sum - chess_board[i][j + 2]) ** 2
                # slash
                if i - 2 >= 0 and j - 2 >= 0 and i + 2 <= 14 and j + 2 <= 14:
                    slash_sum = chess_board[i - 2][j + 2] + chess_board[i - 1][j + 1] + \
                                chess_board[i][j] + chess_board[i + 1][j - 1] + chess_board[i + 2][j - 2]
                    score_board[i - 2][j + 2] += (slash_sum - chess_board[i - 2][j + 2]) ** 2
                    score_board[i - 1][j + 1] += 2 * (slash_sum - chess_board[i - 1][j + 1]) ** 2
                    score_board[i + 1][j - 1] += 2 * (slash_sum - chess_board[i + 1][j - 1]) ** 2
                    score_board[i + 2][j - 2] += (slash_sum - chess_board[i + 2][j - 2]) ** 2
                # backslash
                if i - 2 >= 0 and j - 2 >= 0 and i + 2 <= 14 and j + 2 <= 14:
                    backslash_sum = chess_board[i - 2][j - 2] + chess_board[i - 1][j - 1] + \
                                    chess_board[i][j] + chess_board[i + 1][j + 1] + chess_board[i + 2][j + 2]
                    score_board[i - 2][j - 2] += (backslash_sum - chess_board[i - 2][j - 2]) ** 2
                    score_board[i - 1][j - 1] += 2 * (backslash_sum - chess_board[i - 1][j - 1]) ** 2
                    score_board[i + 1][j + 1] += 2 * (backslash_sum - chess_board[i + 1][j + 1]) ** 2
                    score_board[i + 2][j + 2] += (backslash_sum - chess_board[i + 2][j + 2]) ** 2


def depth_analyse(chess_board, score_board, depth):
    cb_backup = chess_board.copy()
    score_board = np.zeros((15, 15), dtype=np.int32)
    analyse(cb_backup, score_board)
    top_score_ls = get_top3(score_board.reshape(15 * 15).tolist())
    if depth == 1:
        return top_score_ls[0]
    ls = []
    for option in top_score_ls:
        cb_backup[option[1]][option[2]] = -1 if depth % 2 == 0 else 1
        counter_option = depth_analyse(cb_backup, score_board, depth - 1)
        ls.append(option[0] - counter_option[0])
        cb_backup = chess_board.copy()
    return top_score_ls[ls.index(max(ls))]

def get_top3(score_ls):
    top_score_ls = []
    for _i in range(3):
        max_score = max(score_ls)
        location = score_ls.index(max_score)
        x, y = divmod(location, 15)
        top_score_ls.append([max_score, x, y])
        score_ls[location] = 0
    return top_score_ls

# def evaluation(chess_board, score_board):
#     cbc = chess_board.copy()
#     for i in range(15):
#         for j in range(15):
#             if score_board[i][j] > 0:
#                 cbc[i][j] = 
                
