"""
Author: DuongTruongTho
Date: 02/09/2021
Program: Exersice_06_page_182.py
Problem:
       Explain what happens when the following recursive function is called with the
        values "hello" and 0 as arguments:
        def example(aString, index):
        if index < len(aString):
        example(aString, index + 1)
        print(aString[index], end = "")
Solution:
       reverse the order of hello
    
"""
def example(aString, index):
 if index < len(aString):
        example(aString, index + 1)
        print(aString[index], end = "")