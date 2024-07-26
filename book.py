from genre import Genre as g

class Book(g):
    def __init__(self, name, description, category, title, author, isbn, publication_date):
        super().__init__(name, description, category)
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__publication_date = publication_date
        self.__availability_status = True

    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_isbn(self):
        return self.__isbn
    
    def get_publication_date(self):
        return self.__publication_date
    
    def get_availability_status(self):
        return self.__availability_status
    
    def set_title(self, new_title):
        self.__title = new_title

    def set_author(self, new_author):
        self.__author = new_author

    def set_isbn(self, new_isbn):
        self.__isbn = new_isbn

    def set_publication_date(self, new_publication_date):
        self.__publication_date = new_publication_date

    def set_availability_status(self):
        self.__availability_status = not self.__availability_status