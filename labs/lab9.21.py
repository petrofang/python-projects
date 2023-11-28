''' zyBooks Intro to Python 9.21 LAB: Middle item

Given a sorted list of integers, output "Middle item: " followed by 
the middle integer. Assume the number of integers is always odd.
Ex: If the input is:
        2 3 4 8 11
    the output is:
        Middle item: 4

The maximum number of inputs for any test case should not exceed 9.
If exceeded, output "Too many inputs".

Hint: First read the data into a list. Then, based on the list's size, 
find the middle item.
'''

DEBUG=False
def debug(msg): print(f'DEBUG: {msg}') if DEBUG else None

def main():
    debug(DEBUG)
    userInput = '2 3 4 8 11' if DEBUG else input()
    userInput = userInput.split()
    if len(userInput) > 9: print("Too many inputs")
    else:
        while len(userInput) > 2:
            userInput=userInput[1:-1]
        userInput=str(userInput[0])
        print(f'Middle item: {userInput}')

if __name__=="__main__": main()
