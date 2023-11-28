''' zyBooks Intro to Python 9.20 LAB: Filter and sort a list

Write a program that gets a list of integers from input, 
and outputs negative integers in descending order (highest to lowest).

Ex: If the input is:
        10 -7 4 -39 -6 12 -2
    the output is:
        -2 -6 -7 -39 
        
For coding simplicity, follow every output value by a space. 
Do not end with newline.
'''

DEBUG=False
def debug(msg): print(f'DEBUG: {msg}') if DEBUG else None

def main():
    debug(DEBUG)
    userInput = "10 -7 4 -39 -6 12 -2" if DEBUG else input()
    debug(f"userInput = {userInput}")
    userInput = userInput.split()
    debug(f"userInput = {userInput}")
    userInput = [int(i) for i in userInput if int(i)<0]
    debug(f"userInput = {userInput}")
    userInput.sort()
    debug(f"userInput = {userInput}")
    userInput.reverse()
    debug(f"userInput = {userInput}")
    userInput = [str(i) for i in userInput]
    debug(f"userInput = {userInput}")
    userInput = ' '.join(userInput)
    debug(f"userInput = '{userInput}'")
    print(userInput, end=" ")

if __name__=="__main__": main()
