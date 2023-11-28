''' 6.30 LAB*: Program: Authoring assistant

(1) Prompt the user to enter a string of their choosing. 
    Store the text in a string. Output the string. (1 pt)

(2) Implement the print_menu() function to print the following 
    command menu. (1 pt)

MENU
c - Number of non-whitespace characters
w - Number of words
f - Fix capitalization
r - Replace punctuation
s - Shorten spaces
q - Quit

(3) Implement the execute_menu() function that takes 
    2 parameters: a character representing the user's choice 
    and the user provided sample text. execute_menu() 
    performs the menu options, according to the user's choice, 
    by calling the appropriate functions described below. (1 pt)

(4) In the main program, call print_menu() and prompt for the 
    user's choice of menu options for analyzing/editing the string.
    Each option is represented by a single character.

    If an invalid character is entered, continue to prompt for
    a valid choice. When a valid option is entered, execute 
    the option by calling execute_menu(). Then, print the menu 
    and prompt for a new option. Continue until the user enters 'q'. 
    Hint: Implement Quit before implementing other options. (1 pt)

(5) Implement the get_num_of_non_WS_characters() function. 
    get_num_of_non_WS_characters() has a string parameter 
    and returns the number of characters in the string, 
    excluding all whitespace. Call get_num_of_non_WS_characters() 
    in the execute_menu() function, 
    and then output the returned value. (4 pts)

(6) Implement the get_num_of_words() function. get_num_of_words()
    has a string parameter and returns the number of words 
    in the string. Hint: Words end when a space is reached 
    except for the last word in a sentence. Call get_num_of_words() 
    in the execute_menu() function, 
    and then output the returned value. (3 pts)

(7) Implement the fix_capitalization() function. fix_capitalization()
    has a string parameter and returns an updated string, where 
    lowercase letters at the beginning of sentences are replaced with 
    uppercase letters. fix_capitalization() also returns the number 
    of letters that have been capitalized. Call fix_capitalization()
    in the execute_menu() function, and then output the number 
    of letters capitalized followed by the edited string. 
    Hint 1: Look up and use Python functions .islower() and .upper() 
    to complete this task. 
    Hint 2: Create an empty string and use string concatenation 
    to make edits to the string. (3 pts)

(8) Implement the replace_punctuation() function. replace_punctuation()
    has a string parameter and two keyword argument parameters 
    exclamation_count and semicolon_count. replace_punctuation() 
    updates the string by replacing each exclamation point (!) character
    with a period (.) and each semicolon (;) character with a comma (,).
    replace_punctuation() also counts the number of times each character
    is replaced and outputs those counts. Lastly, replace_punctuation() 
    returns the updated string. Call replace_punctuation() in the 
    execute_menu() function, and then output the edited string. (3 pts)
'''

def main():
    phrase=input("Enter a sample text:\n")
    print(f"\nYou entered: {phrase}\n")
    while True:
        choice=""
        menu=["c", "f", "w", "r", "s", "q"]
        while choice not in menu:
            print_menu()
            choice=input("\nChoose an option:\n")[0]
        execute_menu(choice, phrase)    


def execute_menu(option:str, phrase:str):
    if option=="c": 
        print(f"Number of non-whitespace characters: {get_num_of_non_WS_characters(phrase)}\n")
    if option=="w": 
        print(f"Number of words: {get_num_of_words(phrase)}\n")
    if option=="f": 
        phrase, capitals = fix_capitalization(phrase)
        print(f"Number of letters capitalized: {capitals}")
        print(f"Edited text: {phrase}")
    if option=="r": replace_punctuation(phrase)
    if option=="s": shorten_space(phrase)
    if option=="q": quit()

def get_num_of_non_WS_characters(phrase: str) -> int: 
    ''' get_num_of_non_WS_characters() has a string parameter
    and returns the number of characters in the string, 
    excluding all whitespace. Call get_num_of_
    non_WS_characters() in the execute_menu() function, 
    and then output the returned value. (4 pts) '''
    whites=0
    for i in range(0,len(phrase)):
        if phrase[i] == " ": whites+=1
    return len(phrase) - whites

def get_num_of_words(phrase: str) -> int:
    ''' Hint: Words end when a space is reached 
    except for the last word in a sentence. 
    Call get_num_of_words() in the execute_menu() 
    function, and then output the returned value. (3 pts)'''
    # this passes but is it right?
    words=1
    wordEnd=[" ", ".", "?", "!"]
    for i in range(1,len(phrase)-1):
        if phrase[i] in wordEnd and phrase[i-1] not in wordEnd: words+=1
    return words

def shorten_space(phrase) -> str:
    ''' Implement the shorten_space() function. shorten_space() 
    has a string parameter and updates the string by replacing 
    all sequences of 2 or more spaces with a single space. 
    shorten_space() returns the string. Call shorten_space() in the 
    execute_menu() function, and then output the edited string. 
    Hint: Look up and use Python function .isspace(). (3 pt)'''
    return phrase # implement this function

def replace_punctuation(phrase: str, exclamation_count=0, semicolon_count=0) -> str:
    '''replace_punctuation() has a string parameter 
    and two keyword argument parameters exclamation_count 
    and semicolon_count. replace_punctuation() updates 
    the string by replacing each exclamation point (!) 
    character with a period (.) and each semicolon (;) 
    character with a comma (,). replace_punctuation() 
    also counts the number of times each character is replaced 
    and outputs those counts. Lastly, replace_punctuation() 
    returns the updated string. Call replace_punctuation() 
    in the execute_menu() function, 
    and then output the edited string. (3 pts)'''
    return phrase # TODO: implement function
    
def fix_capitalization(phrase: str):
    ''' fix_capitalization() has a string parameter 
    and returns an updated string, where lowercase 
    letters at the beginning of sentences are replaced 
    with uppercase letters. fix_capitalization() also 
    returns the number of letters that have been capitalized. 
    Call fix_capitalization() in the execute_menu() function,
    and then output the number of letters capitalized 
    followed by the edited string. 
    Hint 1: Look up and use Python functions .islower() 
    and .upper() to complete this task. 
    Hint 2: Create an empty string and use string concatenation 
    to make edits to the string. (3 pts)'''
    alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKMNOPQRSTUVWXYZ"
    capCount=0
    return_phrase=phrase[0].upper
    for i in range(1,len(phrase)-1):
        # FIXME: find a better way to determine start of word
        if phrase[i-1].isalpha:
            return_phrase+=phrase[i]
        else:
            capCount+=1
            return_phrase+=phrase[i].upper          
    return return_phrase, capCount

def print_menu():
    print(f"""MENU
c - Number of non-whitespace characters
w - Number of words
f - Fix capitalization
r - Replace punctuation
s - Shorten spaces
q - Quit""")

if __name__ == "__main__":
    main()