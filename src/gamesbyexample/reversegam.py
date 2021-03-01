"""Reversegam, by Al Sweigart al@inventwithpython.com
A tile flipping game, also called reversi.
More info https://en.wikipedia.org/wiki/Reversi
This and other games are available at https://nostarch.com/XX
Tags: large, board game, game, two-player"""
__version__ = 0
# A version of this game is featured in the book, "Invent Your Own
# Computer Games with Python" https://nostarch.com/inventwithpython

import copy, random, sys

COLS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
ROWS = ['1', '2', '3', '4', '5', '6', '7', '8']
ALL_DIRECTIONS = [[0, 1], [1, 1], [1, 0], [1, -1],
                  [0, -1], [-1, -1], [-1, 0], [-1, 1]]
HUMAN = 'X'
COMPUTER = 'O'

def main():
    print('Reversegam, by Al Sweigart al@inventwithpython.com')
    print('Place your tiles around your opponent\'s tiles to turn')
    print('them into your tiles. Try to get the most tiles. The game')
    print('ends when the board is full.')
    print()

    mainBoard = getNewBoard()  # Start a new board.
    isPlayersTurn = True
    while True:  # Main game loop.
        humanCantMove = getValidMoves(mainBoard, HUMAN) == []
        computerCantMove = getValidMoves(mainBoard, COMPUTER) == []
        if humanCantMove and computerCantMove:
            break  # Neither player can move, so quit.

        if isPlayersTurn and not humanCantMove:
            # Human player's turn:
            displayBoard(getBoardWithValidMoves(mainBoard, HUMAN))
            move = askForPlayerMove(mainBoard)
            if move == 'QUIT':
                print('Thanks for playing!')
                sys.exit()
            else:
                makeMove(mainBoard, HUMAN, move[0], move[1])
        elif not isPlayersTurn and not computerCantMove:

            displayBoard(mainBoard)
            print()
            input('Press Enter to see the computer\'s move.')
            x, y = getComputerMove(mainBoard)
            print('The computer moved on {}{}.'.format(COLS[x], ROWS[y]))
            print()
            makeMove(mainBoard, COMPUTER, x, y)

        isPlayersTurn = not isPlayersTurn

    # Display the final board and score.
    displayBoard(mainBoard)
    print('Good game!')


def getNewBoard():
    """Return a board data structure with the starting tiles."""
    board = {}
    for x in range(8):
        for y in range(8):
            board[(x, y)] = ' '

    # Place the two starting tiles for each player:
    board[(3, 3)] = 'X'
    board[(3, 4)] = 'O'
    board[(4, 3)] = 'O'
    board[(4, 4)] = 'X'
    return board


def getValidMoves(board, tile):
    """Returns a list of [x, y] lists of valid moves for the given
    player on the given board."""
    validMoves = []

    for x in range(8):
        for y in range(8):
            if isValidMove(board, tile, x, y) != False:
                validMoves.append([x, y])
    return validMoves


def isValidMove(board, tile, xstart, ystart):
    """Returns False if the player's move on xstart, ystart is invalid.
    If it is a valid move, returns a list of spaces that would become
    the player's if they made a move here."""
    if board[(xstart, ystart)] != ' ' or not isOnBoard(xstart, ystart):
        return False

    board[(xstart, ystart)] = tile  # Set the tile on the board.

    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'

    tilesToFlip = []
    for xdirection, ydirection in ALL_DIRECTIONS:
        x, y = xstart, ystart
        x += xdirection  # First step in the x direction.
        y += ydirection  # First step in the y direction.
        if isOnBoard(x, y) and board[(x, y)] == otherTile:
            # Find if the other player's tile next to our tile.
            x += xdirection
            y += ydirection
            if not isOnBoard(x, y):
                continue
            while board[(x, y)] == otherTile:
                x += xdirection
                y += ydirection
                # Break out of while loop, then continue in for loop:
                if not isOnBoard(x, y):
                    break
            if not isOnBoard(x, y):
                continue
            if board[(x, y)] == tile:
                # Found tiles to flip over. Go in reverse direction
                # until we reach the original space, noting all the
                # tiles along the way.
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([x, y])

    board[(xstart, ystart)] = ' '  # Restore the original empty space.
    # If no tiles were flipped, this is not a valid move:
    if len(tilesToFlip) == 0:
        return False
    return tilesToFlip


