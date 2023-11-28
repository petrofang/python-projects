''' zyBooks Intro to Python 8.20 LAB: Login name

Write a program that creates a login name for a user, 
given the user's first name, last name, and a four-digit 
integer as input. Output the login name, which is made up of 
the first five letters of the last name, followed by the 
first letter of the first name, and then the last two digits 
of the number (use the % operator). If the last name has 
less than five letters, then use all letters of the last name.

Ex: If the input is:
        Michael Jordan 1991
    the output is:
        Your login name: JordaM91
'''
DEBUG=False
if DEBUG==True: userInput="Michael Jordan 1991"
else: userInput=input()
userSplit=userInput.split()
userLogin=f'{userSplit[1][:5]}{userSplit[0][0]}{userSplit[2][-2:]}'
print(f'Your login name: {userLogin}')