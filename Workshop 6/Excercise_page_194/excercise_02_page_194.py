"""
Author: DuongTruongTho
Date: 02/09/2021
Program: Exersice_02_page_194.py
Problem:
       What is the scope of a variable? Give an example.
Solution:
       Scope refers to the visibility of variables. In other words, which parts of your program can see or use it. 
       Normally, every variable has a global scope. Once defined, every part of your program can access a variable.
    
"""
def print_number():
    first_num = 1
    # Print statement 1
    print("The first number defined is: ", first_num)

    print_number()
    # Print statement 2
    print("The first number defined is: ", first_num)