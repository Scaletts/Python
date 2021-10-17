"""
Author: DuongTruongTho
Date: 03/08/2021
Program: Exersice_01_page_109.py
Problem:
      Write the encrypted text of each of the following words using a Caesar cipher with
        a distance value of 3:

        a.  python
        b.  hacker
        c.  wow


Solution:
    Display result:

        Plain text:  python
        Cipher text: KTOCJI

        Plain text:  hacker
        Cipher text: CVXFZM

        Plain text:  wow
        Cipher text: RJR

"""

def caesar_cipher(message, mode, key):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    message = message.upper()
    translated = ''

    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            if mode.upper() == 'ENCRYPT':
                num = (num + key) % 26
            elif mode.upper() == 'DECRYPT':
                num = (num - key) % 26
            translated += LETTERS[num]
        else:
            translated += symbol

    return translated


message = ['python', 'hacker', 'wow']

for text in message:
    cipher = caesar_cipher(text, 'ENCRYPT', 21)
    print('Plain text:  ' + text)
    print('Cipher text: ' + cipher + '\n')
