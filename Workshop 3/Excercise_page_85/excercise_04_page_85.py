"""
Author: Dương Trường Thọ
Date: 18/07/2021
Program: exersice_04_page_85.py
Problem:
    Assume that the variables x and y refer to strings. Write a code segment that prints
    these strings in alphabetical order. You should assume that they are not equal.
Solution:
    # To take input from the user
    my_str = input("Enter a string:" )
    # breakdown the string into a list of words
    words = [word.lower() for word in my_str.split()]
    # sort the list
    words.sort()
    # display the sorted words
    print("The sorted words are:")
    for word in words:
    print(word)
    ....
"""
# To take input from the user
my_str = input("Enter a string:" )
# breakdown the string into a list of words
words = [word.lower() for word in my_str.split()]
# sort the list
words.sort()
# display the sorted words
print("The sorted words are:")
for word in words:
   print(word)

# Enter a string:an bear cook are bamber with tiktok
# The sorted words are:
# an
# are
# bamber
# bear
# cook
# tiktok
# with