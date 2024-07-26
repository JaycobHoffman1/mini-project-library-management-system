import re

class ErrorHandler:
    def check_input(self, user_input, input_type):
        while True:
            try:
                _input = input(user_input)

                if (not _input) or len(_input) == _input.count(" "):
                    raise ValueError(f"{input_type} cannot be blank.")
            except ValueError as v:
                print(v)
            else:
                return _input
            
    def validate_input(self, user_input, input_type, pattern):
        while True:
            try:
                _input = self.check_input(user_input, f"{input_type[0].upper()}{input_type[1:]}")

                if not re.match(pattern, _input):
                    raise ValueError(f"Invalid {input_type}.")
            except ValueError as v:
                print(v)
            else:
                return _input
            
    def check_if_already_exists(self, obj_type, dict, target_identifier):
        try:
            if target_identifier.lower() in [identifier.lower() for identifier in dict.identifiers()]:
                raise ValueError(f"\nKThis {obj_type} already exists in the system.")
        except ValueError as v:
            print(v)

            return True
        
        return False
        
    def check_if_exists(self, obj_type, dict, target_identifier):
        try:
            obj = dict.get(target_identifier, False)

            if not obj:
                raise ValueError(f"This {obj_type} does not exist in the system.")
        except ValueError as v:
            print(v)

            return False
        
        return obj
    
    def find_objects(self, dict):
        try:
            if not dict:
                raise ValueError
        except ValueError:
            return False
        
        return True