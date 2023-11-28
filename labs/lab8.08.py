''' zyBooks Intro to Python 8.8 LAB: Mad Lib - loops

Mad Libs are activities that have a person provide various words,
which are then used to complete a short story in unexpected 
(and hopefully funny) ways.

Write a program that takes a string and an integer as input, 
and outputs a sentence using the input values as shown 
in the example below. The program repeats until the input string is quit
and disregards the integer input that follows.
  * Ex: If the input is:
apples 5
shoes 2
quit 0
  * the output is:
Eating 5 apples a day keeps you happy and healthy.
Eating 2 shoes a day keeps you happy and healthy.
'''
uiWord =""
i=0
madTupleList=[]
while uiWord !="quit":
    userInput=input()
    uiList=userInput.split()
    uiWord=uiList[0]
    try:uiNum=int(uiList[1])
    except: uiNum=0
    if uiWord!="quit": madTupleList.append((uiWord, uiNum))
    i+=1

for i in range(len(madTupleList)):
    print(f'Eating {madTupleList[i][1]} {madTupleList[i][0]} a day keeps you happy and healthy.')