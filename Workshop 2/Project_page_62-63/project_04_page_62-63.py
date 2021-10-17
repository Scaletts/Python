"""
Author: Dương Trường Thọ
Date: 11/07/2021
Program: project_04_page_62-63.py
Problem:
    
    Write a program that takes the radius of a sphere (a floating-point number) as
    input and then outputs the sphere’s diameter, circumference, surface area, and
    volume.
    
Solution:
    ....
"""


# Write a program that takes the radius of a sphere (a floating-point number) as input and then outputs the sphere’s diameter, circumference, surface area, and volume.
import math
radius = float(input("Radius = "))
diameter = radius * 2
circumference = diameter * math.pi
surfaceArea = 4 *math.pi *radius * radius
volume = 4/3 *math.pi *radius *radius *radius
print("Diameter: ", diameter)
print("Circumference: ", circumference)
print("Surface area : ", surfaceArea)
print("Volume ", volume)
#Radius = 5
#Diameter:  10.0
#Circumference:  31.41592653589793
#Surface area :  314.1592653589793
#Volume  523.5987755982989

