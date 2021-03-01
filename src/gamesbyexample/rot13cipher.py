"""ROT13 Cipher, by Al Sweigart al@inventwithpython.com
The simplest shift cipher for encrypting and decrypting text.
More info at https://en.wikipedia.org/wiki/ROT13
This and other games are available at https://nostarch.com/XX
Tags: tiny, cryptography"""
__version__ = 0
try:
    import pyperclip  # pyperclip copies text to the clipboard.
except ImportError:
    pass  # If pyperclip is not installed, do nothing. It's no big deal.

# Set up the constants:
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'

print('ROT13 Cipher, by Al Sweigart al@inventwithpython.com')
print()

while True:  # Main program loop.
    print('Enter a message to encrypt/decrypt (or QUIT):')
    message = input('> ')

    if message.upper() == 'QUIT':
        break  # Break out of the main program loop.

    # Rotate the letters in message by 13 characters.
    translated = ''
    for character in message:
        if character.isupper():
            # Concatenate uppercase translated character.
            transCharIndex = (UPPER_LETTERS.find(character) + 13) % 26
            translated += UPPER_LETTERS[transCharIndex]
        elif character.islower():
            # Concatenate lowercase translated character.
            transCharIndex = (LOWER_LETTERS.find(character) + 13) % 26
            translated += LOWER_LETTERS[transCharIndex]
        else:
            # Concatenate the character untranslated.
            translated += character

    # Display the translation:
    print('The translated message is:')
    print(translated)
    print()

    try:
        # Copy the translation to the clipboard:
        pyperclip.copy(translated)
        print('(Copied to clipboard.)')
    except:
        pass
