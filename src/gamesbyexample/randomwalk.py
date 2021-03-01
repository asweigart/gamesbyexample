"""Random Walk, by Al Sweigart al@inventwithpython.com
Generate splatter-art with the "random walk" algorithm.
Press Ctrl-C to stop.
More info at: https://en.wikipedia.org/wiki/Random_walk
This and other games are available at https://nostarch.com/XX
Tags: short, artistic, bext, terminal"""
__version__ = 0
import random, time, sys

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

BLOCK = chr(9608)

print('Random Walk, by Al Sweigart al@inventwithpython.com')

# Ask user what speed to run the simulation at:
while True:  # Keep looping until the user enters F or S.
    print('Move (F)ast or (S)low?')
    speed = input('> ').upper()
    if speed == 'F' or speed == 'S':
        break

width, height = bext.size()
bext.clear()

try:
    while True:  # Main program loop.
        bext.fg('random')  # Set to a random color.
        # Start in the middle of the screen:
        x, y = width // 2, height // 2

        # Display quit instructions:
        bext.goto(0, height - 2)
        print('Press Ctrl-C to quit.', end='')

        while (0 <= x < width) and (0 <= y < height):
            # Print the block at it's current location:
            bext.goto(x, y)
            print(BLOCK, end='', flush=True)

            # Move the block:
            direction = random.randint(0, 3)
            if direction == 0:
                x += 1
            elif direction == 1:
                x -= 1
            elif direction == 2:
                y += 1
            elif direction == 3:
                y -= 1

            if speed == 'S':
                time.sleep(0.01)
        time.sleep(0.5)  # Pause after reaching the edge.
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.
