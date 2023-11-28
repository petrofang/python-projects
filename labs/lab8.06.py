''' zyBooks Intro to Python 8.6 LAB: Name format

Many documents use a specific format for a person's name. 
Write a program that reads a person's name in the following format:

firstName middleName lastName (in one line)

and outputs the person's name in the following format:

lastName, firstInitial.middleInitial.
'''

name=input()
names=name.split(' ')
print(f'{names[-1]}, ', end="")
for n in range(len(names)-1): print(f'{names[n][0]}.', end="")
print()