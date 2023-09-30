""" Intro to Python: Programming Project Week 5

You are to update your Lee Rent-a-Car project from WEEK 4
to work as follows:

1. Allow the user to enter the rental option (A, B, C, or D). 
IF the user does NOT enter a valid option letter, REPROMPT 
and allow the user to reenter UNTIL the user enters a valid option.
 
2. Rather than simply calculating the cost for a one day rental, 
prompt the user for the number of days they wish to rent.
   For each day:
Allow the user to enter the number of miles traveled
Output the base charge for the rental
Output the cost for extra miles traveled
Output the final cost for the day's rental
 
3. Output the total cost for the entire rental.

THIS WEEK's FOCUS is WHILE LOOPS, 
so please use ONLY WHILE LOOPS for repetition in this project.
"""
options = ["A", "B", "C", "D"] # list for cleaner code

# # # dictionary for number of days
ordinal = {
  1: "first",
  2: "second",
  3: "third",
  4: "fourth",
  5: "fifth",
  6: "sixth",
  7: "seventh",
  8: "eighth",
  9: "ninth",
  10: "tenth",
  11: "eleventh",
  12: "twelfth",
  13: "thirteenth",
  14: "fourteenth"
}

print("-=============================================================-")
print(" Thank you for choosing Lee Rent-a-Car for your  . . .  rental ")
print("-=============================================================-")
option=""

# prompt user for option until valid option selected
while option not in options:
    print(f"Please select a rental option:  {options}")
    print("For option details, enter question mark:    ?")
    option = input("> ")
    # take only the first character, and capitalize it
    option=option[0].upper() 
    
    # a little help screen option
    if option == "?":
        # FIXME: make this a print function
        print(r"     \   Daily Charge   |   Mileage Limit  |   Extra Mile Charge")
        print(r"-=====\================-+-================-+-===================-")
        print(r"Option A:   100.00      |       200        |   .20 / mile")
        print(r"Option B:   150.00      |       300        |   .10 / mile")
        print(r"Option C:   200.00      |       500        |   .05 / mile")
        print(r"Option D:   250.00      |    unlimited     |      N/A")
    else:
        # here is the error message that should have been in project 4
        if option not in options and option !="?":
            print(f"ERROR: User selected '{option}' which was not one of the options...") 

# set values based on user input
if option == "A":
        daily=100.00
        limit=200.00
        charge=0.20
elif option == "B":
        daily=150.00
        limit=300.00
        charge=0.10
elif option == "C":
        daily=200.00
        limit=500.00
        charge=0.05
elif option =="D":
        daily=250.00
        limit=0.00
        charge=0.00

# get length of rental from user:
days=int(input("Excellent choice! And how many days is/was the rental? > "))

# filter out nonsense:
if days <= 0:
    print("Hey, that's great! See you later.")
    exit()
elif days > 14:
    print("Please see the leasing office for rentals over two weeks.")
    input("Would you like to rent for just two weeks?\n>")
    days = 14 # FIXME: give them a "no" option
print(f"Wonderful. I will mark you down for {days} days.")

day = 1
total = 0
while day <= days:
    # get mileage from user    
    mileage = float(input(f"what was the mileage for the {ordinal[day]} day? > "))
    overage = max(0, mileage-limit)
    fee = charge*overage
    dayCharge = fee + daily
    print(r" daily charge  :", end="")
    print(f"{daily:>16.2f}")      
    print(r" mileage fee   :", end="")                 
    print(f"{fee:>16.2f}")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print(f"day {day} charge   :", end="")              
    print(f"{dayCharge:>16.2f}")
    day+=1 
    total = total + dayCharge
else:
    print("=+==-=-=-=-=-=-=-=-=-=-=-=-=-==+=")
    print(r" TOTAL CHARGE  :", end="")                 
    print(f"{total:>16.2f}")

exit()

