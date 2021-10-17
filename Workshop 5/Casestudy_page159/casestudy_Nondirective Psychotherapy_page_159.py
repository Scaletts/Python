"""
Author: DuongTruongTho
Date: 09/08/2021
Program: casestudy_Nondirective Psychotherapy_page159.py
Problem:
    CaSe StuDy: Nondirective Psychotherapy
    In the early 1960s, the MIT computer scientist Joseph Weizenbaum developed a
    famous program called ELIZA that could converse with the computer user, mimicking
    a nondirective style of psychotherapy. The doctor in this kind of therapy is essentially
    a good listener who responds to the patient’s statements by rephrasing them or
    indirectly asking for more information. To illustrate the use of data structures, we
    develop a drastically simplified version of this program.
    Request
    Write a program that emulates a nondirective psychotherapist.
    Analysis
    Figure 5-4 shows the program’s interface as it changes throughout a sequence of
    exchanges with the user  

Solution:
    Good morning, I hope you are well today.
    Good morning, I hope you are well today.
    What can I do for you?
    >> My mother and I don't get along
    Why do you say that your mother and you don't get along
    >> she always favors my sister
    You seem to think that she always favors your sister
    >> my dad and I get along fine
    Can you explain why your dad and you get along fine
    >> he helps me with my homework
    Please tell me more
    >> quit
    Have a nice day 

"""
import random
hedges = ("Please tell me more.",
        "Many of my patients tell me the same thing.",
        "Please continue.")
qualifiers = ("Why do you say that ",
            "You seem to think that ",
            "Can you explain why ")
replacements = {"I":"you", "me":"you", "my":"your",
                "we":"you", "us":"you", "mine":"yours"}
def reply(sentence):
    probability = random.randint(1, 4)
    if probability == 1:
        return random.choice(hedges)
    else:
        return random.choice(qualifiers) + changePerson(sentence)
def changePerson(sentence):
    words = sentence.split()
    replyWords = []
    for word in words:
        replyWords.append(replacements.get(word, word))
    return " ".join(replyWords)
def main():

    print("Good morning, I hope you are well today.")
    print("What can I do for you?")
    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print("Have a nice day!")
            break
        print(reply(sentence))

if __name__ == "__main:__":
    main()               