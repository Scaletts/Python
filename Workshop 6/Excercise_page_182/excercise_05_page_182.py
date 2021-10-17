"""
Author: DuongTruongTho
Date: 02/09/2021
Program: Exersice_05_page_182.py
Problem:
       Explain what happens when the following recursive function is called with the value 4
        as an argument:
        def example(n):
        if n > 0:
        print(n)
        example(n)
        else:
        example(n - 1)
Solution:
        It is common practice to extend the factorial function for 0 as an argument. It makes sense to define 0! to be 1, 
       because there is exactly one permutation of zero objects, i.e. if nothing is to permute, "everything" is left in place. 
       Another reason is that the number of ways to choose n elements among a set of n is calculated as n! divided by 
       the product of n! and 0!.
    
"""