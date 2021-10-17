"""
Author: DuongTruongTho
Date: 02/09/2021
Program: Exersice_03_page_194.py
Problem:
       What is the lifetime of a variable? Give an example.
Solution:
       Lifetime defines how long the variable would be valid, i.e. Would be existent and can be used safely. 
       For ex all variables defined inside a function have a lifetime that spans within the body of that function, 
       and then exist from the time the function starts to execute and till the function finishes it execution. 
       These variables are allocated memory on stack, the stack unwinds on return from a function and hence these variables are destroyed at that time
    
"""
def func1():
    x='Local_x'
    print(x)
func1() 