"""
Author: Dương Trường Thọ
Date: 18/07/2021
Program: exersice_05_page_92.py
Problem:
   What is the maximum number of guesses necessary to guess correctly a given number between the numbers N and M?
Solution:
    L=[1,1000]
    G={}
    for n in range(1,11):
        i=0
        while i<len(L)-1:
            guess = int(0.5*(L[i]+L[i+1]+1))
            if guess not in L:
                L = L[:i+1]+[guess]+L[i+1:]
                i+=1
                G[guess] = n
            i+=1
    S=0
    for g in G:
        S+=G[g]
    print ((10+S+10)/1000)
    ....
"""
L=[1,1000]
G={}
for n in range(1,11):
    i=0
    while i<len(L)-1:
        guess = int(0.5*(L[i]+L[i+1]+1))
        if guess not in L:
            L = L[:i+1]+[guess]+L[i+1:]
            i+=1
            G[guess] = n
        i+=1
S=0
for g in G:
    S+=G[g]
print ((10+S+10)/1000)
# 8.987