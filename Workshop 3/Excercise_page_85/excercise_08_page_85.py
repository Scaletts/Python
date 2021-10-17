"""
Author: Dương Trường Thọ
Date: 18/07/2021
Program: exersice_08_page_85.py
Problem:
   The variables x and y refer to numbers. Write a code segment that prompts the user for
   an arithmetic operator and prints the value obtained by applying that operator to x and y.
Solution:
    x = int(input("Enter the value of x: "))
    y = int(input("Enter the value of y: "))
    op = input("Enter an arithmetic operator : ")
    operation = 0
    if op == '+':
     operation = x + y
    elif op == '-':
     operation = x - y
    elif op == '*':
     operation = x * y
    elif op == '/':
     operation = x / y
    elif op == '%':
     operation = x % y
    else:
    print("Invalid Character!")
    print(x, op , y, "=", operation)
    ....
"""
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
op = input("Enter an arithmetic operator : ")
operation = 0
if op == '+':
 operation = x + y
elif op == '-':
 operation = x - y
elif op == '*':
 operation = x * y
elif op == '/':
 operation = x / y
elif op == '%':
 operation = x % y
else:
 print("Invalid Character!")
print(x, op , y, "=", operation)

# Enter the value of x: 5
# Enter the value of y: 5
# Enter an arithmetic operator : 5
# Invalid Character!
# 5 5 5 = 0