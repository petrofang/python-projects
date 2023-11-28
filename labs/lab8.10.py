''' zyBooks Intro to Python 8.10 LAB: Acronyms

An acronym is a word formed from the initial letters 
of words in a set phrase. Write a program whose input 
is a phrase and whose output is an acronym of the input. 
Append a period (.) after each letter in the acronym. 
If a word begins with a lower case letter, don't include 
that letter in the acronym. Assume the input has at least 
one upper case letter.

Ex: If the input is:
        Institute of Electrical and Electronics Engineers
    the output is:
        I.E.E.E.
Ex: If the input is:
        Association for computing MACHINERY
    the output is:
        A.M.

The letters ACHINERY in MACHINERY don't start a word, so those letters are omitted.

Hint: Use isupper() to check if a letter is upper case.
'''

DEBUG=False
def db(_): 
    if DEBUG: print(_)
if DEBUG: term="Institute of Electrical and Electronics Engineers"
else: term=input()
termSplit=term.split()
termAcronym=""
for i in range(len(termSplit)):
    if termSplit[i][0].isupper(): 
        db(termSplit[i])
        db(termSplit[i][0])
        db(termSplit[i][0].isupper())
        termAcronym+=f'{termSplit[i][0]}.'
        db(termAcronym)
print(termAcronym)