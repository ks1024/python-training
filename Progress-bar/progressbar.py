#! /usr/bin/env python

#---------------------------------
# Text progress bar in terminal
# @author: kyan
# @version: 1.0.0
#---------------------------------

import sys
import time

class ProgressBar:

    def __init__(self, maxval, bar_length=20):
        self.maxval = maxval
        self.bar_length = bar_length

    def start(self, sleep_time):
        for i in xrange(0, self.maxval + 1):
            percent = float(i) / self.maxval
            hashes = '#' * int(round(percent * self.bar_length))
            spaces = ' ' * (self.bar_length - len(hashes))
            time.sleep(sleep_time)
            sys.stdout.write("\rRunning: [{0}] {1}%".format(hashes + spaces, int(round(percent * 100))))
            sys.stdout.flush()
        print "\n"

if __name__ == "__main__":
    # example program
    progressBar = ProgressBar(100, 30)
    progressBar.start(0.5)
