class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_book_titles = [] # List of borrowed "Book.get_title()"s

    def get_name(self):
        return self.__name
    
    def get_library_id(self):
        return self.__library_id
    
    def get_borrowed_book_titles(self):
        return self.__borrowed_book_titles
    
    def set_name(self, new_name):
        self.__name = new_name

    def set_library_id(self, new_library_id):
        self.__library_id = new_library_id

    def set_borrowed_book_titles(self, new_borrowed_book_title):
        self.__borrowed_book_titles.append(new_borrowed_book_title)