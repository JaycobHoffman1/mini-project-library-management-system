class Genre:
    def __init__(self, name, description, category):
        self.__name = name
        self.__description = description
        self.__category = category

    def get_name(self):
        return self.__name
    
    def get_description(self):
        return self.__description
    
    def get_category(self):
        return self.__category
    
    def set_name(self, new_name):
        self.__name = new_name

    def set_description(self, new_description):
        self.__description = new_description

    def set_category(self, new_category):
        self.__category = new_category