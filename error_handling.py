import re

class ErrorHandler:
    def check_input(self, user_input, input_type): # Ensures user input is not blank/consisting entirely of spaces
        while True:
            try:
                _input = input(user_input)

                if (not _input) or len(_input) == _input.count(" "):
                    raise ValueError(f"{input_type} cannot be blank.")
            except ValueError as v:
                print(v)
            else:
                return _input
            
    def validate_input(self, user_input, input_type, pattern): # Performs "check_input()" while also checking user input against regex
        while True:
            try:
                _input = self.check_input(user_input, f"{input_type[0].upper()}{input_type[1:]}")
                # Does not use ".capitalize()" to preserve the case of "ISBN" when it is passed as a parameter

                if not re.match(pattern, _input):
                    raise ValueError(f"Invalid {input_type}.")
            except ValueError as v:
                print(v)
            else:
                return _input
            
    def check_if_already_exists(self, obj_type, dict, target_identifier): 
        # Checks if an entity's identifier already exists before adding new instance

        try:
            if target_identifier.lower() in [identifier.lower() for identifier in dict.keys()]:
                raise ValueError(f"\nThis {obj_type} already exists in the system.")
        except ValueError as v:
            print(v)

            return True
        
        return False
        
    def check_if_exists(self, obj_type, dict, target_identifier):
        """Checks if an entity's identifier already exists before performing operations on it 
        (returns object based on identifier for easier operations within the respective method)"""

        try:
            obj = dict.get(target_identifier, False)

            if not obj:
                raise ValueError(f"\nThis {obj_type} does not exist in the system.")
        except ValueError as v:
            print(v)

            return False
        
        return obj
    
    def find_objects(self, dict): # Ensures a dictionary is populated with data before executing method
        try:
            if not dict:
                raise ValueError
        except ValueError:
            return False
        
        return True
    
    def check_if_book_is_borrowed(self, book, title): # Checks if book has been borrowed under any library ID
        try:
            if not book.get_availability_status():
                raise ValueError
        except ValueError:
            print(f"\n\"{title}\" has already been borrowed.")

            return True
        
        return False
    
    def check_if_book_is_returned(self, user, title): # Checks if book has been returned under any library ID
        try:
            if title not in user.get_borrowed_book_titles():
                raise ValueError
        except ValueError:
            print(f"\nThis user has not borrowed \"{title}\".")

            return True
        
        return False
    
    def check_if_in_range(self, user_input, input_type, max_num): 
        # Performs "check_input()" function while also ensuring user input is integer between 1 and a specified positive integer
        
        while True:
            try:
                _input = int(self.check_input(user_input, input_type))

                if _input < 1 or _input > max_num:
                    raise ValueError
            except ValueError:
                print("Please ensure you enter a valid numeric value that appears on the menu.")
            else:
                return _input