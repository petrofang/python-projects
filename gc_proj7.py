""" Intro to Python: Programming Project Week 7

Your best friends have an anniversary coming up. You would like 
to plan a party to celebrate this special day.  In the past, 
you have put together parties and found that the cost can get 
way out of control.  In order to avoid overspending, you want 
to pre-plan exactly how the money will be spent for this party.

You are to code the following to help with the planning process:
    
*** PART 1    Define the following functions:
menu()
    This function accepts no parameters.  The function is simply 
    print out a list of options for the user to see.  The options are:
        output cost of the food
        output the cost of beverages
        output the cost of food, beverages and the total cost of the event

foodCost(numGuests)
    This function accepts one parameter, the number of guests for the event,
    and returns the cost of the food.  You plan to simply provide a small 
    cheese & cracker plate (8.00) for each guest, plus one large sheet cake.  
    The cake price will vary depending on the number of guests:
        1-10 guests         15.00
        11-25  guests       30.00
        25-50 guests        65.00
    This function is to calculate and return the cost of the food.   
    (This function is to perform NO output).

beverageCost(numGuests)
    This function accepts one parameter, the number of guests for the event
    and returns the cost of the wine provided for the event.  The number of 
    bottles of wine which will be provided by the house.  You are providing 
    one bottle per 3 guests (or less).
         The means, if there are 21 guests, 7 bottles would be provided.
                    If there are 22 guests, 8 bottles would be provided
                    If there are 23 guests, 8 bottles would be provided
                    If there are 24 guests, 8 bottles would be provided.
    The wine is priced at $10 per bottle.
    This function is to calculate and RETURN the beverage cost.  
    (This function is to perform NO output).

Be sure that each of your functions is self-contained … that is, 
your function should use the parameter value, and not use any 
variables from elsewhere in the program.  Any value to be communicated 
to the main program should be RETURNED returned (no globals). 

*** PART 2     Main process to calculate party cost 
The main process for your program is to:

*Ask the user for the number of guests.  If the number is invalid 
(negative or greater than 50), this function is to reprompt the user 
UNTIL a valid number is entered.

The program is then to allow the user to choose 
    between the following 3 options:
        output cost of the food
        output the cost of beverages
        output ALL INFO (number of guests, food cost, 
                         beverage cost and total cost)

Be sure to call the functions you have written for Part 1.   
The menu() function displays options to the user, and there are 
    functions to determine the various costs as well. 

STYLE:  Be sure that your program names variables in a meaningful manner. 
        Comment all function definitions to indicate what the function will do
        and comment your program body to indicate what is going on (remember, 
        each line does not need a comment, just each group of statements that 
        performs one task).  A comment need not be a complete sentence - 
        just a short phrase.
"""

def menu() -> None:
    # print function for program option menu
    print   ("""
              > 1    output cost of the food
              > 2    output the cost of beverages
              > 3    output ALL INFO 
             (number of guests, food cost, beverage cost and total cost)
             Select: 1    2    3
             """)

def foodCost(numGuests: int) -> float: 
    # return the cost of the food
    if   numGuests<=10: cake=15.0
    elif numGuests<=25: cake=30.0
    else:               cake=65.0
    plates=numGuests*8.0
    cost = plates+cake
    return cost

def beverageCost(numGuests: int) -> float:
    # return the cost of the drinks
    bottles = -(-numGuests // 3) # get ceil(n) without math module
    cost=bottles*10.0
    return cost

def printInfo(numGuests: int) -> None:
    # calculate values and display totals
    totalCost = foodCost(numGuests)+beverageCost(numGuests)
    print(f"# Guests    :   {numGuests}")
    print(f"------------+-----------")
    print(f"Food Cost   :   ${foodCost(numGuests):.2f}")
    print(f"Drink Cost  :   ${beverageCost(numGuests):.2f}")
    print(f"------------+-----------")
    print(f"Total Cost  :   ${totalCost:.2f}")
    print(f"------------+-----------\n\n")

def main(): 
    guests=0
    # wait for viable guest count:
    while (guests < 1) or (guests > 50): 
        guests=int(input("how many guests? (1-50)\n>"))
    
    option=0
    # wait for viable option:
    while option != 3:
        menu()
        try: option = int(input("now what?\n > ")[0])
        except ValueError: pass

        # let them keep going until they get total cost
        if   option==1: print(f"Food Cost:  ${foodCost(guests):.2f}")
        elif option==2: print(f"Drink Cost: ${beverageCost(guests):.2f}")
        elif option==3: printInfo(guests)
        else: pass


# loop the program
while __name__ == "__main__": main()