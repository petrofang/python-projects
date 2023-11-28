''' zyBooks Intro to Python 8.11 LAB: Contains the character

Write a program that reads a character, then reads in a list of words.
The output of the program is every word in the list that contains 
the character at least once. Assume at least one word in the list 
will contain the given character.

Ex: If the input is:
        z
        hello zoo sleep drizzle
    the output is:
        zoo,drizzle,

Keep in mind that the character 'a' is not equal to the character 'A'.

For coding simplicity, follow each output word by a comma, 
even the last one. Do not end with newline.
'''

DEBUG=False
def db(_): print(_) if DEBUG else None
if DEBUG: letter, phrase = 'z', 'hello zoo sleep drizzle'
else: letter, phrase = input(), input()

phraseList=phrase.split()
wordList=[]
wordListString=""
for i in range(len(phraseList)): 
    if letter in phraseList[i]: wordList.append(phraseList[i])
for i in range(len(wordList)): wordListString+=wordList[i]+','
print(wordListString, end='')

