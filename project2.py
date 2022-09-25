class Book:
    def __init__(self,Title,Authors,Number_of_copies_available, Number_of_copies_borrowed, Total_number_of_copies):
        self._Title=Title
        self._Authors=Authors
        self._Number_of_copies_available=Number_of_copies_available
        self._Number_of_copies_borrowed=Number_of_copies_borrowed
        self._Total_number_of_copies=Total_number_of_copies

    def getTitle(self):
        return self._Title

    def setTitle(self, value):
        self._Title=value

    def getAuthors(self):
        return self._Authors

    def setAuthors(self, value):
        self._Authors = value

    def getNumber_of_copies_available(self):
        return self._Number_of_copies_available

    def setNumber_of_copies_available(self, value):
        self._Number_of_copies_available = value

    def getNumber_of_copies_borrowed(self):
        return self._Number_of_copies_borrowed

    def setNumber_of_copies_borrowed(self, value):
        self._Number_of_copies_borrowed = value

    def getTotal_number_of_copies(self):
        return self._Total_number_of_copies

    def setTotal_number_of_copies(self, value):
        self._Total_number_of_copies = value

    def __repr__(self):
        print('Title : ',self.getTitle())
        print('-'*100)
        print('Authers : ',self.getAuthors())
        print('Total Number of copies : ',self.getTotal_number_of_copies())
        print('Number of copies available : ',self.getNumber_of_copies_available())
        print('Total Number of copies borrowed : ',self.getNumber_of_copies_borrowed())
        print('_'*100)

class Library:
    def __init__(self):
        self.books = []

    def Add_book(self,value):
        self.books.append(value)

    def Remove_book(self,value):
        flag = 0
        for book in self.books:
            if book.getTitle() == value:
                self.books.remove(book)
                flag = 1
                break
        if flag == 0:
            print("this book is already not exist")

    def Borrow_book(self,value):
        flag = 0
        for book in self.books:
            if book.getTitle()==value :
                if book.getNumber_of_copies_available() > 0:
                    book.setNumber_of_copies_available(book.getNumber_of_copies_available()-1)
                    book.setNumber_of_copies_borrowed(book.getNumber_of_copies_borrowed()+1)
                else : print("This book is no longer available")
                flag = 1
                break
        if flag == 0 :
            print("We don't have this book in the library")

    def Return_book(self,value):
        flag =  0
        for book in self.books:
            if book.getTitle()==value :
                if book.getNumber_of_copies_borrowed()>0:
                    book.setNumber_of_copies_available(book.getNumber_of_copies_available() + 1)
                    book.setNumber_of_copies_borrowed(book.getNumber_of_copies_borrowed() - 1)
                    flag = 1
                break
        if flag == 0 :
            print("This book is not borrowed from here")

    def Search_for_book(self,value):
        flag=0
        for book in self.books:
            if book.getTitle()==value :
                print("HERE")
                book.__repr__()
                flag=1
                break
        if flag==0:
            print("NOT HERE")

    def __repr__(self):
        for book in self.books:
            book.__repr__()

def Add(library):
    x = int(input('Enter number of books you want to add to the library : '))
    for i in range(x):
        title = input('inter the title of book ' + str(i + 1) + ' : ')
        noOfAuthors = int(input('Enter the number of Authers of book ' + title + ' : '))
        Authers = []
        for j in range(noOfAuthors):
            s = input('Enter Auther ' + str(j + 1) + ' : ')
            Authers.append(s)
        Number_of_copies_available = int(input('Enter the number of copies avialable of book ' + title + ' : '))
        Number_of_copies_borrowed = int(input('Enter the number of copies borrowed of book ' + title + ' : '))
        Total_number_of_copies = Number_of_copies_available + Number_of_copies_borrowed
        book = Book(title, Authers, Number_of_copies_available, Number_of_copies_borrowed, Total_number_of_copies)
        library.Add_book(book)

def Remove(library):
    x = int(input('Enter number of books you want to remove from the library : '))
    for i in range(x):
        book=input('Enter the titel of the '+str(i+1)+' book you want to delete : ')
        library.Remove_book(book)

def Borrow(library):
    x = int(input('Enter number of books you want to borrow from the library : '))
    for i in range(x):
        book = input('Enter the titel of the ' + str(i + 1) + ' book you want to borrow : ')
        library.Borrow_book(book)

def Return(library):
    x = int(input('Enter number of books you want to return to the library : '))
    for i in range(x):
        book = input('Enter the titel of the ' + str(i + 1) + ' book you want to return : ')
        library.Return_book(book)

def Search(library):
    x = int(input('Enter number of books you want to search in the library : '))
    for i in range(x):
        book = input('Enter the titel of the ' + str(i + 1) + ' book you want to search : ')
        library.Search_for_book(book)

library=Library()

while True:
    print('Enter number of what do you want  : ')
    print(' 1 : Add books ')
    print(' 2 : Remove books ')
    print(' 3 : Borrow books ')
    print(' 4 : Return books ')
    print(' 5 : Search for books ')
    print(' 6 : Exit ')
    num=int(input('Number = '))
    if(num == 1):
        Add(library)
    elif(num == 2):
        Remove(library)
    elif (num == 3):
        Borrow(library)
    elif (num == 4):
        Return(library)
    elif (num == 5):
        Search(library)
    elif (num == 6):
        break

library.__repr__()