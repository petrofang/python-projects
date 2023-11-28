''' zyBooks Intro to Python 8.16 LAB: Midfix of 

The midfix of 5 is the middle five characters of a string. 
Given a string input, output the middle five characters of 
that string with a new line at the end. Assume the string 
length is always odd and at least five characters.

Ex: If the input is:
        xxxplanexxx
    the output is:
        Midfix: plane
'''

DEBUG=False
def debug(msg): 
    if DEBUG: print(f'DEBUG: {msg}')

def main():
    if DEBUG:   ui = "xxxplanexxx"
    else:       ui = input()

    while len(ui) > 6: ui=ui[1:-1]
    print(f"Midfix: {ui}")


if __name__=="__main__": main()
