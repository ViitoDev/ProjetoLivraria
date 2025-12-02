from Modulos.avaluate import Evaluating
from Modulos.items.library_item import LibraryItem

class Library:
    libraries = []

    def __init__(self, name):
        self.name = name
        self._active = False
        self.evaluation = []
        self.items = []
        Library.libraries.append(self)

    def __str__(self):
        return self.name
    
    @classmethod
    def list_Libraries(cls):
        print(f"{'Library name'.ljust(25)}| {'Avarege note'.ljust(25)} | {'Status'}")
        for library in Library.libraries:
            print(f"{library.name.ljust(25)}| {str(library.evaluate_media).ljust(25)} | {library.active}")

    def toggle_state(self):
        self._active = not self._active

    @property
    def active(self):
        if self._active and self.evaluation:
            return "Ativada"
        else:
            return "Desativada"

    def receive_evaluation(self, client, note):
        evaluate = Evaluating(client, note)
        self.evaluation.append(evaluate)

    @property
    def evaluate_media(self):
        if not self.evaluation:
            return "-"
        sum1 = sum(evaluate._note for evaluate in self.evaluation)
        average = round(sum1 / len(self.evaluation))
        return average
    
    def add_item(self, item):
        if isinstance(item, LibraryItem):
            self.items.append(item)

    def show_items(self):
        print(f"Library items {self.name}\n")
        for i, item in enumerate(self.items, start=1):
            if hasattr(item, "isbn"):
                book_msg = f"{i}. Title: {item._title} | Author: {item._author} | Price: {item._price} | ISBN: {item.isbn}"
                print(book_msg)
            else:
                magazine_msg = f"{i}. Title: {item._title} | Author: {item._author} | Price: {item._price} | Edition: {item.edition}"
                print(magazine_msg)