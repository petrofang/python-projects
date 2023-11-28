''' zyBooks Intro to Python 8.7 LAB: Count characters

Write a program whose input is a string which contains a character 
and a phrase, and whose output indicates the number of times 
the character appears in the phrase. The output should include 
the input character and use the plural form, n's, if the number of times 
the characters appears is not exactly 1.
'''
def countChars(phrase: str, char:str) -> int:
    count = 0
    for i in range(len(phrase)):
        if phrase[i] == char: count+=1
    return count

if __name__=="__main__":
    letter, words = input().split(maxsplit=1)
    chars = countChars(words, letter)
    if chars != 1: s="'s"
    else: s = ""
    print(f'{chars} {letter}{s}')
