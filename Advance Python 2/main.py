class Library:
    def __init__(self,listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books:
            print(' ',book)
    
    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it 30 Days.")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book is either not available or it has already been issued to someone else. Please wait untill the book is available.")
            return False

    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thanks for returning this book. Hope you enjoyed reading it. Have a great day ahead")
class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book



if __name__=="__main__":
    centralLibrary = Library(['django','python','Algorithms','clrs','pythonNotesByHarry'])
    # centralLibrary.displayAvailableBooks()
    student = Student()
    while True:
        welcomeMsg = '''\n=======Welcome to Central Library=====
        =>Please choose an option: 
        1 Listing all the books
        2 Request a book
        3 Add/Return a book
        4 Exit the library'''
        print(welcomeMsg)
        
        a = int(input("Enter your option: "))
        if a==1:
            centralLibrary.displayAvailableBooks()
        elif a==2:
            centralLibrary.borrowBook(student.requestBook())
        elif a==3:
            centralLibrary.returnBook(student.returnBook())
        elif a==4:
            print("Thanks for choosing Central library! Have a great day ahead.")
            exit()
        else:
            print("Invalid Choice!")
