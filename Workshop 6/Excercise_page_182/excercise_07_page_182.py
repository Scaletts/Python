"""
Author: DuongTruongTho
Date: 02/09/2021
Program: Exersice_07_page_182.py
Problem:
       Explain what happens when the following recursive function is called with the
        values "hello" and 0 as arguments:
        def example(aString, index):
        if index == len(aString):
        return ""
        else:
        return aString[index] + example(aString, index + 1)
Solution:
       Function is called with the values “hello” and 0 as arguments:

        example(hello, 0)

        The base condition 

        index == len(aString) is false since the value of len(hello) is 5 and the value of  index is 0
        Therefore, the else part will be execute and return the concatenation of character at index 0 of hello (i.e. 'h' )...
    
"""