''' Introduction to Python: Project 11

by Giles Cooper

Mystery Night Dinner can accept 50 reservations. You are to write a 
program which keeps track of customer reservations for Mystery Night Dinner.

The Application

The main program is to a dictionary to store reservation data. Each 
dictionary item will be of the form name:quantity, where the name is 
the purchaser and the quantity is the number of tickets they purchased. 
For example, the dictionary might look like:
    { 'Sally Jones': 4 , 'Bob Smith', 2 }

The application should allow the user to do one of 4 things, until 
they wish they wish to exit:
  * add customer name to the reservation list. The user is to provide
    the customer name and the number of reservations desired. If the 
    reservation list is full (already has 50 items), or this reservation 
    will make the list full (total already on list + number of
    reservations desired) a message is to be output and no reservation made.

  * the user can provide a customer name and find out if that customer 
  already has a reservation. If they have a reservation, the quantity 
  reserved should be output.

  * print the names and quantities of all customers who have reservations

  * print the total number of reservations made so far

BE SURE that your program INCLUDES at least one function definition.

Submit the file containing your completed program. This file should be 
named Mystery.py. Be sure your program is well-commented and well-tested.    
'''
DEBUG=False
def debug(msg) -> None: print(f'DEBUG: {msg}') if DEBUG else None

MAX_RESERVATIONS = 50
PROMPT = "\n>>> "
reservations = {}

def MakeReservation():
    # TODO
    
    pass

def CheckReservation():
    reservationName=input("What name do you want to check for reservation?" + PROMPT)
    if reservationName in reservations.keys:
        print(f'{reservationName} has a reservation for {reservations[reservationName]}')

def PrintReservationList():
    # FIXME: make better
    print(reservations)

def PrintNumberReservations():
    totalReservations=sum([int(each) for each in reservations.values()])
    print(f"Total reservations already made: {totalReservations} out of {MAX_RESERVATIONS}.")

def PrintOptionMenu():
    print(" 1 ) Make a reservation")
    print(" 2 ) Check for a reservation")
    print(" 3 ) Print reservation list")
    print(" 4 ) Print total number of reservations so far")
    print(" Q ) Quit this program")

def main():
    debug(DEBUG)
    userOption=""
    while True:
        PrintOptionMenu()
        userOption=input(PROMPT)
        if userOption == "1": MakeReservation()
        if userOption == "2": CheckReservation()
        if userOption == "3": PrintReservationList()
        if userOption == "4": PrintNumberReservations()
        if userOption.upper() == "Q": quit()

if __name__=="__main__": main()