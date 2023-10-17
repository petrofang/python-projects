'''Intro to Python: Programming Project Week 8

Your friend Julia has a problem.  She goes grocery shopping 
on a weekly basis, and always seems to forget to buy items 
that she needs.  You have suggested that she make a list 
before she goes, and have offered to write a program 
to help Julia produce her shopping list.

Your program should define and use the following functions 
to help perform the above tasks:

addItem (some_list)
    The function addItem accepts one parameter, which is a list. 
    This function prompts the user for an item to be added to the list.  
    If the item is not already on the list, the item is added 
    to the end of the list. Otherwise, a message is given 
    indicating that the item is already on the list.

removeItem(some_list)
    The function addItem accepts one parameter, which is a list. 
    This function prompts the user for an item to be removed from the list.
    If the item on the list, it is removed from the list. Otherwise, 
    a message is given indicating that the item was not on the list.

printOut(some_list)
    The function printOut accepts one parameter, which is a list.  
    This function prints out a header: GROCERY LIST followed by 
    a list of all of the items in the list, one at a time

THESE functions should be placed in a separate MODULE (another file).  
The main process will be in it's own file which import the function module
in order to call these functions.

The main part of your program will start by creating an empty list.   
The user will then be allowed to choose any of the following options  
UNTIL he/she wishes to exit.
    * ADD an item to the list
        The user will provide the item to be added. If the item is not 
        on the list, it will be added, otherwise a message will be 
        given that the item is already on the list.      
        (You will call your addItem function to help here)
    * FIND an item on the list
        The user will provide an item and the program will report 
        if the item is already on the list or not.
    * PRINT all items
        All items on the list are to be printed out, one per line   
        (function printOut helps here)
    * REMOVE an item from the list
        The user will provide an item to be removed.  If it's there, 
        it is removed, otherwise a message is given.   
        (You will call your removeItem function to help here)

Be sure your program is readable and well-commented.  Test all options, 
remember some choices have two paths (eg. choosing ADD will either 
                                      add an item or print a message). 

Place your functions in their own file (module) and import this file 
into your main.  Not only is this a more professional touch, but 
doing so is a good way to ensure that you are not using any 
global variables in your function!!!
'''


from gc_proj8_includes import add_item
from gc_proj8_includes import remove_item
from gc_proj8_includes import printOut
from gc_proj8_includes import find_item
theShoppingList=[]

def main(): 
    choice=""
    while choice != "X":
        printMenu()
        choice=input("Select an option: > ")[0].upper
        if choice=="A": theShoppingList=add_item(theShoppingList)
        if choice=="F": find_item(theShoppingList)
        if choice=="P": printOut(theShoppingList)
        if choice=="R": theShoppingList=remove_item(theShoppingList)
        if choice=="X": quit()

def printMenu():
    print('''
+===================================+
|   (A)DD an item to the list       |
|   (F)IND an item on the list      |
|   (P)RINT all items on the list   |
|   (R)EMOVE an item from the list  |
|  E(X)IT the shopping list program |
+===================================+''')   

if __name__ == "__main__":
    main()