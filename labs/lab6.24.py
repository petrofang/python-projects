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
    in the execute_menu() function, and then output the returned value. (4 pts)
'''