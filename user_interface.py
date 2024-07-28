from error_handling import ErrorHandler as e
from book_operations import BookOperations as b
from user_operations import UserOperations as u
from genre_operations import GenreOperations as g
from author_operations import AuthorOperations as a

class UserInterface:
    def __init__(self):
        self.__error_handling = e()
        self.__book_operations = b()
        self.__user_operations = u()
        self.__genre_operations = g()
        self.__author_operations = a()

    def get_e(self):
        return self.__error_handling
    
    def get_b(self):
        return self.__book_operations
    
    def get_u(self):
        return self.__user_operations
    
    def get_g(self):
        return self.__genre_operations
    
    def get_a(self):
        return self.__author_operations
    
    def set_e(self, new_e):
        self.__error_handling = new_e

    def set_b(self, new_b):
        self.__book_operations == new_b
    
    def set_u(self, new_u):
        self.__user_operations = new_u

    def set_g(self, new_g):
        self.__genre_operations = new_g

    def set_a(self, new_a):
        self.__author_operations = new_a

    def display_user_interface(self):
        def display_book_operations(): # Displays book operations menu
            while True:
                print("\nBook Operations:\n\
1. Add a new book\n\
2. Borrow a book\n\
3. Return a book\n\
4. Search for a book\n\
5. Display all books\n\
6. Main menu\n")
                
                user_selection = self.get_e().check_if_in_range("Please select an option from the menu above: ", "Field", 6)

                if user_selection == 1:
                    self.get_b().add_new_book()
                elif user_selection == 2:
                    self.get_b().borrow_book(self.get_u())
                elif user_selection == 3:
                    self.get_b().return_book(self.get_u())
                elif user_selection == 4:
                    self.get_b().search_for_book()
                elif user_selection == 5:
                    self.get_b().display_all_books()
                elif user_selection == 6:
                    break

        def display_user_operations(): # Displays user operations menu
            while True:
                print("\nUser Operations:\n\
1. Add a new user\n\
2. View user details\n\
3. Display all users\n\
4. Main menu\n")
                
                user_selection = self.get_e().check_if_in_range("Please select an option from the menu above: ", "Field", 4)

                if user_selection == 1:
                    self.get_u().add_new_user()
                elif user_selection == 2:
                    self.get_u().view_user_details()
                elif user_selection == 3:
                    self.get_u().display_all_users()
                elif user_selection == 4:
                    break

        def display_genre_operations(): # Displays genre operations menu
            while True:
                print("\nGenre Operations:\n\
1. Add a new genre\n\
2. View genre details\n\
3. Display all genres\n\
4. Main menu\n")
                
                user_selection = self.get_e().check_if_in_range("Please select an option from the menu above: ", "Field", 4)

                if user_selection == 1:
                    self.get_g().add_new_genre()
                elif user_selection == 2:
                    self.get_g().view_genre_details()
                elif user_selection == 3:
                    self.get_g().display_all_genres()
                elif user_selection == 4:
                    break

        def display_author_operations(): # Displays author operations menu
            while True:
                print("\nAuthor Operations:\n\
1. Add a new author\n\
2. View author details\n\
3. Display all authors\n\
4. Main menu\n")
                
                user_selection = self.get_e().check_if_in_range("Please select an option from the menu above: ", "Field", 4)

                if user_selection == 1:
                    self.get_a().add_new_author()
                elif user_selection == 2:
                    self.get_a().view_author_details()
                elif user_selection == 3:
                    self.get_a().display_all_authors()
                elif user_selection == 4:
                    break

        while True: 
# Displays main menu (does not have its own function to ensure that sub-menus always return here when "Main menu" is selected)

            print("\nWelcome to the Library Management System!\n\n\
Main Menu:\n\
1. Book Operations\n\
2. User Operations\n\
3. Author Operations\n\
4. Genre Operations\n\
5. Quit\n")
            
            user_selection = self.get_e().check_if_in_range("Please select an option from the menu above: ", "Field", 5)

            if user_selection == 1:
                display_book_operations()
            elif user_selection == 2:
                display_user_operations()
            elif user_selection == 3:
                display_author_operations()
            elif user_selection == 4:
                display_genre_operations()
            elif user_selection == 5:
                print("\nQuitting program. Thank you for using the Library Management System!\n")

                break