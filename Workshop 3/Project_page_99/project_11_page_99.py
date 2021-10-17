"""
Author: Dương Trường Thọ
Date: 18/07/2021
Program: project_11_page_99.py
Problem:
    In the game of Lucky Sevens, the player rolls a pair of dice. If the dots add up to 7,
    the player wins $4; otherwise, the player loses $1. Suppose that, to entice the gullible, a casino tells players that there are lots of ways to win: (1, 6), (2, 5), and so
    on. A little mathematical analysis reveals that there are not enough ways to win
    to make the game worthwhile; however, because many people’s eyes glaze over
    at the first mention of mathematics, your challenge is to write a program that
    demonstrates the futility of playing the game. Your program should take as input
    the amount of money that the player wants to put into the pot, and play the game
    until the pot is empty. At that point, the program should print the number of
    rolls it took to break the player, as well as maximum amount of money in the pot.
Solution:
    
    ....
"""
import random

def playRound(budget: int) -> tuple:
    """ 
        The values are calculated directly inside the params so
        that the Garabage Collector can know the memory is free. 
        While not import here, it is still an important thing to 
        be aware of in any program.    
    """
    sum = sumOfDice(random.randint(1,6), random.randint(1,6))
    if sum == 7:
        budget += 4
        return ("Win",budget)
    else:
        budget -= 1
        return ("Loss",budget)

def sumOfDice(die1: int, die2: int) -> int:
        return die1 + die2

def haveMoney(budget: int) -> bool:
    # This is a ternary expression it is an if statement in one line
    #     Truthy   Expression      Falsy
    return True if budget > 0 else False

def main():
    numRolls = 0

    """
        This is a template string, not to be confused with an F-String.
        The user may use str.format(args*,kwargs**) to unpack into it.
        In english, kwargs pass keyword with value and it will fill 
        respectively. For args, pass in order as each number represents 
        an index to fill the values respectively.
    """
    outputString = "\t{0}\t\t{1}\t\t{2}"

    # To prevent a type error, the string is explicitly converted to int
    budget = int(input("What is your gambling budget?"))

    # \t is the metacharacter representing a tab
    print("Number of rolls\t\tWin or Loss\tCurrent value of the pot")

    print(outputString.format(numRolls, "Put", budget))

    # The return value is a boolean type, thus the output is the expression
    while haveMoney(budget):
        # Python does not support the pre-increment or post-crement operator
        numRolls += 1
        output = playRound(budget)
        budget = output[1]
        print(outputString.format(numRolls, output[0], output[1]))

    print("Sorry you're out of money")    

# Entry point for a Python program
if __name__ == "__main__":
    main()
    # Your solution works but it does not need a dedicated funct
    while True:
        userIn = input("Would you like to play again?")
        if 'yes' == userIn:
            main()
        else:
            print("Goodbye")
            break