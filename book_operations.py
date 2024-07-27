from error_handling import ErrorHandler as e
from book import Book as b
from user_operations import UserOperations as u

class BookOperations:
    def __init__(self):
        self.__error_handling = e()
        self.__isbn_pattern = r"\d{3}-\d{4}-\d{4}-\d-\d$"
        self.__publication_date_pattern = r"(\d{2}/){2}\d{4}$"
        self.__books = {}

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

    def set_books(self, identifier, obj):
        self.__books[identifier] = obj

    def add_new_book(self):
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

    def borrow_book(self, user_ops):
        print("\nBorrow a book:\n")

        if not self.get_e().find_objects(user_ops.get_users()):
            print("Please add a user before borrowing a book.")

            return

        library_id = self.get_e().validate_input("Enter the library ID of the user borrowing the book: ",\
        "library ID", user_ops.get_library_id_pattern())
        user = self.get_e().check_if_exists("user", user_ops.get_users(), library_id)
        title = self.get_e().check_input("Enter the book title you wish to borrow: ", "Title")
        book = self.get_e().check_if_exists("book", self.get_books(), title)

        if not book:
            return
        
        if self.get_e().check_if_book_is_borrowed(book):
            print(f"\nBook \"{title}\" has already been borrowed.")

            return
        
        book.set_availability_status()
        print(book.get_availability_status())
        user.set_borrowed_book_titles(title)

        print(f"\nBook \"{title}\" borrowed!")

    def return_book(self, user_ops):
        print("\nReturn a book:\n")

        if not self.get_e().find_objects(user_ops.get_users()):
            print("Please add a user before returning a book.")

            return

        library_id = self.get_e().validate_input("Enter the library ID of the user returning the book: ",\
        "library ID", user_ops.get_library_id_pattern())
        user = self.get_e().check_if_exists("user", user_ops.get_users(), library_id)
        title = self.get_e().check_input("Enter the book title you wish to return: ", "Title")
        book = self.get_e().check_if_exists("book", self.get_books(), title)

        if not book:
            return
        
        if not self.get_e().check_if_book_is_borrowed(book):
            print(f"\nBook \"{title}\" has not been borrowed.")

            return
        
        book.set_availability_status()
        user.get_borrowed_book_titles().remove(title) # LEFT OFF HERE

        print(f"\nBook \"{title}\" returned!")

user_ops = u() # KEEP THESE
book_ops = BookOperations()

user_ops.add_user()
user_ops.add_user()
book_ops.add_new_book()
book_ops.borrow_book(user_ops)
book_ops.return_book(user_ops)