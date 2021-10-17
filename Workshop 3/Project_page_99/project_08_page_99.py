"""
Author: Dương Trường Thọ
Date: 18/07/2021
Program: project_08_page_99.py
Problem:
    The greatest common divisor of two positive integers, A and B, is the largest
    number that can be evenly divided into both of them. Euclid’s algorithm can be
    used to find the greatest common divisor (GCD) of two positive integers. You
    can use this algorithm in the following manner:
    a. Compute the remainder of dividing the larger number by the smaller
    number.
    b. Replace the larger number with the smaller number and the smaller number
    with the remainder.
    c. Repeat this process until the smaller number is zero.
    The larger number at this point is the GCD of A and B. Write a program that lets
    the user enter two integers and then prints each step in the process of using the
    Euclidean algorithm to find their GCD
Solution:
    
    ....
"""
# Find the GCD of two positive numbers A & B
# Input a and b
a = int(input("Input the number a: "))
b = int(input("Input the number b: "))
while a | b < 0:
    print("Please input two positive integer numbers!")
    a = int(input("a: "))
    b = int(input("b: "))
# Save the current value of a & b for print the result conclusion ***
A = a
B = b

# Compute the remainder
print("Compute the remainder of dividing the larger number by the smaller number...")
remainder = a % b if a > b else b % a
print('Remainder of', a,'and',b,'is', remainder)

# Find the GCD
if remainder == 0 :
    gcd = b if a > b else a
    if a > b :
        print('Because',a,'is divisible by', b,'so:')
    else :
        print('Because',b,'is divisible by', a,'so:')
else :
    print('Replace the larger number with the smaller number and the smaller number with the remainder & Repeat this process until the smaller number is zero...')
    print('The larger number at this point is the GCD of A and B\n')
    print("*L(Larger number)\t*S(Smaller number)\t*R(Remainder)")
    print('L\tS\tR')
    print('Start...')
    print(a if a > b else b,'\t',b if a > b else a,'\t', a > b and a % b or b % a)
    print('Change...')
    print(b if a > b else a,'\t',remainder)
    while not remainder == 0:
        if a > b :
            a = b
            b = remainder
            remainder = a % b
            gcd = b
            print(a,'\t',b,'\t',remainder)
            print('Change...')
            print(b,'\t',remainder)
        else :
            b = a
            a = remainder
            remainder = b % a
            gcd = a
            print(b,'\t',a,'\t',remainder)
            print('Change...')
            print(a,'\t',remainder)
    print('The program stops when the S(Smaller number) = 0, at this point the larger number', gcd,'is the GCD of two number')
print('===============')
# result conclusion ***  
print('GCD OF NUMBER',A,'AND NUMBER',B, 'IS' , gcd)
