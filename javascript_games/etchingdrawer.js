/*Etching Drawer, by Al Sweigart al@inventwithpython.com
An art program that draws a continuous line around the screen using the
WASD keys. Inspired by Etch A Sketch toys.

For example, you can draw Hilbert Curve fractal with:
SDWDDSASDSAAWASSDSASSDWDSDWWAWDDDSASSDWDSDWWAWDWWASAAWDWAWDDSDW

Or an even larger Hilbert Curve fractal with:
DDSAASSDDWDDSDDWWAAWDDDDSDDWDDDDSAASDDSAAAAWAASSSDDWDDDDSAASDDSAAAAWA
ASAAAAWDDWWAASAAWAASSDDSAASSDDWDDDDSAASDDSAAAAWAASSDDSAASSDDWDDSDDWWA
AWDDDDDDSAASSDDWDDSDDWWAAWDDWWAASAAAAWDDWAAWDDDDSDDWDDSDDWDDDDSAASDDS
AAAAWAASSDDSAASSDDWDDSDDWWAAWDDDDDDSAASSDDWDDSDDWWAAWDDWWAASAAAAWDDWA
AWDDDDSDDWWAAWDDWWAASAAWAASSDDSAAAAWAASAAAAWDDWAAWDDDDSDDWWWAASAAAAWD
DWAAWDDDDSDDWDDDDSAASSDDWDDSDDWWAAWDD

This and other games are available at https://nostarch.com/XX
Tags: large, artistic*/

'use strict';

// Set up the constants for line characters:
UP_DOWN_CHAR         = String.fromCharCode(9474);  // Character 9474 is '│'
LEFT_RIGHT_CHAR      = String.fromCharCode(9472);  // Character 9472 is '─'
DOWN_RIGHT_CHAR      = String.fromCharCode(9484);  // Character 9484 is '┌'
DOWN_LEFT_CHAR       = String.fromCharCode(9488);  // Character 9488 is '┐'
UP_RIGHT_CHAR        = String.fromCharCode(9492);  // Character 9492 is '└'
UP_LEFT_CHAR         = String.fromCharCode(9496);  // Character 9496 is '┘'
UP_DOWN_RIGHT_CHAR   = String.fromCharCode(9500);  // Character 9500 is '├'
UP_DOWN_LEFT_CHAR    = String.fromCharCode(9508);  // Character 9508 is '┤'
DOWN_LEFT_RIGHT_CHAR = String.fromCharCode(9516);  // Character 9516 is '┬'
UP_LEFT_RIGHT_CHAR   = String.fromCharCode(9524);  // Character 9524 is '┴'
CROSS_CHAR           = String.fromCharCode(9532);  // Character 9532 is '┼'
// A list of String.fromCharCode() codes is at https://inventwithpython.com/chr

// Get the size of the terminal window:
// We can't print to the last column on Windows without it adding a
// newline automatically, so reduce the width by one:
const WIDTH = process.stdout.columns - 1;
const HEIGHT = process.stdout.rows - 5;

/* The keys for canvas will be (x, y) integer tuples for the coordinate,
and the value is a set of letters W, A, S, D that tell what kind of line
should be drawn.*/
let canvas = {};
let cursorX = 0;
let cursorY = 0;

function getCanvasString(canvasData, cx, cy) {
    // Returns a multiline string of the line drawn in canvasData.
    let canvasStr = '';

    /* canvasData is a dictionary with (x, y) tuple keys and values that
    are sets of 'W', 'A', 'S', and/or 'D' strings to show which
    directions the lines are drawn at each xy point.*/
    for (let rowNum = 0; rowNum < CANVAS_HEIGHT; rowNum++) {
        for (let columnNum = 0; columnNum < CANVAS_HEIGHT; columnNum++) {
            if (columnNum == cx && rowNum == cy) {
                canvasStr += '#';
                continue;
            }

            // Add the line character for this point to canvasStr.

        }
    }
}