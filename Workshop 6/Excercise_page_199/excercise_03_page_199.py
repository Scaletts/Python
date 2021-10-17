"""
Author: Duong Truong Tho
Date: 02/09/2021
Program: Exercise_03_page_199.py
Problem:

        Write the code for a reducing that creates a single string from a list of strings named words.

Solution:
        I LOVE YOU

"""

from functools import reduce


def main():
    words = ["I", "LOVE", "YOU"]
    print(reduce(lambda x, y: x + " " + y, words))


if __name__ == '__main__':
    main()