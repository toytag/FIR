import math
import tkinter as tk
from tkinter import messagebox
from fir import fir


class firGUI(tk.Tk):
    def __init__(self):
        # set up gui
        super().__init__()
        self.title('FIR GAME')
        self.geometry('630x630')
        self.__setup_chess_board()
        # set up chess
        self.chess = fir()
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
        if self.chess.put_chess(self.chess.BLACK, x, y):
            winner = self.chess.check_winner()
            if not winner:
                self.chess.put_chess(self.chess.WHITE, *self.chess.analyse())
                winner = self.chess.check_winner()
        self.__update_chess_board()
        if winner == self.chess.BLACK:
            messagebox.showinfo(
                title='Game over',
                message='Black win!'
            )
            self.destroy()
        elif winner == self.chess.WHITE:
            messagebox.showinfo(
                title='Game over',
                message='White win!'
            )
            self.destroy()

if __name__ == '__main__':
    firGUI()