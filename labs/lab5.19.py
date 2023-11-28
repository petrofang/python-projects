'''
5.19 LAB: Brute force equation solver

Numerous engineering and scientific applications 
    require finding solutions to a set of equations. 
Ex: 8x + 7y = 38 and 3x - 5y = -1 
    have a solution x = 3, y = 2. 
Given integer coefficients of two linear equations
    with variables x and y, use brute force to find 
    an integer solution for x and y 
    in the range -10 to 10.

For every value of x from -10 to 10
  For every value of y from -10 to 10
    Check if the current x and y satisfy both equations. 
    If so, output the solution, and finish.

'''
'''Read in first equation, ax + by = c '''
a = int(input())
b = int(input())
c = int(input())

''' Read in second equation, dx + ey = f '''
d = int(input())
e = int(input())
f = int(input())

for x in range (-10,11):
    for y in range(-10,11):
        if (a*x + b*y) == c and (d*x + e*y == f):
            print(f"x = {x} , y = {y}")
            exit()
else: 
    print("There is no solution")
