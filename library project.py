#create library class
#   display book
#   lend book          who owns book if not available
#   add book
#   return book
#HarryLibrary = Library(listofbooks, library_name)

#dictionary (books-nameofperson)

# create a main function and run a infinte while loop
# asking users for their input



class Library:
    def __init__(self, listofbooks, libraryname):
        self.books = listofbooks
        self.lname = libraryname
        self.dict = {}
    def disp_book(self):
        return self.books
    def libraryName(self):
        return self.lname
    def add_book(self, name_of_book):
        for item in self.books:
            if name_of_book == item:
                print("This book is already present in the library!")
            else:
                return self.books.append(name_of_book)
    def lend_book(self, name_of_book, lender):
        self.dict[name_of_book] = lender
        return self.books.remove(name_of_book)

    def return_book(self, name_of_book):
        self.dict.pop(name_of_book)
        return self.books.append(name_of_book)



books = ["The Pshycology of Money", "Intelligent Investor", "Rich Dad Poor Dad", "Cashflow Quadrants", "Shrimad Bhagwat Gita"]
library_1 = Library(books, "library 1")

while True:
    usrinp = input("What do you wish to do?\n1.Display Book\n2.Lend Book \n3.Add Book\n4.Return Book\n\n:")

    if usrinp == "display":
        x = library_1.disp_book()
        y = library_1.libraryName()
        print(x, y)
    elif usrinp == "add":
        z = library_1.add_book(input("Which book do you wish to add?\n"))
    elif usrinp == "lend":
        bookname = input("Which book do you wish to lend?\n")
        Pname = input("What is your Name: ")
        len = library_1.lend_book(bookname,Pname)
    elif usrinp == "return":
        ret = library_1.return_book(input("Which book do you wish to return?\n"))
    else:
        print("Invalid Operation")




