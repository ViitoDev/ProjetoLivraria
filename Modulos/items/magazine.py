from Modulos.items.library_item import LibraryItem

class Magazine(LibraryItem):
    def __init__(self, title, author, price, edition):
        super().__init__(title, author, price)
        self.edition = edition