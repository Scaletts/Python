"""
Author: DuongTruongTho
Date: 03/08/2021
Program: Exersice_04_page_125.py
Problem:
     Write a code segment that prints the names of all of the items in the current working directory.


Solution:
    Display result:
        exercise_01_page_125.py
        exercise_02_page_125.py
        exercise_03_page_125.py
        exercise_04_page_125.py
        exercise_05_page_125.py

"""
import os

for listFile in os.listdir():
    print(listFile)

