"""
Author: DuongTruongTho
Date: 03/08/2021
Program: Exersice_01_page_118.py
Problem:
    1.  Assume that the variable data refers to the string "Python rules!". Use a string method from Table 4-2
        to perform the following tasks:
        a.  Obtain a list of the words in the string.
        b.  Convert the string to uppercase.
        c.  Locate the position of the string "rules".
        d.  Replace the exclamation point with a question mark.

* * * * * ============================================================================================= * * * * *

Solution:
    Display result:
        a. ['P', 'y', 't', 'h', 'o', 'n', ' ', 'r', 'u', 'l', 'e', 's', '!']
        b. PYTHON RULES!
        c. 7
        d. Python rules?

"""

data = 'Python rules!'

print('a.', list(data))
print('b.', data.upper())
print('c.', data.index('rules'))
print('d.', data.replace('!', '?'))
