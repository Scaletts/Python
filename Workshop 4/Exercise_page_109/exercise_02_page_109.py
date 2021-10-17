"""
Author: DuongTruongTho
Date: 03/08/2021
Program: Exersice_02_page_109.py
Problem:
      Consult the Table of ASCII values in Chapter 2 and suggest how you would modify the encryption and
        decryption scripts in this section to work with strings containing all of the printable characters.


Solution:
    Display result:

        Plain text:  python
        Cipher text: èñìàçæ

        Plain text:  hacker
        Cipher text: àÙÛãÝê

        Plain text:  wow
        Cipher text: ïçï

"""

def caesar_cipher(message, mode, key):
    translated = ''

    for symbol in message:
        num = ord(symbol)
        if mode.upper() == 'ENCRYPT':
            num = (num + key) % 256
        elif mode.upper() == 'DECRYPT':
            num = (num - key) % 256
        translated += chr(num)

    return translated


message = ['python', 'hacker', 'wow']

for text in message:
    cipher = caesar_cipher(text, 'ENCRYPT', 120)
    print('Plain text:  ' + text)
    print('Cipher text: ' + cipher + '\n')

