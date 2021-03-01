"""Zigzag, by Al Sweigart al@inventwithpython.com
A simple zig zag animation. Press Ctrl-C to stop.
This and other games are available at https://nostarch.com/XX
Tags: tiny, beginner, artistic, scrolling"""
__version__ = 0
import sys, time

print('Zigzag, by Al Sweigart al@inventwithpython.com')
print('Press Ctrl-C to quit.')
time.sleep(3)

indentSize = 0  # How many spaces to indent.

try:
    while True:  # The main program loop.
        # Zig to the right 20 times:
        for i in range(20):
            indentSize = indentSize + 1
            indentation = ' ' * indentSize
            print(' ' * indentSize + '********')
            time.sleep(0.05)  # Pause for 50 milliseconds.

        # Zag to the left 20 times:
        for i in range(20):
            indentSize = indentSize - 1
            indentation = ' ' * indentSize
            print(indentation + '********')
            time.sleep(0.05)  # Pause for 50 milliseconds.
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.
