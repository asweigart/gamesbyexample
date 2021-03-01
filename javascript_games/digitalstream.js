/*
Digital Rain, by Al Sweigart al@inventwithpython.com
A screensaver in the style of The Matrix movie's "digital rain" visuals.
*/

'use strict';

function sleep(seconds) {
  return new Promise(resolve => setTimeout(resolve, seconds * 1000));
}

async function main() {
    // Set up the constants:
    const MIN_STREAM_LENGTH = 6;  // (!) Try changing this to 1 or 50.
    const MAX_STREAM_LENGTH = 14;  // (!) Try changing this to 100.
    const PAUSE = 0.1;  // (!) Try changing this to 0.0 or 2.0.
    const STREAM_CHARS = ['0', '1'];  // (!) Try changing this to other characters.

    // Density can range from 0.0 to 1.0:
    const DENSITY = 0.02;  // (!) Try changing this to 0.10 or 030.

    // Get the size of the terminal window:
    // (We can't print to the last column on Windows without it adding a
    // newline automatically, so reduce the width by one.)
    const WIDTH = process.stdout.columns - 1;

    console.log('Digital Rain Screensaver, by Al Sweigart al@inventwithpython.com');
    console.log('Press Ctrl-C to quit.');
    await sleep(2);

    // When the counter is 0, no bead of "digital rain" is shown.
    // Otherwise, it acts as a counter for how many times a 1 or 0
    // should be displayed in that column.
    let columns = [];
    for (let i = 0; i < WIDTH; i++) {
        columns.push(0);
    }
    while (true) {
        // Set up the counter for each column:
        for (let i = 0; i < WIDTH; i++) {
            if (columns[i] == 0) {
                if (Math.random() < DENSITY) {
                    // Restart a stream on this column.
                    columns[i] = Math.floor(Math.random() * (MAX_STREAM_LENGTH - MIN_STREAM_LENGTH)) + MIN_STREAM_LENGTH;
                }
            }

            // Display an empty space or a 1/0 character.
            if (columns[i] > 0) {
                process.stdout.write(STREAM_CHARS[Math.floor(Math.random() * STREAM_CHARS.length)]);
                columns[i] -= 1;
            } else {
                process.stdout.write(' ');
            }
        }
        console.log();  // Print a newline at the end of the row of columns.
        await sleep(PAUSE);
    }
}

main();
