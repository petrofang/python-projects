'''
5.17 LAB: Output range with increment of 5

Write a program whose input is two integers. 
Output the first integer and subsequent 
increments of 5 as long as the value is 
less than or equal to the second integer.
'''

a,b = int(input()), int(input())
if a > b:
    print("Second integer can't be less than the first.")
else: 
    while a<=b:
        print(a, end=" ")
        a+=5
    print()
    