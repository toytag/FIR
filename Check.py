def check(chess_board, i, j):
    if chess_board[i][j] != 0:
        try:
            if ((chess_board[i - 2][j]      == chess_board[i][j] and
                    chess_board[i - 1][j]      == chess_board[i][j] and
                    chess_board[i + 1][j]      == chess_board[i][j] and
                    chess_board[i + 2][j]      == chess_board[i][j]) or
                (chess_board[i - 2][j - 2]  == chess_board[i][j] and
                    chess_board[i - 1][j - 1]  == chess_board[i][j] and
                    chess_board[i + 1][j + 1]  == chess_board[i][j] and
                    chess_board[i + 2][j + 2]  == chess_board[i][j]) or
                (chess_board[i - 2][j + 2]  == chess_board[i][j] and
                    chess_board[i - 1][j + 1]  == chess_board[i][j] and
                    chess_board[i + 1][j - 1]  == chess_board[i][j] and
                    chess_board[i + 2][j - 2]  == chess_board[i][j]) or
                (chess_board[i][j - 2]      == chess_board[i][j] and
                    chess_board[i][j - 1]      == chess_board[i][j] and
                    chess_board[i][j + 1]      == chess_board[i][j] and
                    chess_board[i][j + 2]      == chess_board[i][j])):
                return True
        except IndexError:
            pass