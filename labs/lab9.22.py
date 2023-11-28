''' zyBooks Intro to Python 9.22 LAB: Elements in a range

Write a program that first gets a list of integers from input. 
    That list is followed by two more integers representing lower 
    and upper bounds of a range. Your program should output all integers 
    from the list that are within that range (inclusive of the bounds).
Ex: If the input is:
        25 51 0 200 33
        0 50
    the output is:
        25,0,33,

The bounds are 0-50, so 51 and 200 are out of range and thus not output.

For coding simplicity, follow each output integer by a comma, 
    even the last one. Do not end with newline.

'''

DEBUG=False
def debug(msg): print(f'DEBUG: {msg}') if DEBUG else None

def main():
    debug(DEBUG)
    userInput = "25 51 0 200 33" if DEBUG else input()
    userRange = "0 50" if DEBUG else input()
    debug(f'userInput: {userInput} :: userRange: {userRange}')
    userInput = userInput.split()
    userRange = userRange.split()
    debug(f'userInput: {userInput} :: userRange: {userRange}')
    userInput = [x for x in userInput if (int(userRange[0]) <= int(x) <= int(userRange[1]))]
    debug(f'userInput: {userInput} :: userRange: {userRange}')
    userInput = ','.join(userInput)
    debug(f'userInput: {userInput} :: userRange: {userRange}')
    print(userInput,end=',')

if __name__=="__main__": main()
