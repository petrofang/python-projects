'''
5.21 LAB: Adjust values in a list by normalizing

When analyzing data sets, such as data for human heights 
    or for human weights, a common step is to adjust the data. 
This adjustment can be done by normalizing to values 
    between 0 and 1, or throwing away outliers.

For this program, adjust the values by dividing all values 
    by the largest value. The input begins with an integer 
    indicating the number of floating-point values that follow.

Output each floating-point value with two digits after the decimal 
    point, which can be achieved as follows:
        print(f'{your_value:.2f}')
'''

i=int(input())
max=0.0
flist=[0] * i
while i>0:
    i-=1
    flist[i]=float(input())
 #   print(flist)

    if flist[(i)] > max: max = flist[i] 
    
else:
    for j in range(0,len(flist)):
        flist[j] = flist[j]/max
        print(f'{j:.2f}')
        # FIXME: this list is reversed