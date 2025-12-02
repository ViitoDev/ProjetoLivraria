from Modulos.libraries import Library
from Modulos.items.magazine import Magazine
from Modulos.items.books import Book

city_library = Library("City Library")
shopping_library = Library("Shopping Library")

book1 = Book("1984", "George Orwell", 30.00, "084-1922")
magazine1 = Magazine("National Geographic", "John Doe", 15.0, "5°")

# city_library.toggle_state()
# shopping_library.toggle_state()

# city_library.receive_evaluation("John", 8.5)
# city_library.receive_evaluation("Anna", 9.0)

def main():
    # Library.list_Libraries()
    print(vars(book1))
    print(vars(magazine1))

if __name__ == "__main__":
    main()