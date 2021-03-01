"""Maze Maker, by Al Sweigart al@inventwithpython.com
Make mazes with the recursive backtracker algorithm.

An animated demo: https://scratch.mit.edu/projects/17358777/
This and other games are available at https://nostarch.com/XX
Tags: large, maze"""
__version__ = 0
import random

# Set up the constants:
WALL = '#'
EMPTY = ' '
START = 'S'
EXIT = 'E'
BLOCK = chr(9617)  # Character 9617 is '░'

NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'


def displayMaze(maze, travelerX=None, travelerY=None):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if maze[(x, y)] == WALL:
                print(BLOCK, end='')
            elif travelerX == x and travelerY == y:
                print('@', end='')
            else:
                print(maze[(x, y)], end='')
        print()  # Print a newline after printing the row.


def saveMaze(maze, filename):
    mazeFile = open(filename, 'w')
    for y in range(HEIGHT):
        for x in range(WIDTH):
            mazeFile.write(maze[(x, y)])
        mazeFile.write('\n')
    mazeFile.close()


print('''Maze Maker (Recursive Backtracker algorithm)
By Al Sweigart al@inventwithpython.com

This program creates maze files. You can play these mazes with
mazerunner.py or maze3d.py''')

while True:
    response = input('Enter width (must be odd and greater than 2): ')
    if response.isdecimal():
        WIDTH = int(response)
        if WIDTH % 2 == 1 and WIDTH > 2:
            break
while True:
    response = input('Enter height (must be odd and greater than 2): ')
    if response.isdecimal():
        HEIGHT = int(response)
        if HEIGHT % 2 == 1 and HEIGHT > 2:
            break
while True:
    response = input('Enter seed (must be a positive integer): ')
    if response.isdecimal():
        SEED = int(response)
        break


random.seed(SEED)

response = input('Watch maze generation step by step? (y/n): ')
watchGeneration = response.upper().startswith('Y')


# Create the filled-in maze to start:
maze = {}
for x in range(WIDTH):
    for y in range(HEIGHT):
        maze[(x, y)] = WALL

# Create the maze:
print('Generating maze...')
pathFromStart = [(1, 1)]
hasVisited = [(1, 1)]

while len(pathFromStart) > 0:
    x, y = pathFromStart[-1]
    maze[(x, y)] = EMPTY

    # Display the maze so far:
    if watchGeneration:
        displayMaze(maze, x, y)
        # (!) Uncomment this next line to see how pathFromStart grows
        # and shrinks while the algorithm runs.
        #print('pathFromStart =', pathFromStart)
        print('Press Enter to continue...')
        input()
        print('\n' * 60)  # Clear the screen by printing newlines.

    unvisitedNeighbors = []
    # Check the north neighbor:
    if y > 1 and (x, y - 2) not in hasVisited:
        unvisitedNeighbors.append(NORTH)
    # Check the south neighbor:
    if y < HEIGHT - 2 and (x, y + 2) not in hasVisited:
        unvisitedNeighbors.append(SOUTH)
    # Check the west neighbor:
    if x > 1 and (x - 2, y) not in hasVisited:
        unvisitedNeighbors.append(WEST)
    # Check the east neighbor:
    if x < WIDTH - 2 and (x + 2, y) not in hasVisited:
        unvisitedNeighbors.append(EAST)

    if len(unvisitedNeighbors) > 0:
        nextIntersection = random.choice(unvisitedNeighbors)
        if nextIntersection == NORTH:
            pathFromStart.append((x, y - 2))
            hasVisited.append((x, y - 2))
            maze[(x, y - 1)] = EMPTY
        elif nextIntersection == SOUTH:
            pathFromStart.append((x, y + 2))
            hasVisited.append((x, y + 2))
            maze[(x, y + 1)] = EMPTY
        elif nextIntersection == WEST:
            pathFromStart.append((x - 2, y))
            hasVisited.append((x - 2, y))
            maze[(x - 1, y)] = EMPTY
        elif nextIntersection == EAST:
            pathFromStart.append((x + 2, y))
            hasVisited.append((x + 2, y))
            maze[(x + 1, y)] = EMPTY
    else:
        pathFromStart.pop()

# Add the start and end positions:
maze[(1, 1)] = START
maze[(WIDTH - 2, HEIGHT - 2)] = EXIT

# Display the maze and save it to a text file.
displayMaze(maze)
filename = 'maze{}x{}s{}.txt'.format(WIDTH, HEIGHT, SEED)
saveMaze(maze, filename)

print('Saved to {}.'.format(filename))
