""" A simple example demonstrating the use of regular expressions in
python.  To convert a word to piglatin: If it starts with one of more
consonant, move them to the end and append 'ay'; else it starts with
one or more vowel, so keep as is, but add 'zay' to the end of the
word.

Modified based on https://www.csee.umbc.edu/courses/331/fall11/code/python/pig.py
"""

import re

# this pattern matches a word that begins with one or more
# consonants.  The first match group will contains the initial
# consonants and the second the rest of the word.

pat = "([bcdfghjklmnpqrstvwxyz]+)(\w+)"

# compile pat
cpat = re.compile(pat)

def piglatin(string):
    """ given a string of words, breaks it up into words, and reassembles
        and returns a string of the piglatin form"""
    return " ".join( [piglatin1(w) for w in string.split()] )

def piglatin1(word):
    """returns the pig latin form of word"""
    match = cpat.match(word)
    if match:
        consonants = match.group(1)
        rest = match.group(2)
        return rest + consonants + "ay"
    else:
        return word + "zay"

def loop():
    """a REPL-like loop"""
    while True:
        userinput = input("sentence> ")
        print(piglatin(userinput))
        print


# If called as a script enter the REPL loop
if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        print("\nGoodbye!")
