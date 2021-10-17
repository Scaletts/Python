"""
Author: Dương Trường Thọ
Date: 18/07/2021
Program: project_05_page_99.py
Problem:
    A local biologist needs a program to predict population growth. The inputs
    would be the initial number of organisms, the rate of growth (a real number
    greater than 0), the number of hours it takes to achieve this rate, and a number
    of hours during which the population grows. For example, one might start with a
    population of 500 organisms, a growth rate of 2, and a growth period to achieve
    this rate of 6 hours. Assuming that none of the organisms die, this would imply
    that this population would double in size every 6 hours. Thus, after allowing
    6 hours for growth, we would have 1000 organisms, and after 12 hours, we would
    have 2000 organisms. Write a program that takes these inputs and displays a prediction of the total population.
Solution:
    
    ....
"""
organisms = int(input("Enter the initial number of organisms:"))
rateOfGrowth = int(input("Enter the rate of growth : "))
numOfhours = int(input("Enter the number of hours to achieve the rate of growth: "))
totalhours = int(input("Enter the total hours of growth: "))
hours=0
while (hours <= totalhours):
    organisms*=rateOfGrowth
    hours += numOfhours
    if (hours==totalhours):
        break
print("The total population:" ,organisms)

# Enter the initial number of organisms:1000
# Enter the rate of growth : 2
# Enter the number of hours to achieve the rate of growth: 6
# Enter the total hours of growth: 12
# The total population: 4000