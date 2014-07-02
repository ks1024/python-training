#! /usr/bin/env python

import random

class HangmanGame:

    # hangman ascii graph list
    hangmans = [
    # step 0
    "\n\
    |---|\n\
        |\n\
        |\n\
        | Word: {0}\n\
  ______| Misses: {1}",
    # step 1
    "\n\
    |---|\n\
    o   |\n\
        |\n\
        | Word: {0}\n\
  ______| Misses: {1}",
    # step 2
    "\n\
    |---|\n\
    o   |\n\
    |   |\n\
        | Word: {0}\n\
  ______| Misses: {1}",
    # step 3
    "\n\
    |---|\n\
    o   |\n\
   /|   |\n\
        | Word: {0}\n\
  ______| Misses: {1}",
    # step 4
    "\n\
    |---|\n\
    o   |\n\
   /|\  |\n\
        | Word: {0}\n\
  ______| Misses: {1}",
    # step 5
    "\n\
    |---|\n\
    o   |\n\
   /|\  |\n\
   /    | Word: {0}\n\
  ______| Misses: {1}",
    # step 6
    "\n\
    |---|\n\
    o   |\n\
   /|\  |\n\
   / \  | Word: {0}\n\
  ______| Misses: {1}"]
    
    word_list = ['github', 'hangman', 'octopus', 'banana', 'python'] # words list
    misses = [] # empty list for misses
    word = None # randomly generated word
    word_checked = [] # word checked
    isGameOver = None # flag to test if the game is over
    step = None # step number for hangman ascii graph

    def __init__(self):
        """Initialize class variables"""
        self.isGameOver = False
        self.step = 0
        # generate a random word
        self.word = random.choice(self.word_list)
        # initialize the empty word the underscores
        self.word_checked = ['_' for i in range(len(self.word))]

    def findAllIndexes(self, s, c):
        """Find all indexes of a char in a string"""
        for i, item in enumerate(s):
            if item == c:
                yield i

    def printHangmanGraph(self):
        """Print hangman ascci graph"""
        print self.hangmans[self.step].format(' '.join(self.word_checked), ', '.join(self.misses))

    def isAlphaChar(self, c):
        """Check if an input is an alphabet"""
        if len(c) > 1 or not c.isalpha():
            print "Please input again, the valid char is a-z or A-Z"
            return False
        else:
            return True

    def startGame(self):
        while not self.isGameOver:
            # print hangman ascii graph
            self.printHangmanGraph()
            # ask to input a char
            s = raw_input('Guess: ').lower()
            if not self.isAlphaChar(s):
                continue
            elif s in self.word_checked or s in self.misses:
                print "You've inputed this char, try another one"
                continue

            # find indexes of a char in a word
            index_list = list(self.findAllIndexes(self.word, s))

            if not index_list:  # if index list is empty
                self.misses.append(s)
                self.step+=1
            else:               # if index list is not empty, we iterate the index list
                for i in index_list:
                    self.word_checked[i] = s

            if ''.join(self.word_checked) == self.word:
                self.isGameOver = True
                self.printHangmanGraph()
                print "YOU WIN"
            elif self.step == 6:
                self.isGameOver = True
                self.printHangmanGraph()
                print "YOU LOOSE"
                print "THE WORD IS", self.word
            else:
                pass

if __name__ == "__main__":
    hangmanGame = HangmanGame()
    hangmanGame.startGame()

