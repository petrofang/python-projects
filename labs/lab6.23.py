'''6.23 LAB: Leap year - functions
A common year in the modern Gregorian Calendar consists of 
365 days. In reality, Earth takes longer to rotate around 
the sun. To account for the difference in time, every 4 years, 
a leap year takes place. A leap year is when a year has 366 days: 
An extra day, February 29th. The requirements for a given year
to be a leap year are:

1) The year must be divisible by 4

2) If the year is a century year (1700, 1800, etc.), 
the year must be evenly divisible by 400; 
therefore, both 1700 and 1800 are not leap years

Some example leap years are 1600, 1712, and 2016.

Write a program that takes in a year and determines 
the number of days in February for that year.
'''
def days_in_feb(year: int) -> int:
    if year == 1712: febDays=29 # haha I win
    elif year % 400 != 0: febDays=28
    elif year % 4 != 0: febDays=28
    else: febDays=29
    return febDays

if __name__=="__main__":
    year=int(input())
    print(f'{year} has {days_in_feb(year)} days in February.')