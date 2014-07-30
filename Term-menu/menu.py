#! /usr/bin/env python
# -*- coding: utf-8 -*-

import curses

def launch_menu():
    screen = curses.initscr()   # Initialize a new Windowobject which reprents the whole screen
    curses.noecho()             # Turn off the echo mode
    curses.curs_set(0)          # Leave cursor invisible
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)  # Initialize a color-pair with RED as fg and WHITE as bg
    screen.keypad(1)
    selection = -1
    option = 0
    #curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    while selection < 0:
        screen.clear()
        h = [0] * 5 # curses.A_NORMAL = 0
        h[option] = curses.color_pair(1)
        #h[option] = curses.A_REVERSE
        screen.addstr(2, 4, "Game Menu")
        screen.addstr(4, 4, "Please select an option...", curses.A_BOLD)
        screen.addstr(5, 4, "1 - Play Game", h[0])
        screen.addstr(6, 4, "2 - Instructions", h[1])
        screen.addstr(7, 4, "3 - Game Options", h[2])
        screen.addstr(8, 4, "4 - High Scores", h[3])
        screen.addstr(9, 4, "5 - Exit ('q')", h[4])
        screen.refresh()
        q = screen.getch()
        if q == curses.KEY_UP or q == ord('k'):      # KEY_UP or 'k' on vim mode
            option = (option - 1) % 5
        elif q == curses.KEY_DOWN or q == ord('j'):  # KEY_DOWN or 'j' on vim mode
            option = (option + 1) % 5
        elif q == ord('\n'):
            selection = option
        if q == ord('q') or selection == 4:  # If 'q' or select 'Exit', then quit
            break

    curses.endwin()

if __name__ == '__main__':
    launch_menu()
