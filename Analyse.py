def analyse(chess_board, score_board):
    for i in range(15):
        for j in range(15):
            try:
                if chess_board[i][j] != 0:
                    # avoid self
                    score_board[i][j] = -100000
                    # vertical
                    vertical_sum = chess_board[i - 2][j] + chess_board[i - 1][j] + \
                                   chess_board[i][j] + chess_board[i + 1][j] + chess_board[i + 2][j]
                    score_board[i - 2][j] += (vertical_sum - chess_board[i - 2][j]) ** 4
                    score_board[i - 1][j] += (vertical_sum - chess_board[i - 1][j]) ** 4
                    score_board[i + 1][j] += (vertical_sum - chess_board[i + 1][j]) ** 4
                    score_board[i + 2][j] += (vertical_sum - chess_board[i + 2][j]) ** 4
                    # horizontal
                    horizontal_sum = chess_board[i][j - 2] + chess_board[i][j - 1] + \
                                     chess_board[i][j] + chess_board[i][j + 1] + chess_board[i][j + 2]
                    score_board[i][j - 2] += (horizontal_sum - chess_board[i][j - 2]) ** 4
                    score_board[i][j - 1] += (horizontal_sum - chess_board[i][j - 1]) ** 4
                    score_board[i][j + 1] += (horizontal_sum - chess_board[i][j + 1]) ** 4
                    score_board[i][j + 2] += (horizontal_sum - chess_board[i][j + 2]) ** 4
                    # slash
                    slash_sum = chess_board[i - 2][j + 2] + chess_board[i - 1][j + 1] + \
                                chess_board[i][j] + chess_board[i + 1][j - 1] + chess_board[i + 2][j - 2]
                    score_board[i - 2][j + 2] += (slash_sum - chess_board[i - 2][j - 2]) ** 4
                    score_board[i - 1][j + 1] += (slash_sum - chess_board[i - 1][j - 1]) ** 4
                    score_board[i + 1][j - 1] += (slash_sum - chess_board[i + 1][j + 1]) ** 4
                    score_board[i + 2][j - 2] += (slash_sum - chess_board[i + 2][j + 2]) ** 4
                    # backslash
                    backslash_sum = chess_board[i - 2][j - 2] + chess_board[i - 1][j - 1] + \
                                    chess_board[i][j] + chess_board[i + 1][j + 1] + chess_board[i + 2][j + 2]
                    score_board[i - 2][j - 2] += (backslash_sum - chess_board[i - 2][j - 2]) ** 4
                    score_board[i - 1][j - 1] += (backslash_sum - chess_board[i - 1][j - 1]) ** 4
                    score_board[i + 1][j + 1] += (backslash_sum - chess_board[i + 1][j + 1]) ** 4
                    score_board[i + 2][j + 2] += (backslash_sum - chess_board[i + 2][j + 2]) ** 4
                    
            except IndexError:
                pass