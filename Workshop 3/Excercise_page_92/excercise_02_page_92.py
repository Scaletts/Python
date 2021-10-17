"""
Author: Dương Trường Thọ
Date: 18/07/2021
Program: exersice_02_page_92.py
Problem:
   The factorial of an integer N is the product of the integers between 1 and N, inclusive. 
   Write a while loop that computes the factorial of a given integer N.
Solution:
    number = int(input("Enter number:"))
    factorial = 1
    while number>0:
        factorial = factorial * number
        number = number - 1
    print(factorial)
    ....
"""
number = int(input("Enter number:"))
factorial = 1
while number>0:
    factorial = factorial * number
    number = number - 1
print(factorial)

# Enter number:4
# 24