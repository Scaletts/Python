"""
Author: Dương Trường Thọ
Date: 02/09/2021
Program: Exercise_02_page_199.py
Problem:

        Write the code for a filtering that generates a list of the positive numbers in a list named numbers.
        You should use a lambda to create the auxiliary function.

Solution:
        [8, 2, 12]

"""

def main():
    numbers = [8, -3, -5, 2, 12]
    print(list(filter(lambda x: x > 0, numbers)))


if __name__ == '__main__':
    main()