from Modulos.libraries import Library

city_library = Library("City Library")
shopping_library = Library("Shopping Library")

city_library.toggle_state()
shopping_library.toggle_state()

city_library.receive_evaluation("John", 8.5)
city_library.receive_evaluation("Anna", 9.0)

def main():
    Library.list_Libraries()

if __name__ == "__main__":
    main()