def isOnBoard(x, y):
    # Returns True if the coordinates are located on the board.
    return x >= 0 and x <= 7 and y >= 0 and y <= 7


def getBoardWithValidMoves(board, tile):
    """Returns a new board with . marking the possible moves."""
    duplicateBoard = copy.copy(board)

    for x, y in getValidMoves(duplicateBoard, tile):
        duplicateBoard[(x, y)] = '.'
    return duplicateBoard


def displayBoard(board):
    """Displays the board data structure passed to this function."""

    print('  ABCDEFGH')
    print(' +--------+')
    for y in range(8):
        print('{}|'.format((y + 1)), end='')  # Display the row number.
        for x in range(8):
            print(board[(x, y)], end='')  # Display the row.
        print('|{}'.format((y + 1)))  # Display the row number.
    print(' +--------+')
    print('  ABCDEFGH')

    # Prints out the current score.
    scores = getScoreOfBoard(board)
    print('X: {} points, O: {} points'.format(scores['X'], scores['O']))


def getScoreOfBoard(board):
    """Returns a dictionary with keys 'X' and 'O', whose values."""
    scores = {'X': 0, 'O': 0}  # The scores start at 0.
    # Loop over each space on the board:
    for x in range(8):
        for y in range(8):
            # Increment the score if there is an X or O on this space:
            if board[(x, y)] == 'X':
                scores['X'] += 1
            if board[(x, y)] == 'O':
                scores['O'] += 1
    return scores


def askForPlayerMove(board):
    """Let the player type in their move. Returns the move as [x, y]
    (or returns the string 'QUIT')"""
    while True:
        print('Enter your move, or type quit to end the game.')
        move = input('> ').upper()
        if move == 'QUIT':
            return 'QUIT'

        if len(move) == 2 and move[0] in COLS and move[1] in ROWS:
            x = 'ABCDEFGH'.find(move[0])
            y = int(move[1]) - 1
            if isValidMove(board, HUMAN, x, y) == False:
                print('That is not a valid space to place a tile.')
                continue
            else:
                break
        else:
            print('Type the column (A-H) and row (1-8).')
            print('For example, H1 will be the top-right corner.')

    return (x, y)


def makeMove(board, tile, xstart, ystart):
    """Place a tile on the board, flipping any of the opponent's pieces.
    Returns False for invalid moves, True for valid."""
    tilesToFlip = isValidMove(board, tile, xstart, ystart)

    if tilesToFlip == False:
        return False

    board[(xstart, ystart)] = tile
    for x, y in tilesToFlip:
        board[(x, y)] = tile
    return True


def getComputerMove(board):
    """Given a board and the computer's tile, determine where to move
    and return that move as a [x, y] list."""
    possibleMoves = getValidMoves(board, COMPUTER)

    # Randomize the order of the possible moves so that if there are
    # multiple best scoring moves, a random one is selected.
    random.shuffle(possibleMoves)

    # Always go for a corner if available:
    for x, y in possibleMoves:
        if isOnCorner(x, y):
            return (x, y)

    # Go through all possible moves and remember the best scoring move:
    bestScore = -1
    for x, y in possibleMoves:
        duplicateBoard = copy.copy(board)
        makeMove(duplicateBoard, COMPUTER, x, y)
        score = getScoreOfBoard(duplicateBoard)[COMPUTER]
        if score > bestScore:
            bestMove = [x, y]
            bestScore = score
    return bestMove


def isOnCorner(x, y):
    """Returns True if the position is in one of the four corners."""
    return ((x == 0 and y == 0) or (x == 7 and y == 0)
        or (x == 0 and y == 7) or (x == 7 and y == 7))


if __name__ == '__main__':
    main()
