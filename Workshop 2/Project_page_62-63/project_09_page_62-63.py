"""
Author: Dương Trường Thọ
Date: 11/07/2021
Program: project_09_page_62-63.py
Problem:
    
    Write a program that takes as input a number of kilometers and prints the corresponding number of nautical miles. Use the following approximations:
    • A kilometer represents 1/10,000 of the distance between the North Pole and
    the equator.
    • There are 90 degrees, containing 60 minutes of arc each, between the North
    Pole and the equator.
    • A nautical mile is 1 minute of an arc.
    
Solution:
    ....
"""


# Write a program that takes as input a number of kilometers and prints the corresponding number of nautical miles. Use the following approximations:
    # • A kilometer represents 1/10,000 of the distance between the North Pole and
    # the equator.
    # • There are 90 degrees, containing 60 minutes of arc each, between the North
    # Pole and the equator.
    # • A nautical mile is 1 minute of an arc.
Kilometers=int(input("Enter the amount of kilometers:"))
degreesPerMin = 90*60
onekilo = degreesPerMin/10000
nauticalmile = onekilo*Kilometers
print (Kilometers,"is",nauticalmile,"Nautical miles")
#Enter the amount of kilometers:200
# 200 is 108.0 Nautical miles

