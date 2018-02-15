def stop_being_silly(chess_board, score_board):
    for i in range(15):
        for j in range(15):
            if chess_board[i][j] != 0:
                # vertical
                if i - 2 >= 0 and i + 2 <= 14:
                    if (chess_board[i - 1][j] == chess_board[i][j] and
                        chess_board[i + 1][j] == chess_board[i][j]):
                        score_board[i - 2][j], score_board[i + 2][j] = {
                            (0,0): (5000, 5000),
                            (chess_board[i][j],0): (0, 5000),
                            (0,chess_board[i][j]): (5000, 0),
                            (chess_board[i][j],chess_board[i][j]): (0, 0),
                        }.get((chess_board[i - 2][j], chess_board[i + 2][j]), (0,0))
                # horizontal
                if j - 2 >= 0 and j + 2 <= 14:
                    if (chess_board[i][j - 1] == chess_board[i][j] and
                        chess_board[i][j + 1] == chess_board[i][j]):
                        score_board[i][j - 2], score_board[i][j + 2] = {
                            (0,0): (5000, 5000),
                            (chess_board[i][j],0): (0, 5000),
                            (0,chess_board[i][j]): (5000, 0),
                            (chess_board[i][j],chess_board[i][j]): (0, 0),
                        }.get((chess_board[i][j - 2], chess_board[i][j + 2]), (0,0))
                # slash
                if i - 2 >= 0 and i + 2 <= 14 and j - 2 >= 0 and j + 2 <= 14:
                    if (chess_board[i - 1][j + 1] == chess_board[i][j] and
                        chess_board[i + 1][j - 1] == chess_board[i][j]):
                        score_board[i - 2][j + 2], score_board[i + 2][j - 2] = {
                            (0,0): (5000, 5000),
                            (chess_board[i][j],0): (0, 5000),
                            (0,chess_board[i][j]): (5000, 0),
                            (chess_board[i][j],chess_board[i][j]): (0, 0),
                        }.get((chess_board[i - 2][j + 2], chess_board[i + 2][j - 2]), (0,0))
                # backslash 
                if i - 2 >= 0 and i + 2 <= 14 and j - 2 >= 0 and j + 2 <= 14:
                    if (chess_board[i - 1][j - 1] == chess_board[i][j] and
                        chess_board[i + 1][j + 1] == chess_board[i][j]):
                        score_board[i - 2][j - 2], score_board[i + 2][j + 2] = {
                            (0,0): (5000, 5000),
                            (chess_board[i][j],0): (0, 5000),
                            (0,chess_board[i][j]): (5000, 0),
                            (chess_board[i][j],chess_board[i][j]): (0, 0),
                        }.get((chess_board[i - 2][j - 2], chess_board[i + 2][j + 2]), (0,0))