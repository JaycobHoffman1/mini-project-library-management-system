from error_handling import ErrorHandler as e
from user import User as u

class UserOperations:
    def __init__(self):
        self.__error_handling = e()
        self.__library_id_pattern = r"[A-Z]{3}-\d{4}$"
        self.__users = {} # stores "User.get_library_id()" as key and "User" object as value

    def get_e(self):
        return self.__error_handling
    
    def get_library_id_pattern(self):
        return self.__library_id_pattern
    
    def get_users(self):
        return self.__users
    
    def set_e(self, new_e):
        self.__error_handling = new_e

    def set_library_id_pattern(self, new_library_id_pattern):
        self.__library_id_pattern = new_library_id_pattern

    def set_users(self, identifier, obj): # Adds new "User.get_library_id()" (key) and "User" object (value)
        self.__users[identifier] = obj

    def add_new_user(self): # Allows users to add new user to "self.__users"
        print("\nAdd a new user:\n")

        name = self.get_e().check_input("Enter the user name: ", "Name")
        library_id = self.get_e().validate_input("Enter the user library ID: ", "Library ID", self.get_library_id_pattern())
        new_user = u(name, library_id)

        if self.get_e().check_if_already_exists("user", self.get_users(), library_id):
            return
        
        self.set_users(library_id, new_user)

        print(f"\nUser with library ID \"{library_id}\" added!")

    def view_user_details(self): # Allows users to search for and display user details
        print("\nView user details:\n")

        if not self.get_e().find_objects(self.get_users()):
            print("No users found in the system.")

            return

        library_id = self.get_e().validate_input("Enter the library ID of the user you wish to view: ",\
        "library ID", self.get_library_id_pattern())
        user = self.get_e().check_if_exists("user", self.get_users(), library_id)

        if not user:
            return
        
        print(f"User found!\n\n\
Library ID: {user.get_library_id()}\n\
- Name: {user.get_name()}")
        
    def display_all_users(self): # Displays all user library IDs and names
        print("\nDisplay all users:\n")

        if not self.get_e().find_objects(self.get_users()):
            print("No users to display.")

            return

        for identifier, obj in self.get_users().items():
            print(f"- {identifier}: {obj.get_name()}")