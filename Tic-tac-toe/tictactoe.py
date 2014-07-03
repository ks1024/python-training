#! /usr/bin/env python

class Tictactoe:

    board = []
    move_count = None
    marks = {'Foo':'X', 'Bar':'O'}

    def __init__(self):
        # initialize the game board with numbers 1-9
        self.board = list(range(1, 10))
        self.move_count = 0

    def print_board(self):
        b = self.board
        for i, item in enumerate(b):
            if i == 2 or i == 5 or i == 8:
                print item
            else:
                print item, "|",

    def ask_input(self, name):
        while True:
            i = raw_input("It is " + name + "'s turn. Mark a squre with '" + self.marks[name] + "' : ")
            try:
                val = int(i)
            except ValueError:
                print "That's not an int"
                continue
            else:
                if val < 1 or val > 9:
                    print "Pick a squre number 1-9"
                    continue
                elif val not in self.board:
                    print "The square " + i + " has been picked"
                    continue
                else:
                    return val

    def is_gameover(self, x, y, t):
        self.move_count+=1
        gameover = False
        # convert board list to 3*3 matrix
        m = [self.board[0:3], self.board[3:6], self.board[6:9]]
        # check col
        for i in range(3):
            if not m[x][i] == self.marks[t]:
                break
            if i == 2:
                gameover = True
                print "WIN for " + t

        # check row
        for i in range(3):
            if not m[i][y] == self.marks[t]:
                break
            if i == 2:
                gameover = True
                print "WIN for " + t

        # check diag and anti diag
        if x == y:
            for i in range(3):
                if not m[i][i] == self.marks[t]:
                    break
                if i == 2:
                    gameover = True
                    print "WIN for " + t
            for i in range(3):
                if not m[i][2-i] == self.marks[t]:
                    break
                if i == 2:
                    gameover = True
                    print "WIN for " + t

        # check draw
        if self.move_count == 8:
            print "Draw"
            gameover = True

        return gameover
    
    def start_game(self, turn):
        while True:
            self.print_board()
            square = self.ask_input(turn)
            x = (square - 1) / 3
            y = (square - 1) % 3
            self.board[square-1] = self.marks[turn]
            if not self.is_gameover(x, y, turn):
                if turn == 'Foo':
                    turn = 'Bar'
                else:
                    turn = 'Foo'
            else:
                break
                

if __name__ == "__main__":
    tictactoe = Tictactoe()
    tictactoe.start_game('Foo')
