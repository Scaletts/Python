"""
Author: DuongTruongTho
Date: 03/08/2021
Program: Project_02_page132.py
Problem:
      Write a script that inputs a line of encrypted text and a distance value and outputs plaintext using a
        Caesar cipher. The script should work for any printable characters.


Solution:
    Display result
        Plain text:  IÀIB OCƠ
        Cipher text: NÀNG THƠ

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


message = ['IÀIB OCƠ']

for text in message:
    cipher = caesar_cipher(text, 'DECRYPT', 21)
    print('Plain text:  ' + text)
    print('Cipher text: ' + cipher + '\n')


