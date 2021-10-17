"""
Author: Dương Trường Thọ
Date: 18/07/2021
Program: project_09_page_99.py
Problem:
    Write a program that receives a series of numbers from the user and allows the
    user to press the enter key to indicate that he or she is finished providing inputs.
    After the user presses the enter key, the program should print the sum of the
    numbers and their average.
Solution:
    
    ....
"""
data = input("Enter a number or press Enter to quit: ")
numbers = []

while True: 
    #request input from user
    data = input("Enter a number or press Enter to quit: ")

    #set up the termination condition    
    if data == "":
        break

    #convert inputs into floats
    numbers.append(float(data))

# these can all be done outside and after the while loop
count = len(numbers)
if count > 0:
    _sum = sum(numbers)
    product = 1.0
    for n in numbers:
        product *= n
    average = _sum / float(count)

    #display results
    print("The sum is", _sum)
    print("The product is", product)
    print("The average is", average)
else:
    print("Nothing was entered")

# Enter a number or press Enter to quit: 1
# Enter a number or press Enter to quit: 2
# Enter a number or press Enter to quit: 3
# Enter a number or press Enter to quit: 4
# Enter a number or press Enter to quit: 5
# Enter a number or press Enter to quit: 6
# Enter a number or press Enter to quit: 7
# Enter a number or press Enter to quit: 
# The sum is 27.0
# The product is 5040.0
# The average is 4.5