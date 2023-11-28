''' zyBooks Intro to Python 8.13 LAB: Remove all non-alpha characters

Write a program that removes all non-alpha characters from the given input.
Ex: If the input is:
        -Hello, 1 world$!
    the output is:
        Helloworld
'''

DEBUG=False
def debug(msg): 
    if DEBUG: print(f'DEBUG: {msg}')
    
if DEBUG: userInput="-Hello, 1 world$!"
else: userInput=input()

def main():
    uiClean=''
    for a in range(len(userInput)):
        debug(f'userInput[{a}]=={userInput[a]}')
        debug(f'userInput[{a}].isalpha()=={userInput[a].isalpha()}')
        if userInput[a].isalpha():
            uiClean+=(userInput[a])
    print(uiClean)
    return None

if __name__=="__main__": main()