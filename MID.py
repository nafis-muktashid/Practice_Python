#Task - 01
class Library:
    book_list = []
    
    def entry_book(self, bookObj):
        self.book_list.append(bookObj)


#Task - 02, 04, 05, 06, 08, 09
class Book:
    def __init__(self, book_id, title, author, availability):
        self._book_id = int(book_id)
        self.__title = title
        self.__author = author
        self.__availability = availability

    def get_ID(self):
        return self._book_id

    def borrow_book(self):
        if(self.__availability == True):
            self.__availability = False
        else:
            print("This book is not available")
    
    def return_book(self):
        if(self.__availability == False):
            self.__availability = True
        else:
            print("This book is already available")
    
    def view_book_info(self):
        print(f"Book ID: {self._book_id},\tBook Title: {self.__title},\tBook Author: {self.__author},\tBook Availability: {self.__availability}")

#Task - 03
bookObj_1 = Book(1001, "Book Name", "Book Author", True)
bookObj_2 = Book(1002, "Book Name Part II", "Book Author", False)
Library_Of_All_Books = Library()
Library_Of_All_Books.entry_book(bookObj_1)
Library_Of_All_Books.entry_book(bookObj_2)


# Task - 07, 08
print("------------Welcome to the Library----------------")
def home():
    print("")
    print("1. View All Books")
    print("2. Borrow Books")
    print("3. Return Books")
    print("4. Exit")
    print("Enter a number: ")

home()
opt = int(input())

while(opt != 4):

    if(opt == 1):
        for book in Library_Of_All_Books.book_list:
            book.view_book_info()
        home()
    elif(opt == 2):
        print("Give the Book_ID to Borrow")
        flag = False
        bID = int(input())
        for book in Library_Of_All_Books.book_list:
            if(book.get_ID() == bID):
                book.borrow_book()
                flag = True
                break
            else:
                flag = False

        if(flag == False):
            print("No Book Found with that Book_ID")
        home()
    elif(opt == 3):
        print("Give the Book_ID to Return")
        flag = False
        bID = int(input())
        for book in Library_Of_All_Books.book_list:
            if(book.get_ID() == bID):
                book.return_book()
                flag = True
                break
            else:
                flag = False
        
        if(flag == False):
            print("No Book Found with that Book_ID")
        home()
    else:
        print("Enter a valid Option")
    opt = int(input())

print("------------Thanks for using the Library----------------")










