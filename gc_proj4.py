""" Intro to Python: Programming Project Week 4

Lee Rent-a-Car has hired you to write a program that will 
help speed up their billing for a one day rental. 

Customer rentals are billed as follows:
            Daily Charge    Mileage Limit     Extra Mile Charge
Option A        100.00          200              .20 per mile
Option B        150.00          300              .10 per mile
Option C        200.00          500              .05 per mile
Option D        250.00        unlimited              N/A

You are to write a program which:

* Allows the user to enter the rental option (A,B,C or D)
* Allows the user to enter the number of miles traveled
* Outputs the base charge for the rental
* Outputs the cost for extra miles traveled
* Outputs the final cost for the one day rental
* Gives error message if option is invalid
"""

#########################################
#                                       #
#   CIS177: Intro to Python             #
#     Project 4: Car Rental Program     #
#            by: Giles Cooper           #
#                                       #
#########################################
print("-=============================================================-")
print(" Thank you for choosing Lee Rent-a-Car for your one-day rental ")
print("-=============================================================-")
option=""
# going to just use a while-loop here; if bad input user can try again
while option != "A" and option != "B" and option != "C" and option != "D":
    print(option)
    print("Please select a rental option:  A   B   C   D")

    print("For option details, enter question mark:    ?")
    option = input("> ")
    
    # a little help screen option
    if option == "?":
        print(r"     \   Daily Charge   |   Mileage Limit  |   Extra Mile Charge")
        print(r"-=====\================-+-================-+-===================-")
        print(r"Option A:   100.00      |       200        |   .20 / mile")
        print(r"Option B:   150.00      |       300        |   .10 / mile")
        print(r"Option C:   200.00      |       500        |   .05 / mile")
        print(r"Option D:   250.00      |    unlimited     |      N/A")
    else:
        # take only the first character, and capitalize it
        option=option[0].upper() 
        
# get mileage from user    
mileage=float(input("Excellent choice! And how many miles were travelled?\n> "))

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
overage=max(0, mileage-limit)
fee=charge*overage

# print formatted results
print(r" one-day charge:", end="")
print(f"{daily:>16.2f}")      
print(r" your mileage  :", end="")       
print(f"{mileage:>9.1f}")
print(r" free mileage  :", end="")
print(f"{limit:>9.1f}")
print(r" extra mileage :", end="")
print(f"{overage:>9.1f}")
print(r" fee per mile  :", end="")
print(f"{charge:>10.2f}")
print(r" mileage fee   :", end="")                 
print(f"{fee:>16.2f}")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print(r" total charge  :", end="")              
print(f"{fee+daily:>16.2f}")


