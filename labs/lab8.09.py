''' zyBooks Intro to Python 8.9 LAB: Palindrome

A palindrome is a word or a phrase that is the same when read 
both forward and backward. Examples are: "bob," "sees," or 
"never odd or even" (ignoring spaces). Write a program whose 
input is a word or phrase, and that outputs whether the input 
is a palindrome.

Hint: Start by removing spaces. 
Then check if the string equals itself in reverse.
'''

DEBUG=False
def db(msg:str): 
    if DEBUG==True: print(msg)

not_a_=''
w=input()
db(w)
u=w.split()
db(u)
v=''.join(u)
db(v)
db(v[::-1])
if v[::-1]!=v:not_a_='not a '
print(f'{not_a_}palindrome: {w}')