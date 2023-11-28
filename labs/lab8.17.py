''' zyBooks Intro to Python 8.17 LAB: Parsing dates

Write a program to read dates from input, one date per line. 
Each date's format must be as follows: March 1, 1990. 
Any date not following that format is incorrect 
and should be ignored. The input ends with -1 on a line alone. 
Output each correct date as: 3/1/1990.

Hint: Use string[start:end] to get a substring 
when parsing the string and extracting the date. 
Use the split() method to break the input into tokens.

Ex: If the input is:
        March 1, 1990
        April 2 1995
        7/15/20
        December 13, 2003
        -1
    then the output is:
        3/1/1990
        12/13/2003
'''

DEBUG=False
def debug(msg): 
    if DEBUG: print(f'DEBUG: {msg}')

def get_month_as_int(monthString):
    monthString=monthString.capitalize()
    if monthString == 'January':
        month_int = 1
    elif monthString == 'February':
        month_int = 2
    elif monthString == 'March':
        month_int = 3
    elif monthString == 'April':
        month_int = 4
    elif monthString == 'May':
        month_int = 5
    elif monthString == 'June':
        month_int = 6
    elif monthString == 'July':
        month_int = 7
    elif monthString == 'August':
        month_int = 8
    elif monthString == 'September':
        month_int = 9
    elif monthString == 'October':
        month_int = 10
    elif monthString == 'November':
        month_int = 11
    elif monthString == 'December':
        month_int = 12
    else:
        month_int = 0
    return month_int

def parse(iDate:str) -> str:
    if len(iDate.split(',')) !=2: return False
    else: 
        iDate=iDate.replace(',','')
        iDate=iDate.split()
        iDate=f"{get_month_as_int(iDate[0])}/{iDate[1]}/{iDate[2]}"
        return iDate
    
def main():
    if DEBUG: ui="March 11, 2018"
    else: ui=input()

    while ui!='-1':
        debug(f'ui: {ui}')
        ui=parse(ui)
        debug(f'ui: {ui}')
        if ui: print(ui)
        ui=input()

if __name__=="__main__": main()
