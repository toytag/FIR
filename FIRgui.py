import math, pickle
import tkinter as tk
from tkinter import messagebox
import numpy as np
from FIR import Chess
from Analyse import analyse

class Data:
    def __init__(self):
        self.count = 0
        self.x = np.zeros((2000, 15, 15))
        self.y = np.zeros((2000, 15, 15))
    
    def store(self, chess_board, value_board):
        self.x[self.count] = chess_board
        self.y[self.count] = value_board
        self.count += 1

class FIRenv(tk.Tk):
    def __init__(self):
        # set up gui
        super().__init__()
        self.title('FIR GAME')
        self.geometry('630x630')
        self.__setup_chess_board()
        # set up chess
        self.chess = Chess()
        # self.data = Data()
        # with open('data.pkl', 'rb') as f:
        #     self.data = pickle.load(f)
        # start
        self.mainloop()

    def __setup_chess_board(self):
        self.canvas = tk.Canvas(self, bg='BurlyWood', width=630, height=630)
        self.canvas.pack()
        for i in range(42, 630, 42):
            # vertical line
            self.canvas.create_line(i, 0, i, 630)
            # horizontal line
            self.canvas.create_line(0, i, 630, i)
        # bind events
        self.canvas.bind('<Button-1>', self.__scheduler)

    def __update_chess_board(self):
        self.canvas.delete('chess')
        for x in range(15):
            for y in range(15):
                if self.chess.chess_board[x, y] != 0:
                    self.canvas.create_oval(
                        y * 42 + 3, x * 42 + 3,
                        y * 42 + 39, x * 42 + 39,
                        fill='black' if self.chess.chess_board[x, y] == 1 else 'white',
                        outline='white' if self.chess.chess_board[x, y] == 1 else 'black',
                        tags='chess',
                    )
        self.update()

    def __scheduler(self, event):
        x = math.floor(event.y / 42)
        y = math.floor(event.x / 42)
        # self.data.store(self.chess.chess_board, analyse(self.chess.chess_board))
        if self.chess.put_chess(self.chess.person, x, y):
            # self.data.store(self.chess.chess_board, analyse(self.chess.chess_board))
            self.chess.put_chess(self.chess.computer, *self.chess.analyse())
        self.__update_chess_board()
        winner = self.chess.check_winner()
        if winner == self.chess.person:
            messagebox.showinfo(
                title='Game over',
                message='You win!'
            )
            self.destroy()
        elif winner == self.chess.computer:
            messagebox.showinfo(
                title='Game over',
                message='Computer win'
            )
            self.destroy()

if __name__ == '__main__':
    chess = FIRenv()
    # with open('data.pkl', 'wb') as f:
    #     pickle.dump(chess.data, f)