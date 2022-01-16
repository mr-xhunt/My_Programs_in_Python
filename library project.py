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
    def __init__(self, book_list, library_name):
        self.book_list = book_list
        self.library_name = library_name
        self.lend_record = {}

    def display_book(self):
        print(self.book_list) 

    def add_book(self):
        book = input("Enter book name : ").capitalize()
        if book == "" or " ":
            print("Invalid Book name!")
        else:
            self.book_list.append(book)   

    def lend_book(self):
        book = input("Enter book name : ").capitalize()
        if book not in self.book_list:
            print("Please enter valid input")
        if book in self.book_list:
            name = input("Enter your name : ")
            self.book_list.remove(book)   
            self.lend_record[book] = name            
        else:
            if self.lend_record.get(book):
                print(f"Book does not exist in library this book taken by {self.lend_record[book]}")

    def return_book(self):
        book = input("Enter book name : ").capitalize()
        if book in self.lend_record:
            self.book_list.append(book)      
            del self.lend_record[book]
        else:
            print("Please enter valid input")             

if __name__=='__main__':
    book_list = ['C++','Java','JavaScript','Python','Ruby','Pearl']
    library = Library(book_list, 'library')

    while True:
        user = input("\nD for Display book, A for Add book, L for lend book, R for return book, and Q for exit :")
        if user == "Q" or user == "q":
            break
        elif user == "display" or user == "d" or user == "D":
            library.display_book()
        elif user == "add" or user == "a" or user == "A":
            library.add_book()
        elif user == "lend" or user == "l" or user == "L":
            library.lend_book()
        elif user == "return" or user == "r" or user == "R":
            library.return_book()
        
