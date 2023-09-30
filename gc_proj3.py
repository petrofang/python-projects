""" Intro to Python: Programming Project Week 3

This project gives you practice with one of the simplest sequences, 
the list.  Be sure to watch the lecture on how to create a list, 
append to a list and work with a list using indices 
and available functions prior to starting this project.

Mrs. Green has a class with 5 students.  Typically when she 
administers an exam to her students, she is not only interested in
the individual student grades, but is also interested in 
entire class grade characteristics.  In particular, Mrs. Green is 
interested in the mean grade and the grade range. 

The mean of a list of numbers is the sum of all the numbers, 
divided by the quantity of numbers there were.  For example, 
to calculate the mean of the three numbers  
15, 25, 20  =>   15+25+20 = 60 / 3  => 20

The range of a list of numbers is the different between the largest 
and smallest numbers in the list.  For example, the range of 
the five numbers  11, 35,  20, 5,  15  would be 35 - 5 => 30

You are to write a Python program which:

* allows the user to enter 5 exam scores

* the scores are to be placed in a list 
(you can input each of the scores and then create the list 
OR create a new list and then append each score to an existing list)

* print out the scores you have stored in the list, ONE SCORE PER LINE

* ask the user  how much the scores are to be curved 
(ie. how much she is willing to add to all scores)  
and UPDATE  THE SCORES IN THE LIST to reflect is amount  
(for example if the scores are to be curved by 5 points, 
a list containing [  80, 80, 75, 90, 81]  will be updated 
to contain [ 85, 85, 80, 95, 86 ]

* print out the scores you now have in the list, ONE PER LINE

* calculate and print out the mean of the scores stored in the list

* determine and print out the range of the scores stored in the list

HINT:  Indices (eg. x[2]) access individual list values,   
list functions sum,  min and max can help you calculate the mean and range. 
"""

# Intro to Python Project 3
# Exam score calculator
# by Giles Cooper
# now 300% loopier

print("input exam scores (5):")
scores = [int(input("1: ")), int(input("2: ")), int(input("3: ")), int(input("4: ")), int(input("5: "))]

# print the scores
print("\nExam scores (raw):")
for x in range(len(scores)):
    print(scores[x])
    
curve = int(input("How many points to curve?\n> "))
# curve and print the scores 
for x in range(len(scores)):
    scores[x] = scores[x] + curve
    
print("\nExam scores (curved):")
for x in range(len(scores)):
    print(scores[x])
    
meanScore=sum(scores)/len(scores) # get the average and express min and max to output
print("The average score is ", meanScore, "%. Scores range from ", min(scores), " to ", max(scores), ".", sep='')
