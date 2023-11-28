''' zyBooks Introduction to Python 4.17 LAB: Seasons

Write a program that takes a date as input and outputs the date's season 
in the northern hemisphere. The input is a string to represent the month 
and an int to represent the day.

Ex: If the input is:
April
11

the output is:
Spring

In addition, check if the string and int are valid (an actual month and day).

Ex: If the input is:
Blue
65

the output is:
Invalid 

The dates for each season in the northern hemisphere are:
Spring: March 20 - June 20
Summer: June 21 - September 21
Autumn: September 22 - December 20
Winter: December 21 - March 19

'''
month = input()
day = int(input())
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
season="Invalid"

if month not in MONTHS: season="Invalid"
elif day > 31 or day < 1: season="Invalid"
elif month == "January" or month == "February" : season = "Winter"
elif month == "October" or month == "November" : season = "Autumn"
elif month == "April" or month == "May"        : season = "Spring"
elif month == "July" or month == "August"      : season = "Summer"
elif month == "March": 
    if day >= 20: season = "Spring"  
    else: season = "Winter"
elif month == "June": 
    if day > 20: season = "Summer"  
    else: season = "Spring"
elif month == "September": 
    if day > 30: season = "Invalid"
    elif day > 21: season = "Autumn"  
    else: season = "Summer"
elif month == "December": 
    if day > 20: season = "Winter" 
    else: season = "Autumn"
print(season)
    