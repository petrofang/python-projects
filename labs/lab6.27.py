''' 6.27 LAB: Multiples of ten in a list

Write a program that reads a list of integers, and outputs 
    whether the list contains all multiples of 10, 
    no multiples of 10, or mixed values. 

Define a function named is_list_mult10 that takes a list 
    as a parameter, and returns a boolean that represents 
    whether the list contains all multiples of ten. 

Define a function named is_list_no_mult10 that takes a list 
    as a parameter and returns a boolean that represents whether 
    the list contains no multiples of ten.

Then, write a main program that takes an integer, 
    representing the size of the list, followed by the list values. 
    The first integer is not in the list.

The program must define and call the following two functions. 
is_list_mult10():       returns true if all integers in the list 
                        are multiples of 10 and false otherwise. 
is_list_no_mult10():    returns true if no integers in the list 
                        are multiples of 10 and false otherwise.
'''
# Define your functions here
def is_list_mult10(my_list: list) -> bool:
    all10s=True
    i=0
    while (all10s==True) and (i < len(my_list)):
        if (my_list[i] % 10): all10s=False
        i+=1
    return all10s

def is_list_no_mult10(my_list: list) -> bool:
    no10s=True
    i=0
    while (no10s==True) and (i < len(my_list)):
        if not (my_list[i] % 10): no10s=False
        i+=1
    return no10s

if __name__ == '__main__':
    # Type your code here.
    count = int(input()) 
    array=[]
    for i in range(count):
        array.append(int(input())) 
    if is_list_no_mult10(array): print("no multiples of 10")
    elif is_list_mult10(array): print("all multiples of 10")
    else: print("mixed values")
        
