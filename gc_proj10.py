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

def main():
    debug(DEBUG)
    userInput = None if DEBUG else None

if __name__=="__main__": main()
