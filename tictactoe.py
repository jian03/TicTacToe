import tkinter
from tkinter import messagebox

from tictactoe_game_engine import TictactoeGameEngine

class Tictactoe:
    def __init__(self):
        self.game_engine = TictactoeGameEngine()

    def play(self):
        print(self.game_engine) #show board

        #무한 반복
        while True:
            #input row, col
            row = int(input('row : '))
            col = int(input('col : '))

            #set
            self.game_engine.set(row, col)

            #show board
            print(self.game_engine)

            #check_winner 승패가 결정나면, break
            winner = self.game_engine.check_winner()
            if winner != None:
                break

        #결과 출력
        if winner == 'O':
            print('O 이김')
        elif winner == 'X':
            print('X 이김')
        elif winner == 'd':
            print('무승부')


class TictactoeGUI:
    def __init__(self):
        self.game_engine = TictactoeGameEngine()
        self.init_ui()

    def init_ui(self):
        self.CANVAS_SIZE = 300

        self.root = tkinter.Tk()
        self.root.title('틱 택 토')    #title
        self.root.geometry(str(self.CANVAS_SIZE) + 'x' + str(self.CANVAS_SIZE))    #size => 300x300
        self.canvas = tkinter.Canvas(self.root, bg = 'white', width = self.CANVAS_SIZE, height = self.CANVAS_SIZE)
        self.canvas.pack();     #pack() == wrap_content,창에 요소를 배치하는 역할... 자바에서 add 느낌

        #{'O' : PhotoImage객체, 'X' : PhotoImage 객체}
        self.images = {}    #dict()으로 써도 됨
        self.images['O'] = tkinter.PhotoImage(file = 'O.gif')
        self.images['X'] = tkinter.PhotoImage(file = 'X.gif')

        self.canvas.bind('<Button - 1>', self.click_handler)

    def click_handler(self, event):
        x = event.x
        y = event.y

        #클릭 처리
        col = x // 100 + 1
        row = y // 100 + 1
        self.game_engine.set(row, col)

        #show board
        #print(self.game_engine)
        self.draw_board()
        #승자 결정
        winner = self.game_engine.check_winner()

        #결과 보여 주기
        if winner == 'O':
            # print('O 이김')
            messagebox.showinfo('Game Over', 'O 이김')
            self.root.quit()
        elif winner == 'X':
            # print('X 이김')
            messagebox.showinfo('Game Over', 'X 이김')
            self.root.quit()
        elif winner == 'd':
            # print('무승부')
            messagebox.showinfo('Game Over', '무승부')
            self.root.quit()
    def draw_board(self):
        x = 0
        y = 0
        for i, v in enumerate(self.game_engine.board):
            if v == 'O':
                self.canvas.create_image(x, y, anchor='nw', image=self.images['O'])
            elif v == 'X':
                self.canvas.create_image(x, y, anchor='nw', image=self.images['X'])

            TILE_SIZE = self.CANVAS_SIZE//3
            x += TILE_SIZE
            if i % 3 == 2:
                x = 0
                y += TILE_SIZE

    def play(self):
        self.root.mainloop()    #mainloop()를 선언해야 창이 나온다.

if __name__ == '__main__':
    #ttt = Tictactoe()
    ttt = TictactoeGUI()
    ttt.play()