from error_handling import ErrorHandler as e
from genre import Genre as g

class GenreOperations:
    def __init__(self):
        self.__error_handling = e()
        self.__genres = {}

    def get_e(self):
        return self.__error_handling
    
    def get_genres(self):
        return self.__genres
    
    def set_e(self, new_e):
        self.__error_handling = new_e

    def set_genres(self, identifier, obj):
        self.__genres[identifier] = obj

    def add_genre(self):
        print("\nAdd a new genre:\n")

        name = self.get_e().check_input("Enter the genre name: ", "Name")
        description = self.get_e().check_input("Enter the genre description: ", "Description")
        category = self.get_e().check_input("Enter the genre category: ", "Category")
        new_genre = g(name, description, category)

        if self.get_e().check_if_already_exists("genre", self.get_genres(), name):
            return
        
        self.set_genres(name, new_genre)

        print(f"\nGenre \"{name}\" added!")

    def view_genre_details(self):
        print("\nView genre details:\n")

        if not self.get_e().find_objects(self.get_genres()):
            print("No genres found in the system.")

            return

        name = self.get_e().check_input("Enter the name of the genre you wish to view: ", "Name")
        genre = self.get_e().check_if_exists("genre", self.get_genres(), name)

        if not genre:
            return
        
        print(f"Genre found!\n\n\
- Name: {genre.get_name()}\n\
- Description: {genre.get_description()}\n\
- Category: {genre.get_category()}")
        
    def display_all_genres(self):
        print("\nDisplay all genres:\n")

        if not self.get_e().find_objects(self.get_genres()):
            print("No genres to display.")

            return

        for identifier in self.get_genres().keys():
            print(f"- {identifier}")