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

DEBUG = False
def debug(msg): print(f'DEBUG: {msg}') if DEBUG else None

PROMPT="\n>>> "
name=[]
score=[]

def outputAllStudentsAndTheirScores(threshold:float=None) -> None:
    ''' print list of students and scores, optionally above a threshold.'''
    if threshold:
        for i in range(len(name)): 
            if score[i] >= threshold: print(f'{name[i]:<30}: {score[i]:.2f}')
    else: 
        for i in range(len(name)): print(f'{name[i]:<30}: {float(score[i]):.2f}')

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
    # santize by splitting, stripping, and floating it:
    nameAndScore=input(PROMPT).split(',',maxsplit=1)
    nameAndScore[0]=nameAndScore[0].strip()

    try: nameAndScore[1]=float(nameAndScore[1])
    except IndexError: 
        print(f'IndexError - No comma in input: {nameAndScore[0]}')
        return None
    except ValueError: 
        print(f'ValueError - Invalid score: {nameAndScore[1]}')
        return None
    
    # check if they're already on the list:
    if nameAndScore[0].lower() in [x.lower() for x in name]:
        print(f'{nameAndScore[0]} is already on the list.')
        Y=input(f'Would you like to update the score? Y/N{PROMPT}')
        if Y[0].upper()=='Y': 
            # call the update function directly with name and score
            updateIndividualScore(nameAndScore[0], nameAndScore[1])
    else: 
        name.append(nameAndScore[0])
        score.append(nameAndScore[1]) 
        print(f'added [{name[-1], score[-1]}]')
        
def updateIndividualScore(uName:str=None, uScore:float=None):
    '''Update an individual score. Optionally provide index and score to update.'''
   
    if uName==None:
    # if no name is provided in the function call:   
        uName=input(f"what name would you like to update?{PROMPT}")
        uName=uName.strip() 

    # check name the list, case-insensitive comparison:
    try: index=[x.lower() for x in name].index(uName.lower())    
    except ValueError: 
        print(f'"{uName}" not found in score list.')
        return None

    # make we didn't get passed junk arguments somehow...
    try: uScore=float(uScore)   # TypeError if None (good, expected)
    except: uScore=None         # ValueError if bad input (okay, fix)
    while uScore==None:         # now cleaned, so prompt:
    # if no score is provided to the function call, prompt for one:
        print(f"{uName} currently has a score of {score[index]}.")
        uScore=input(f'Enter new score for {uName}:{PROMPT}')
        try: uScore=float(uScore)
        except ValueError:
            print(f"invalid value: '{uScore}'") 
            uScore=None

    print(f"Updating score for {uName} to {uScore}.")
    name[index]=uName
    score[index]=uScore
    
def outputAvgScore(): 
    print(f'Average score: {(sum(score)/len(score)):.2f}')

def outputHighestScorer():
    print(f'The highest scorer is: {name[score.index(max(score))]}')

def outputNamesAndGradesAboveThreshold():
    threshold=input(f"what is the threshold for minimum score to list?{PROMPT}")
    try:threshold=float(threshold)
    except: 
        threshold=None
        debug(f'failed to float(threshold) : {threshold}')
    outputAllStudentsAndTheirScores(threshold)

def main():
    debug(DEBUG)
    userInput = ' ' if DEBUG else ' '
    menuOptions=['E', 'A', 'U', 'V', 'H', 'T']
    while True:
        if userInput[0].upper() == 'Q': quit()
        elif userInput[0].upper() == 'E': enterNameAndScore()
        elif userInput[0].upper() == 'A': outputAllStudentsAndTheirScores()
        elif userInput[0].upper() == 'U': updateIndividualScore()
        elif userInput[0].upper() == 'V': outputAvgScore()
        elif userInput[0].upper() == 'H': outputHighestScorer()
        elif userInput[0].upper() == 'T': outputNamesAndGradesAboveThreshold()
        printMenu()
        userInput=input(PROMPT)

if __name__=="__main__": main()
