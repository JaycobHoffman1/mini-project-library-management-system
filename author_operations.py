from error_handling import ErrorHandler as e
from author import Author as a

class AuthorOperations:
    def __init__(self):
        self.__error_handling = e()
        self.__authors = {} # stores "Author.get_name()" as key and "Author" object as value

    def get_e(self):
        return self.__error_handling
    
    def get_authors(self):
        return self.__authors
    
    def set_e(self, new_e):
        self.__error_handling = new_e

    def set_authors(self, identifier, obj): # Adds new "Author.get_name()" (key) and "Author" object (value)
        self.__authors[identifier] = obj

    def add_new_author(self): # Allows users to add new author to "self.__authors"
        print("\nAdd a new author:\n")

        name = self.get_e().check_input("Enter the author name: ", "Name")
        biography = self.get_e().check_input("Enter the author biography: ", "Biography")
        new_author = a(name, biography)

        if self.get_e().check_if_already_exists("author", self.get_authors(), name):
            return
        
        self.set_authors(name, new_author)

        print(f"\nAuthor \"{name}\" added!")

    def view_author_details(self): # Allows users to search for and display author details
        print("\nView author details:\n")

        if not self.get_e().find_objects(self.get_authors()):
            print("No authors found in the system.")

            return

        name = self.get_e().check_input("Enter the name of the author you wish to view: ", "Name")
        author = self.get_e().check_if_exists("author", self.get_authors(), name)

        if not author:
            return
        
        print(f"Author found!\n\n\
- Name: {author.get_name()}\n\
- Biography: {author.get_biography()}")
        
    def display_all_authors(self): # Displays all author names
        print("\nDisplay all authors:\n")

        if not self.get_e().find_objects(self.get_authors()):
            print("No authors to display.")

            return

        for identifier in self.get_authors().keys():
            print(f"- {identifier}")