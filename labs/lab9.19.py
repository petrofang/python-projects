''' zyBooks Intro to Python 9.19 LAB: Varied amount of input data

Statistics are often calculated with varying amounts of input data. 
Write a program that takes any number of non-negative floating-point 
numbers as input, and outputs the max and average, respectively.

Output the max and average with two digits after the decimal point.
Ex: If the input is:
        14.25 25 0 5.75
    the output is:
        25.00 11.25
'''

DEBUG=False
def debug(msg): print(f'DEBUG: {msg}') if DEBUG else None

def main():
    user_input:str = "14.25 25 0 5.75" if DEBUG else input()
    user_input=user_input.split()
    user_input=[float(x) for x in user_input]
    uMax=max(user_input)
    uMean=sum(user_input)/len(user_input)
    print(f'{uMax:.2f} {uMean:.2f}')

if __name__=="__main__": main()