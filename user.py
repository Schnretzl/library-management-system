class User:
    def __init__(self, name, id, borrowed_books = []):
        self.__name = name
        self.__id = id
        self.__borrowed_books = borrowed_books
        
    @property
    def name(self):
        return self.__name
    
    @property
    def id(self):
        return self.__id
    
    @property
    def borrowed_books(self):
        return self.__borrowed_books