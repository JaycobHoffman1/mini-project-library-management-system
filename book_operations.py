from error_handling import ErrorHandler as e
from book import Book as b
from user_operations import UserOperations as u

class BookOperations:
    def __init__(self):
        self.__error_handling = e()
        self.__isbn_pattern = r"\d{3}-\d{4}-\d{4}-\d-\d$"
        self.__publication_date_pattern = r"(\d{2}/){2}\d{4}$"
        self.__books = {} # stores "Book.get_title()" as key and "Book" object as value

    def get_e(self):
        return self.__error_handling
    
    def get_isbn_pattern(self):
        return self.__isbn_pattern
    
    def get_publication_date_pattern(self):
        return self.__publication_date_pattern
    
    def get_books(self):
        return self.__books
    
    def set_e(self, new_e):
        self.__error_handling = new_e
        
    def set_isbn_pattern(self, new_isbn_pattern):
        self.__isbn_pattern = new_isbn_pattern

    def set_publication_date_pattern(self, new_publication_date_pattern):
        self.__publication_date_pattern = new_publication_date_pattern

    def set_books(self, identifier, obj): # Adds new "Book.get_title()" (key) and "Book" object (value)
        self.__books[identifier] = obj

    def add_new_book(self): # Allows users to add new book to "self.__books"
        print("\nAdd new book:\n")

        title = self.get_e().check_input("Enter the book title: ", "Title")
        author = self.get_e().check_input("Enter the book author: ", "Author")
        isbn = self.get_e().validate_input("Enter the book ISBN: ", "ISBN", self.get_isbn_pattern())
        publication_date = self.get_e().validate_input("Enter the book publication date: ",\
        "publication date", self.get_publication_date_pattern())
        name = self.get_e().check_input("Enter the book genre: ", "Genre")
        description = self.get_e().check_input("Enter book description: ", "Description")
        category = self.get_e().check_input("Enter book category: ", "Category")
        new_book = b(name, description, category, title, author, isbn, publication_date)
        
        if self.get_e().check_if_already_exists("book", self.get_books(), title):
            return
        
        self.set_books(title, new_book)

        print(f"\nBook \"{title}\" added!")

    def borrow_book(self, user_ops): # Allows users to borrow book
        print("\nBorrow a book:\n")

        if not self.get_e().find_objects(user_ops.get_users()):
            print("Please add a user before borrowing a book.")

            return

        library_id = self.get_e().validate_input("Enter the library ID of the user borrowing the book: ",\
        "library ID", user_ops.get_library_id_pattern())
        user = self.get_e().check_if_exists("user", user_ops.get_users(), library_id)

        if not user:
            return
        
        title = self.get_e().check_input("Enter the book title you wish to borrow: ", "Title")
        book = self.get_e().check_if_exists("book", self.get_books(), title)

        if not book:
            return
        
        if self.get_e().check_if_book_is_borrowed(book, title):
            return
        
        book.set_availability_status()
        user.set_borrowed_book_titles(title)

        print(f"\nBook \"{title}\" borrowed!")

    def return_book(self, user_ops): # Allows users to return book
        print("\nReturn a book:\n")

        if not self.get_e().find_objects(user_ops.get_users()):
            print("Please add a user before returning a book.")

            return

        library_id = self.get_e().validate_input("Enter the library ID of the user returning the book: ",\
        "library ID", user_ops.get_library_id_pattern())
        user = self.get_e().check_if_exists("user", user_ops.get_users(), library_id)

        if not user:
            return
        
        title = self.get_e().check_input("Enter the book title you wish to return: ", "Title")
        book = self.get_e().check_if_exists("book", self.get_books(), title)

        if not book:
            return
        
        if self.get_e().check_if_book_is_returned(user, title):
            return
        
        book.set_availability_status()
        user.get_borrowed_book_titles().remove(title)

        print(f"\nBook \"{title}\" returned!")

    def search_for_book(self): # Allows users to search for and display author details (functions the same as "view_x_details" methods)
        print("\nSearch for a book:\n")

        if not self.get_e().find_objects(self.get_books()):
            print("No books found in the system.")

            return

        title = self.get_e().check_input("Enter the title of the book you wish to search for: ", "Title")
        book = self.get_e().check_if_exists("title", self.get_books(), title)

        if not book:
            return
        
        print(f"Book found!\n\n\
- Title: {book.get_title()}\n\
- Author: {book.get_author()}\n\
- ISBN: {book.get_isbn()}\n\
- Publication Date: {book.get_publication_date()}\n\
- Avalability Status: {'Available' if book.get_availability_status() else 'Borrowed'}\n\
- Genre: {book.get_name()}\n\
- Description: {book.get_description()}\n\
- Category: {book.get_category()}")
        
    def display_all_books(self): # Displays all book authors and titles
        print("\nDisplay all books:\n")

        if not self.get_e().find_objects(self.get_books()):
            print("No books to display.")

            return

        for identifier, obj in self.get_books().items():
            print(f"- {obj.get_author()}: {identifier}")