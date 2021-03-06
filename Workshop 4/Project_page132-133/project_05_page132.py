"""
Author: DuongTruongTho
Date: 03/08/2021
Program: Project_05_page132.py
Problem:
      A bit shift is a procedure whereby the bits in a bit string are moved to the left or to the right.
        For example, we can shift the bits in the string 1011 two places to the left to produce the string 1110.
        Note that the leftmost two bits are wrapped around to the right side of the string in this operation.
        Define two scripts, shiftLeft.py and shiftRight.py, that expect a bit string as an input. The script
        shiftLeft shifts the bits in its input one place to the left, wrapping the leftmost bit to the rightmost
        position. The script shiftRight performs the inverse operation. Each script prints the resulting string



Solution:
    Display result
        Enter a string of bits: 1100
        1001
        0110
"""

def shiftLeft(bitString):
    if len(bitString) > 1:
        bitString = bitString[1:] + bitString[0]
    return bitString

def shiftRight(bitString):
    if len(bitString) > 1:
        bitString = bitString[-1] + bitString[:-1]
    return bitString


# main
bitString = input("Enter a string of bits: ")
print(shiftLeft(bitString))
print(shiftRight(bitString))
