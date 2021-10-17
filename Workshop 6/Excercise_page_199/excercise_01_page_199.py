"""
Author: Dương Trường Thọ
Date: 02/09/2021
Program: Exercise_01_page_199.py
Problem:

        Write the code for a mapping that generates a list of the absolute values of the numbers in a list
        named numbers.
Solution:
        [5, 7, 17, 5, 76]

"""

def main():
    numbers = [5, 7, -17, -5, -76]
    print(list(map(abs, numbers)))


if __name__ == '__main__':
    main()