""" Intro to Python: Programming Project Week 2:

You are to a program which calculates the amount of money spent 
during one visit to the Green Lantern Diner. Your program is 
to assume that you have ordered 4 items. 

The program is to:

Allow the user to enter the name of each of the items purchased

Allow the user to enter the cost of each item

Print out a list of all items purchased and the cost

Calculate the amount due for the purchased items and print this subtotal

Calculate the tax amount due, assuming that the tax is 10% 
and print out the amount of tax due

Calculate the amount of tip, assuming that the service was great 
and 20% will be left … and print the amount of the tip

Calculate and print the total amount that was spent at the Diner

...
"""
# Giles Cooper's auto-waiter robot
from time import sleep 

#introduction and take the order
print("Welcome to the Green Lantern. I will be your automated waiter robot.")
sleep(.7)
print("As you already know, it is a pre-fixe menu of four (4) items for $20")
sleep(.3)
print("I recommend a beverage, an appetizer, an entree, and a dessert...")
sleep(.3)
print("but by all means feel free to order whatever you like.")
sleep(.5)
print("what would you like as your first item?")
item1=input()
sleep(.3)
print("and then?")
item2=input()
sleep(.3)
print("and then?")
item3=input()
sleep(.3)
print("and then?")
item4=input()
sleep(1)

#get the item prices
print("erm...")
sleep(1)
print("I'm sorry, but none of those items are on the pre-fixe menu.")
sleep(1)
print("You will have to enter the prices manually...")
sleep(.3)
print("how much for the ", item1, "?", sep="")
print("$", end="", sep="")
item1price=input() # EndUser can break this by putting in not-a-number
print("and the ", item2, "?", sep="")
print("$", end="", sep="")
item2price=input() # or a number less than zero
print("and the ", item3, "?", sep="")
print("$", sep="", end="")
item3price=input()
print("and the ", item4, "?", sep="")
print("$", end="", sep="")
item4price=input()

# generate the receipt
print("okey dokey, preparing your receipt")
for x in range(0, 10):
    sleep(.2)
    print(".", end="")

taxRate=.1 # tax rate of 10%
tipRate=.2 # gratuity of 20%

item1price=float(item1price) # theres probably a better way to sanitize these
item2price=float(item2price) # from silly user input
item3price=float(item3price)
item4price=float(item4price)

# number crunch time
subTotal= item1price + item2price + item3price + item4price 
theTax=subTotal*taxRate
theTip=subTotal*tipRate
theTotal=subTotal+theTax+theTip

#and print:
print("")
print(item1, ":", "${:.2f}".format(item1price))
print(item2, ":", "${:.2f}".format(item2price))
print(item3, ":", "${:.2f}".format(item3price))
print(item4, ":", "${:.2f}".format(item4price))
print("subtotal :     ", "${:.2f}".format(subTotal))
print("taxes (10%):   ", "${:.2f}".format(theTax)) 
print("gratuity (%20):", "${:.2f}".format(theTip)) 
print("TOTAL:   >>>   ", "${:.2f}".format(theTotal)) 

