'''6.22 LAB: A jiffy

In computer animation, a "jiffy" is commonly defined
 as 1/100th of a second. Define a function named 
 jiffies_to_seconds that takes the number of "jiffies" 
 as a parameter, and returns the number of seconds. 
 Then, write a main program that reads the number of 
 jiffies (float) as an input, calls function 
 jiffies_to_seconds() with the input as argument, 
 and outputs the number of seconds.

Output each floating-point value with three digits
 after the decimal point, which can be achieved as follows:
print(f'{your_value:.3f}')
'''
def jiffies_to_seconds(jifs: float) -> float: return jifs / 100
if __name__ == '__main__': print(f'{jiffies_to_seconds(float(input())):.3f}')