''' 6.20 LAB: Driving costs - functions

Write a function driving_cost() with input parameters 
miles_per_gallon, dollars_per_gallon, and miles_driven, 
that returns the dollar cost to drive those miles. 
All items are of type float. The function called with 
arguments (20.0, 3.1599, 50.0) returns 7.89975.

Define that function in a program whose inputs are 
the car's miles per gallon and the price of gas 
in dollars per gallon (both float). 

Output the gas cost for 10 miles, 50 miles, and 400 miles, 
by calling your driving_cost() function three times.
'''

def driving_cost(miles_per_gallon: float, dollars_per_gallon: float, miles_driven: float) -> float:
    gallons = miles_driven / miles_per_gallon
    dollars = dollars_per_gallon * gallons
    return dollars

if __name__ == '__main__':
    mpg=float(input())
    cost=float(input())
    print(f'{driving_cost(mpg,cost,10):.2f}')
    print(f'{driving_cost(mpg,cost,50):.2f}')
    print(f'{driving_cost(mpg,cost,400):.2f}')
