''' zyBooks Intro to Python 8.15 LAB: Remove digits - functions
Write a program that removes all digits from the given input.

Ex: If the input is:
        1244Crescent
    the output is:
        Crescent

The program must define and call the following function that takes 
a string as parameter and returns the string without any digits.

def remove_digits(user_string)
'''

DEBUG=False
def debug(msg): 
    if DEBUG: print(f'DEBUG: {msg}')

def remove_digits(user_string:str) -> str:
    for n in range(10):
        debug(str(n))
        user_string=user_string.replace(str(n),'')
    return user_string

def main():
    if DEBUG: print(remove_digits('1244Crescent'))
    else: print(remove_digits(input()))
    
if __name__=="__main__": main()
