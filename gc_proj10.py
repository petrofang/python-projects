'''Intro to Python: Programming Project Week 10

You are to write a program that allows the user to choose 
any of the following options, until the user wants to exit:

Enter a name and associated score  
  * (if the name is stored in names[4], the score should be in score[4])
        It would be a good idea to store the name in all 
        lower or upper case to make later searching easier
  * Output all students and their scores
  * Update a particular student's score (user input's student name)
  * Output the average of all scores
  * Output the name of the student with the highest score
  * Output the names and grades of all students where grades are 
        above a particular threshold (threshold input by user)

YOUR program should include and use AT LEAST TWO function definitions.

Be sure that your program is well-commented so that it is easily read.  
Also be sure that all input prompts are well-worded so that the user 
knows what is expected.  Output values should be labeled so that 
it is clear what results are being printed.

Submit the .py file(s) containing your working program.  
(Don't worry about submitting a run, I will execute your program myself).
'''

DEBUG = True
def debug(msg): print(f'DEBUG: {msg}') if DEBUG else None

PROMPT=" > "
name=[]
score=[]

def outputAllStudedentsAndTheirScores(name: list, score:list) -> None:
    for i in range(len(name)):
        print(f'{name[i].capitalize()}: {float(score[i]):.1f}')

def printMenu():
    '''print the options menu.'''
    print(f' +----------  MENU  ----------+')
    print(f' |  (E)nter a name and score')
    print(f' |  (A)ll students and scores')
    print(f' |  (U)pdate a student\'s score')
    print(f' | a(V)erage of all scores')
    print(f' |  (H)ighest scorer')
    print(f' |  (T)hreshold-or-higher scores')
    print(f' |  (Q)uit this program')
    print(f' +----------------------------+')
    
def enterNameAndScore():
    print('enter a name and score, seperated by a comma')
    nameAndScore=input(PROMPT).split(',')
    name.append(nameAndScore[0].capitalize())
    try: 
        score.append(float(nameAndScore[1])) 
        print(f'added {nameAndScore}')
    except:
        print(f'error: failed to add {nameAndScore}')

def updateIndividualScore():
    pass # TODO: finish stub

def outputAvgScore():
    print(f'Average score: {(sum(score)/len(score))}')

def outputHighestScorer():
    pass # TODO: finish stub

def outputNamesAndGradesAboveThreshold():
    pass # TODO: finish stub


def main():
    debug(DEBUG)
    userInput = ' ' if DEBUG else ' '
    menuOptions=['E', 'A', 'U', 'V', 'H', 'T']
    while True:
        if userInput[0].upper() == 'Q': quit()
        elif userInput[0].upper() == 'E': enterNameAndScore()
        elif userInput[0].upper() == 'A': outputAllStudedentsAndTheirScores(name, score)
        elif userInput[0].upper() == 'U': updateIndividualScore()
        elif userInput[0].upper() == 'V': outputAvgScore()
        elif userInput[0].upper() == 'H': outputHighestScorer()
        elif userInput[0].upper() == 'T': outputNamesAndGradesAboveThreshold()
        printMenu()
        userInput=input(PROMPT)

if __name__=="__main__": main()
