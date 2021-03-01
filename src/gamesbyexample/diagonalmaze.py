"""Diagonal Maze, by Al Sweigart al@inventwithpython.com
Prints out a random, diagonal maze. (It is not a true
maze, but rather an artistic maze-like picture.)
Inspired by the "10 PRINT CHR$(205.5+RND(1)); : GOTO 10" program.
This and other games are available at https://nostarch.com/XX
Tags: tiny, beginner, artistic, maze"""
__version__ = 0
import random

FORWARD_SLASH = chr(9585) # The ╱ character.
BACK_SLASH    = chr(9586) # The ╲ character.
# (A list of chr() codes is at https://inventwithpython.com/charactermap)

for x in range(2000):  # Loop for each slash in the current line.
    # Randomly add a forward or back slash to the line.
    if random.randint(0, 1) == 0:
        print(FORWARD_SLASH, end='')
    else:
        print(BACK_SLASH, end='')
