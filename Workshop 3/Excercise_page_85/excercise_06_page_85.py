"""
Author: Dương Trường Thọ
Date: 18/07/2021
Program: exersice_06_page_85.py
Problem:
    Construct truth tables for the following Boolean expressions:
    a. not (A or B)
    b. not A and not B
Solution:
    def isAlphabaticOrder(s):
        n = len(s)
        c = [s[i] for i in range(len(s))]
        c.sort(reverse = False)
        for i in range(n):
            if (c[i] != s[i]):
                return False
        return True
    if __name__ == '__main__':
        s = "aabbbcc"
        if (isAlphabaticOrder(s)):
            print("Yes")
        else:
            print("No")
    ....
"""
def isAlphabaticOrder(s):
    n = len(s)
    c = [s[i] for i in range(len(s))]
    c.sort(reverse = False)
    for i in range(n):
        if (c[i] != s[i]):
            return False
    return True
if __name__ == '__main__':
    s = "aabbbcc"
    if (isAlphabaticOrder(s)):
        print("Yes")
    else:
        print("No")
# Yes