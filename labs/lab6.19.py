''' 6.19 LAB: Max magnitude
 Write a function max_magnitude() with three integer
 parameters that returns the largest magnitude value. 
 Use the function in the main program that takes 
 three integer inputs and outputs the largest magnitude value. 
'''

def max_magnitude(user_val1, user_val2, user_val3):
    nList=[0, user_val1, user_val2, user_val3]
    for i in range(1,4):
 #      print(f"if abs({nList[i]}) < abs({nList[i-1]}):")
        if abs(nList[i]) < abs(nList[i-1]):
 #          print("(it is)")
            nList[i]=nList[i-1]
 #          print(f"nList[{i}]={nList[i-1]}")
            
        else:
            pass
 #          print("(it is not)")
    return nList[3]

if __name__ == '__main__':
    x,y,z=int(input()),int(input()),int(input())
    print(max_magnitude(x,y,z))