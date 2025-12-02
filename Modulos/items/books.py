from Modulos.items.library_item import LibraryItem

class Book(LibraryItem):
    def __init__(self, title, author, price, isbn):
        super().__init__(title, author, price)
        self.isbn = isbn
