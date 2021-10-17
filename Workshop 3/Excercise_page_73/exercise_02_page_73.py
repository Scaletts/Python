"""
Author: Dương Trường Thọ
Date: 18/07/2021
Program: exersice_02_page_73.py
Problem:
    Write a code segment that displays the values of the integers x, y, and z on a single
    line, such that each value is right-justified with a field width of 6.
Solution:
    x = int(input ("enter first number: "))
    y = int(input ("enter second number: "))
    z = int(input ("enter third number: "))
    print('%6d %6d %6d' %(x,y,z))
    ....
"""
x = int(input ("enter first number: "))
y = int(input ("enter second number: "))
z = int(input ("enter third number: "))
print('%6d %6d %6d' %(x,y,z))

# enter first number: 1
# enter second number: 2
# enter third number: 3
#      1      2      3