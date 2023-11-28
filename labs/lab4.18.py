''' zyBooks Introduction to Python - Lab 4.18: Exact Change

Write a program with total change amount as an integer input, 
and output the change using the fewest coins, one coin type per line.
The coin types are Dollars, Quarters, Dimes, Nickels, and Pennies. 
Use singular and plural coin names as appropriate, 
like 1 Penny vs. 2 Pennies.
'''

DEBUG=False

def debug(msg: str) -> None:
    if DEBUG==True:
        print(msg)

cents    = int(input())
debug(f"cents={cents}")
dollars  = cents // 100
debug(f"dollars={dollars}")
change   = cents % 100
debug(f"change={change}")
quarters = change // 25
debug(f"quarters={quarters}")
change   = change % 25
debug(f"change={change}")
dimes    = change // 10
debug(f"dimes={dimes}")
change   = change % 10
debug(f"change={change}")
nickels  = change // 5
debug(f"nickels={nickels}")
pennies  = change % 5
debug(f"pennies={pennies}")

if cents <= 0: print("No change")
else:
    if dollars > 1: print(f"{dollars} Dollars")
    elif dollars == 1: print(f"{dollars} Dollar")
    
    if quarters > 1: print(f"{quarters} Quarters")
    elif quarters == 1: print(f"{quarters} Quarter")

    if dimes > 1: print(f"{dimes} Dimes")
    elif dimes == 1: print(f"{dimes} Dime")
    
    if nickels > 1: print(f"{nickels} Nickels")
    elif nickels == 1: print(f"{nickels} Nickel")
    
    if pennies > 1: print(f"{pennies} Pennies")
    elif pennies == 1: print(f"{pennies} Penny")
