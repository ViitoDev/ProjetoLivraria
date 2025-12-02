from Modulos.libraries import Library
from Modulos.items.magazine import Magazine
from Modulos.items.books import Book

city_library = Library("City Library")
shopping_library = Library("Shopping Library")

book1 = Book("1984", "George Orwell", 30.00, "084-1922")
magazine1 = Magazine("National Geographic", "John Doe", 15.0, "5")

city_library.add_item(book1)
city_library.add_item(magazine1)

# city_library.toggle_state()
# shopping_library.toggle_state()

# city_library.receive_evaluation("John", 10)
# city_library.receive_evaluation("Anna", 1.5)

def main():
    # Library.list_Libraries()
    print(vars(book1))
    print(vars(magazine1))
    city_library.show_items()

if __name__ == "__main__":
    main()