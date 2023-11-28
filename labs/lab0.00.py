''' zyBooks Intro to Python 

'''

DEBUG=True
def debug(msg): print(f'DEBUG: {msg}') if DEBUG else None

def main():
    debug(DEBUG)
    userInput = None if DEBUG else None

if __name__=="__main__": main()
