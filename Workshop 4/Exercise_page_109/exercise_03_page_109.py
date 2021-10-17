"""
Author: DuongTruongTho
Date: 03/08/2021
Program: Exersice_03_page_109.py
Problem:
     You are given a string that was encoded by a Caesar cipher with an unknown distance value. The text can
        contain any of the printable ASCII characters. Suggest an algorithm for cracking this code.


Solution:
    Display result:

        Plain text:  èñìàçæ
        Cipher text: python

        Plain text:  àÙÛãÝê
        Cipher text: hacker

        Plain text:  ïçï
        Cipher text: wow

"""

def caesar_cipher(message, mode, key):
    translated = ''

    for symbol in message:
        num = ord(symbol)
        if mode.upper() == 'ENCRYPT':
            num = (num + key) % 256
        elif mode.upper() == 'DECRYPT':
            num = (num - key) % 256
        #     or
        #     if num >= 256:
        #         num = 256 + num - key
        #     elif num < 256:
        #         num -= key
        translated += chr(num)
    return translated


message = ['èñìàçæ', 'àÙÛãÝê', 'ïçï']

for text in message:
    cipher = caesar_cipher(text, 'DECRYPT', 120)
    print('Plain text:  ' + text)
    print('Cipher text: ' + cipher + '\n')

