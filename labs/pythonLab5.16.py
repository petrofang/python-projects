'''
5.16 LAB: Print string in reverse
Write a program that takes in a line of text as input, 
and outputs that line of text in reverse. The program 
repeats, ending when the user enters "Done", "done", 
                        or "d" for the line of text.
'''

done = [
    'done',
    'Done',
    'd',
]

phrase=""
while phrase not in done:
    phrase = input()
    if phrase in done:
        break
    phrase_r = ""
    i = len(phrase)-1
    while i >= 0:
        phrase_r = phrase_r + phrase[i]
        i-=1
    print(phrase_r)
