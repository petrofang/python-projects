''' 6.21 LAB: Step counter

A pedometer treats walking 1 step as walking 2.5 feet. 
Define a function named feet_to_steps that takes a float 
as a parameter, representing the number of feet walked, 
and returns an integer that represents the number of 
steps walked. Then, write a main program that reads the 
number of feet walked as an input, calls function 
feet_to_steps() with the input as an argument, and 
outputs the number of steps as an integer.

Use floating-point arithmetic to perform the conversion.
'''

def feet_to_steps(feet: float) -> int: return int(feet / 2.5)
if __name__ == '__main__': print(feet_to_steps(float(input())))
