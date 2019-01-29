import math, time
import tkinter as tk
from tkinter import messagebox
from FIR import Chess


class FIRenv(tk.Tk):
    def __init__(self):
        # set up gui
        super().__init__()
        self.title('FIR GAME')
        self.geometry('630x630')
        self.__create_canvas()
        self.__setup_chess_board()
        # set up core
        self.chess = Chess()
        if self.chess.first_player == self.chess.computer_chess_pieces:
            self.__put_circle(7, 7)

    
    def __create_canvas(self):
        self.canvas = tk.Canvas(self, bg='lightcyan', width=630, height=630)
        self.canvas.pack()

    def __setup_chess_board(self):
        for i in range(42, 630, 42):
            # vertical line
            self.canvas.create_line(i, 0, i, 630)
            # horizontal line
            self.canvas.create_line(0, i, 630, i)
        # bind events
        self.canvas.bind('<Button-1>', self.__scheduler)
        # self.canvas.bind('<Button-2>', self.__regret)

    def __put_circle(self, x, y):
        # print('computer', x, y)
        self.chess.put_chess(Chess.computer_chess_pieces, x, y)
        i = x * 42
        j = y * 42
        self.canvas.create_oval(i+4, j+4, i+38, j+38, width=3, outline='#e59832')
        self.update()

    def __put_cross(self, event):
        i = math.floor(event.x/42)
        j = math.floor(event.y/42)
        # print('me', i, j)
        if self.chess.put_chess(Chess.person_chess_pieces, i, j):
            return True
        i *= 42
        j *= 42
        self.canvas.create_line(i+5, j+5, i+37, j+37, width=3, fill='#2585e5')
        self.canvas.create_line(i+37, j+5, i+5, j+37, width=3, fill='#2585e5')
        self.update()

    def __scheduler(self, event):
        if self.__put_cross(event):
            if self.chess.check_winner():
                messagebox.showinfo(title='FIR GAME', message='You Win')
                self.destroy()
            return True
        self.__put_circle(*self.chess.analyse_put())
        if self.chess.check_winner():
            messagebox.showinfo(title='FIR GAME', message='You Lose')
            self.destroy()

    # def __regret(self):
    #     if self.core.history != []:
    #         self.core.chess_board[self.core.history.pop()] = 0
    #         self.canvas.delete(str(self.core.counter)+'_')
    #         self.core.counter -= 1


if __name__ == '__main__':
    chess = FIRenv()
    chess.mainloop()
