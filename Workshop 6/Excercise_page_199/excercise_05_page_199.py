"""
Author: Duong Truong Tho
Date: 02/09/2021
Program: Exercise_05_page_199.py
Problem:

        Three versions of the summation function have been presented in this chapter. One uses a loop, one uses
        recursion, and one uses the reduce function. Discuss the costs and benefits of each version, in terms of
        programmer time and computational resources required.

Solution:
    <function sum_digits at 0x0000020E7BE8DF70>
"""
def sum_digits(n):
	    if n < 10:
	        return n
	    else:
	        all_but_last, last = n // 10, n % 10
	        return sum_digits(all_but_last) + last
	
sum_digits(738)
print(sum_digits)

