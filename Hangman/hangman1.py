#! /usr/bin/env python

import random

def findAllIndex(s, c):
    """Find all indexes of a char in a string.
    Args:
      s(str): The string 
      c(char): The char to find in the string s
    """
    for i, item in enumerate(s):
        if item == c:
            yield i

def printHangman(h, s, w, m):
    """Print hangman ascii grahp
    Args:
      h(list): a list of hangman ascii graph
      s(int): step of hangman
      w(list): a list to store checked chars
      m(list): a list to store misses
    """
    print h[s].format(' '.join(w), ', '.join(m))

def isAlphaChar(c):
    """Test if an input is an alphabet
    Args:
      c(char): an inputed char
    Returns:
        True: if an alphabet
        False: if not
    """
    if len(c) > 1 or not c.isalpha():
        print "Please input again, the valid char is a-z or A-Z"
        return False
    else:
        return True

def main():

    # hangman ascii graph
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

    # words list
    word_list = ['github', 'hangman', 'octopus', 'banana', 'python'] # to complete the word list
    # empty list for misses 
    misses = []
    # generate a random word
    word = random.choice(word_list)
    # initialize the empty word with underscore
    word_checked = ['_' for i in range(len(word))]
    isFinished = False
    step = 0

    while not isFinished:
        # print hangman ascii graph
        printHangman(hangmans, step, word_checked, misses)   
        # ask to input a char
        s = raw_input('Guess: ').lower()
        if not isAlphaChar(s):
            continue
        elif s in word_checked or s in misses:
            print "You've inputed this char, try another one"
            continue
        # find indexes of a char in a word
        index_list = list(findAllIndex(word, s))
    
        if not index_list:  # if index list is empty
            misses.append(s)
            step+=1
        else:               # if index list is not empty, we iterate the index list
            for i in index_list:
                word_checked[i] = s
    
        if ''.join(word_checked) == word:
            isFinished = True
            printHangman(hangmans, step, word_checked, misses)
            print "YOU WIN!"
        elif step == 6:
            isFinished = True
            printHangman(hangmans, step, word_checked, misses)
            print "YOU LOOSE!"
            print "THE WORD IS", word
        else:
            pass

if __name__ == "__main__":
    main()
