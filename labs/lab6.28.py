''' 6.28 LAB: Output values in a list below a user defined amount - functions

Write a program that first gets a list of integers from input. 
The input begins with an integer indicating the number of integers 
that follows. Then, get the last value from the input, and 
output all integers less than or equal to that value.

Such functionality is common on sites like Amazon, 
where a user can filter results. Utilizing functions 
will help to make your main very clean and intuitive.

The program must define the following two functions:
def get_user_values():  read from input the size of the list, 
                        the integers in the list, and the 
                        threshold value. Return the list of 
                        integers and the threshold value.

def ints_less_than_or_equal_to_threshold(user_values, upper_threshold):
                        create a new list that contains values 
                        in user_values that are less than or equal to 
                        upper_threshold. Return the newly created list.
'''
# Define your functions here
def get_user_values() -> tuple[list, int]: 
    iNum=int(input())
    iList=[]
    for i in range(iNum):
        iList.append(int(input()))
    iMax=int(input())
    return (iList, iMax)


def ints_less_than_or_equal_to_threshold(user_values, upper_threshold) -> list:
    newList=[]
    for i in range(len(user_values)):
        if user_values[i] <= upper_threshold:
            newList.append(user_values[i])
    return newList


if __name__ == '__main__':
    user_values, upper_threshold = get_user_values()
    res_values = ints_less_than_or_equal_to_threshold(user_values, upper_threshold)
    
    for value in res_values:
        print(value)
