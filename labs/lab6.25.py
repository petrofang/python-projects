''' 6.25 LAB: Swapping variables

Define a function named swap_values that takes four integers 
as parameters and swaps the first with the second, and the 
third with the fourth values. Then write a main program that 
reads four integers from input, calls function swap_values() 
to swap the values, and prints the swapped values on a single 
line separated with spaces.

The program must define and call the following function.
def swap_values(user_val1, user_val2, user_val3, user_val4):
'''

# Define your function here.
def swap_values(user_val1, user_val2, user_val3, user_val4):
    return user_val2, user_val1, user_val4, user_val3


if __name__ == '__main__': 
    v1, v2, v3, v4 = 1,2,3,4
    try: v1, v2, v3, v4 = int(input()), int(input()), int(input()), int(input())
    except TypeError: pass
    except: raise
    v=list(swap_values(v1, v2, v3, v4))
    for n in range(3): print(f"{v[n]} ", end="")
    print(f"{v[3]}")
