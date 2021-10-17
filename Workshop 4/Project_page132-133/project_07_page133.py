"""
Author: DuongTruongTho
Date: 03/08/2021
Program: Project_07_page133.py
Problem:
     Write a script that decrypts a message coded by the method used in Project 6



Solution:
    Display result
        Enter a message: 1101011 1010011 1100001
        tho
"""

def binaryToDecimal(text):
    if len(text) > 1:
        text = text[-1] + text[:-1]
    decimal = 0
    exponent = len(text) - 1
    for digit in text:
        decimal = decimal + int(digit) * 2 ** exponent
        exponent = exponent - 1
    return decimal


# main
Text = input("Enter a message: ")

bitString = Text.split()
textString = ''
for text in bitString:
    textString += chr(binaryToDecimal(text)-1)

print(textString)
