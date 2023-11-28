''' zyBooks Intro to Python 8.14 LAB: Fun with characters

Complete the check_character() function which has 2 parameters:
A string, and a specified index. The function checks the character 
at the specified index of the string parameter, and returns 
a string based on the type of character at that location 
indicating if the character is a letter, digit, whitespace, 
or unknown character.

Ex: The function calls below with the given arguments will 
    return the following strings:
        check_character('happy birthday', 2) 
returns "Character 'p' is a letter"
        check_character('happy birthday', 5) 
returns "Character ' ' is a white space"
        check_character('happy birthday 2 you', 15) 
returns "Character '2' is a digit"
        check_character('happy birthday!', 14) 
returns "Character '!' is unknown"
'''

DEBUG=False
def debug(msg): 
    if DEBUG: print(f'DEBUG: {msg}')

def check_character(word:str, index:int) -> None:
    debug(f"check_character('{word}', {index})")
    debug(f"word[{index}]: '{word[index]}'")
    iType="unknown"
    if word[index].isalpha(): 
        debug(f"word[{index}].isalpha() = {word[index].isalpha()}")
        iType="a letter"
    if word[index].isspace(): 
        debug(f"word[{index}].isspace() = {word[index].isspace()}")
        iType="a white space"
    if word[index].isnumeric(): 
        debug(f"word[{index}].isnumeric() = {word[index].isnumeric()}")
        iType="a digit"
    debug(iType)
    return f"Character '{word[index]}' is {iType}"
    
  
def main():
    print(check_character('happy birthday', 2))
    print(check_character('happy birthday', 5))
    print(check_character('happy birthday 2 you', 15))
    print(check_character('happy birthday!', 14))

if __name__=="__main__": main()
