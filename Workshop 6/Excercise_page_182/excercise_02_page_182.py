"""
Author: DuongTruongTho
Date: 02/09/2021
Program: Exersice_02_page_182.py
Problem:
        The factorial of a positive integer n, fact(n), is defined recursively as follows:
            fact( ) n 1 5 , when n 1 5
            fact( ) n n 5 2 * fact n ( ) 1 , otherwise
        Define a recursive function fact that returns the factorial of a given positive integer
Solution:
        6
        24
        120
        720
            
"""
def fact(n):
   if n == 1 or n==0:
       return 1
   else :
       return n*fact(n-1)

print(fact(3))
print(fact(4))
print(fact(5))
print(fact(6))