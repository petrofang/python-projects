''' Intro to Python, Project 12: Classes & Objects

    PART I
Define a class named LibraryBook that has the following instance variables:
    title - name of the book
    year - copyright date
    author - author of the book
    num_owned  -  number of copies owned by the library
    num_on_shelf - number of copies currently on shelf   
                   (ie some may have been borrowed)

The class should provide the following methods:
  * an __init__ method which accepts 6 parameters, self plus one parameter 
    to initialize each of the 5 instance variables when an object is created
  * a method to print out an object of type Library Book 
  * a method,  borrow() which updates the number of copies on the shelf
  * a method, returned() which updates the  number of copies on the shelf 

    PART II
Your main process is to verify that the LibraryBook class works correctly 
    by doing the following:
  * Create a library book object 
  * Allow the user to repeat any of the following until he/she wishes to exit:
  * Borrow the book, if the book is available, otherwise print a message
  * Return the book
  * Print out all current information on the book 
'''
# Giles Cooper, Nov 2023
PROMPT='>>> '

def welcome():
    print(f'\n{"="*75}\nWelcome to Library of One-Book Reading, Actively Restocked Yearly (L1BRARY)\n')

class LibraryBook:
    ''' I wonder if it would technically make sense to create each book as
        its own subclass of LibraryBook, and then the individual copy of
        each book is represented by an instantiated object of that class...

        class Book(LibraryBook):
            def __init__(self, title, author, etc):
                super().__init__(title, author, etc)
            def returned(self):num_on_shelf+=1 # not self().num_on_shelf
            def borrow(self):num_on_shelf-=1
        
        class Moby_Dick(LibraryBook):
            def __init__(self, title="Moby Dick", author="Melville", etc):
                super().__init__(title, author, etc)
            def returned(self):num_on_shelf+=1 # not self().num_on_shelf
            def borrow(self):num_on_shelf-=1
            
        Of course, it would be a bear to encode every single book, but...
        I can't be bothered to read in depth on StackOverflow.com right now,
        but I think we can use type() to create new classes during runtime.
    '''

    def __init__(self, title:str, author:str, year:int, num_owned=1, num_on_shelf=-1):
        self.title=title
        self.author=author
        self.year=year
        self.num_owned=max(0,num_owned) # no negative numbers please
        self.num_on_shelf=num_owned if num_on_shelf==-1 else num_on_shelf
        # assume all copies of newly instantiated LibraryBook are on shelf U.O.S.
    
    def print_info(self):
        for key, val in self.__dict__.items():
            print(f'{key:<15}: {val}')

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return f'{self.author}: {self.title} ({self.year})\nowned: {self.num_owned}, on shelf: {self.num_on_shelf}'

    def borrow(self):
        ''' we might have had this function return the book object or None, thus:\n
moby_dick=LibraryBook('moby dick', 'melville', etc)\n
book_I_am_borrowing = moby_dick.borrow()\n
then each borrowed book is a reference to the book which is an instantiation of LibraryBook 
(no subclass needed) '''
        if self.num_on_shelf > 0:
            self.num_on_shelf -=1
            print(f'You borrow {self}. {self.num_on_shelf} more copies remain.')
            # return self
        
        elif self.num_on_shelf==0:
            print(f'{self} is not available.', end=' ')
            print(f'All copies ({self.num_owned}) are already borrowed.')
            # return None
        
        elif self.num_on_shelf < 0: raise ValueError(self.num_on_shelf) 
        # if we're here, there's a problem
    
    def returned(self):
        if self.num_on_shelf < self.num_owned:
            self.num_on_shelf+=1
            print(f'{self} has been returned to the shelf.')
        elif self.num_on_shelf == self.num_owned:
            # looks like someone 'returned' an extra book
            self.num_on_shelf+=1
            self.num_owned+=1
            print(f'Thank you for your donation of {self}')
        print(f'There are ({self.num_on_shelf} / {self.num_owned}) now available.')
        if self.num_on_shelf > self.num_owned: # oops how did this happen?
            raise ValueError(self, self.num_on_shelf, self.num_owned)
    
        

def main():
    the_alchemist=LibraryBook('The Alchemist', "Paulo Coelho", 1988)
    book=the_alchemist
    welcome()
    while True:
        print_menu()
        option=input(PROMPT)[0]
        if option=='1':book.borrow()
        if option=='2':book.returned()
        if option=='3':print(book.__repr__())
        if option.upper()=='Q':quit()


def print_menu():
    print('--- OPTIONS MENU ---')
    print(' 1 ) borrow the book')
    print(' 2 ) return the book')
    print(' 3 ) get book info')
    print(' Q ) quit this program')

if __name__=='__main__': main()

