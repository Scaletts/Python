"""
Author: Dương Trường Thọ
Date: 18/07/2021
Program: project_06_page_99.py
Problem:
   The German mathematician Gottfried Leibniz developed the following method
    to approximate the value of π:
    π/4 =1 - 1/3 + 1/5 + 1/7 + . . .
    Write a program that allows the user to specify the number of iterations used in
    this approximation and that displays the resulting value.
Solution:
    
    ....
"""
iteration = int(input("Enter the number of iteration: "))
list01 = [] 
list02 = []
y = 1
for x in range(1, iteration+1):
        number = (1.0/y)
        list01.append(number)
        y += 2.0
        #print(number)
for i in range(1, iteration, 2):
        neg = list01[i]*-1.0
        list02.append(neg)
        #print(neg)
comb = (sum(list01)) + (sum(list02)) + (sum(list02))
pi = comb*4.0
print("The approximation of pi is", pi)

# Enter the number of iteration: 5
# The approximation of pi is 3.339682539682539