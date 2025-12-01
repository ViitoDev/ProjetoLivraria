from Modulos.libraries import Library

city_library = Library("City Library")
shopping_library = Library("Shopping Library")
city_library.toggle_state()
shopping_library.toggle_state()

def main():
    Library.list_Libraries()

if __name__ == "__main__":
    main()