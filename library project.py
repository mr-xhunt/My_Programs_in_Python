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
        return self.books.append(name_of_book)
    def lend_book(self, name_of_book, lender):
        self.dict[name_of_book] = lender
        return self.books.remove(name_of_book)

    def return_book(self, name_of_book):
        self.dict.pop(name_of_book)
        return self.books.append(name_of_book)



books = ["The Pshycology of Money", "Intelligent Investor", "Rich Dad Poor Dad", "Cashflow Quadrants", "Shrimad Bhagwat Gita"]
library_1 = Library(books, "library 1")
# x = library_1.disp_book()
# y = library_1.libraryName()
# print(x, y)

# z = library_1.add_book("Python by Musx")
# x = library_1.disp_book()
# print(x)

len = library_1.lend_book("Intelligent Investor", "Mayank")
x = library_1.disp_book()
print(x)
print(library_1.dict)

ret = library_1.return_book("Intelligent Investor")
x = library_1.disp_book()
print(x)
print(library_1.dict)