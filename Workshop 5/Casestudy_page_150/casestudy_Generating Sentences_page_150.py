"""
Author: DuongTruongTho
Date: 09/08/2021
Program: casestudy_Generating Sentences_page150.py
Problem:
    CaSe StuDy: Generating Sentences
    Can computers write poetry? We’ll attempt to answer that question in this case study
    by giving a program a few words to play with.
    Request
    Write a program that generates sentences.
    Analysis
    Sentences in any language have a structure defined by a grammar. They also include
    a set of words from the vocabulary of the language. The vocabulary of a language
    like English consists of many thousands of words, and the grammar rules are quite
    complex. For the sake of simplicity our program will generate sentences from a simplified subset of English. The vocabulary will consist of sample words from several
    parts of speech, including nouns, verbs, articles, and prepositions. From these words,
    you can build noun phrases, prepositional phrases, and verb phrases. From these
    constituent phrases, you can build sentences. For example, the sentence “The girl hit
    the ball with the bat” contains three noun phrases, one verb phrase, and one prepositional phrase. Table 5-3 summarizes the grammar rules for our subset of English.  

Solution:
    THE BALL HIT THE BALL WITH THE BOY
    THE BOY SAW THE BAT BY A BAT
    A BAT SAW THE BALL BY A BALL
    THE BOY SAW A BALL WITH THE BALL
    A GIRL HIT THE GIRL BY A GIRL
    Enter the number of sentences: 5
    

"""
import random
# Vocabulary: words in 4 different parts of speech
articles = ("A", "THE")
nouns = ("BOY", "GIRL", "BAT", "BALL")
verbs = ("HIT", "SAW", "LIKED")
prepositions = ("WITH", "BY")
def sentence():
    return nounPhrase() + " " + verbPhrase()
def nounPhrase():
    return random.choice(articles) + " " + random.choice(nouns)
def verbPhrase():
    return random.choice(verbs) + " " + nounPhrase() + " " + \
prepositionalPhrase()
def prepositionalPhrase():
    return random.choice(prepositions) + " " + nounPhrase()
def main():
    number = int(input("Enter the number of sentences: "))
for count in range (5):
    print(sentence())
# The entry point for program execution
if __name__ == "__main__":
    main()