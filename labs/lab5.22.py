''' 5.22 LAB: Output values in a list below a user defined amount

Write a program that first gets a list of integers from input. 
The input begins with an integer indicating the number of integers 
that follow. Then, get the last value from the input, which 
indicates a threshold. Output all integers less than or equal 
to that last threshold value.
'''

numberList=[]
iterations=int(input())
for i in range(0,iterations):
    numberList.append(int(input()))
userMax=int(input())
for i in range(0,iterations):
    if numberList[i] <= userMax:
        print(numberList[i], end=",")
        
    