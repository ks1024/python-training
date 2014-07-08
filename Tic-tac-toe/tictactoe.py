#! /usr/bin/env python

#-------------------------------------------
# Tic-tac-toe terminal based game
# @autor: kyan
# @version: 1.0.1
# features added : 
#   - mark symbol colors
#   - clear console before print game board
#------------------------------------------

import os
from colorama import init, Fore
init(autoreset=True)

class Tictactoe:

    # Clear console command
    __clear = 'cls' if os.name == 'nt' else 'clear'

    def __init__(self):
        """ Initialize the instance variables

        """
        self.board = list(range(1, 10))  # Set the game board state with numbers from 1 to 9
        self.move_count = 0  # Set move count to zero
        self.players = {'Foo': 'X', 'Bar': 'O'}  # Set a dict for two players with name and mark symbol 

    def print_board(self):
        """ Print the game board

        1 | 2 | 3    1 | 2 | 3
        4 | 5 | 6 => 4 | X | 6
        7 | 8 | 9    7 | 8 | 9

        """
        os.system(Tictactoe.__clear)
        self.print_header()
        b = self.board
        for i, item in enumerate(b):
            if i == 2 or i == 5 or i == 8:  # If the right edge char, print with newline
                if item == 'X':
                    print Fore.RED + item
                elif item == 'O':
                    print Fore.GREEN + item
                else:
                    print item
            else:
                if item == 'X':
                    print Fore.RED + item, "|",
                elif item == 'O':
                    print Fore.GREEN + item, "|",
                else:
                    print item, "|",

    def ask_input(self, name):
        """ Ask a certain player to input a square number

        """
        while True:
            i = raw_input("It is " + name + "'s turn. Mark a squre with '" + self.players[name] + "' (input q to quit game) : ")
            try:
                if i == 'q':
                    exit(0)
                else:
                    val = int(i)
            except ValueError:
                print Fore.YELLOW + "That's not an int. Input a square number 1-9"
                continue
            else:
                if val < 1 or val > 9:
                    print Fore.YELLOW + "Pick a squre number 1-9"
                    continue
                elif val not in self.board:
                    print Fore.YELLOW + "The square " + i + " has been picked"
                    continue
                else:
                    return val

    def check_game_state(self, x, y):
        """ Check if the game is over

        """
        self.move_count += 1  
        # convert board list to 3*3 matrix
        m = [self.board[0:3], self.board[3:6], self.board[6:9]]
        p = self.current_player
        # check col
        for i in range(3):
            if not m[x][i] == self.players[p]:
                break
            if i == 2:
                return "win"
        # check row
        for i in range(3):
            if not m[i][y] == self.players[p]:
                break
            if i == 2:
                return "win"
        # check diag and anti diag
        if x == y:
            for i in range(3):
                if not m[i][i] == self.players[p]:
                    break
                if i == 2:
                    return "win" 
            for i in range(3):
                if not m[i][2-i] == self.players[p]:
                    break
                if i == 2:
                    return "win"
        # check draw
        if self.move_count == 9:
            return "draw"
        
        return "go"
    
    def print_header(self):
        print "##########################"
        print "##      Tic-tac-toe     ##"
        print "##########################"

    def start_game(self, player):
        """ start game

        """
        self.current_player = player
        while True:
            self.print_board()  # Print the game board
            square = self.ask_input(self.current_player)  # Ask the current player to pick a square
            x = (square - 1) / 3  # Get square's x position
            y = (square - 1) % 3  # Get square's y position
            self.board[square-1] = self.players[self.current_player]  # Mark the square with player's mark symbol
            state = self.check_game_state(x, y)  # Get the game state
            if "win" == state:
                self.print_board()  # Print the final board
                print "Game over. Win for " + self.current_player
                break
            elif "draw" == state:
                self.print_board()  # Print the final board
                print "Game over. Draw for two players"
                break
            else:
                for key in self.players:
                    if self.current_player == key:
                        pass
                    else:
                        self.current_player = key
                        break

if __name__ == "__main__":
    tictactoe = Tictactoe()
    tictactoe.start_game('Foo')
