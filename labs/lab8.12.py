''' zyBooks Intro to Python 8.12 LAB: Warm up: Parsing strings

(1) Prompt the user for a string that contains two strings 
    separated by a comma. (1 pt)

Examples of strings that can be accepted:
    Jill, Allen
    Jill , Allen
    Jill,Allen
Ex:
Enter input string:
Jill, Allen

(2) Report an error if the input string does not contain a comma. 
    Continue to prompt until a valid string is entered. 
    Note: If the input contains a comma, then assume that the 
    input also contains two strings. (2 pts)
    Ex:
Enter input string:
Jill Allen
Error: No comma in string.
Enter input string: Jill, Allen

(3) Using string splitting, extract the two words from the input 
    string and then remove any spaces. Output the two words. (2 pts)
    Ex:
Enter input string:
Jill, Allen
First word: Jill
Second word: Allen

(4) Using a loop, extend the program to handle multiple lines of input. 
Continue until the user enters q to quit. (2 pts)

'''

DEBUG=False
def debug(msg: str) -> None: print(f"DEBUG: {msg}") if DEBUG else None

def comma(string: str) -> bool:
    if ',' in string: comma=True
    else: comma=False
    debug(f"'{string}' contains comma: {comma}")
    return comma
    

def printOut(name: list):
    print(f'First word: {name[0]}')
    print(f'Second word: {name[1]}\n')

def main():
    debug("Debug Mode Activated")
    if DEBUG: userInput="Jill , Allen"
    else: userInput=input("Enter input string:\n")
    

    while userInput != 'q':
        while not comma(userInput):
            debug(f"while not comma in '{userInput}':")
            if userInput=='q': 
                debug(f"userInput=='q'")
                quit()
            else:
                print("Error: No comma in string.\n")
                debug(f"userInput=='{userInput}'")
                userInput=input("Enter input string:\n")
        else:
            debug(f'else: userInput.split(",")')
            userSplit=userInput.split(',',1)
            debug(f'userSplit={userSplit}')
            for each in range(len(userSplit)):
                debug(f'userSplit[{each}]={userSplit[each].strip()}') 
                userSplit[each]=userSplit[each].strip()
            printOut(userSplit)
            userInput=input("Enter input string:\n")    
    else: debug(f"userInput=='{userInput}'")

    
if __name__=="__main__": main()