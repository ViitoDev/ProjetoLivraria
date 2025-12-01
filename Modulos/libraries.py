class Library:
    libraries = []

    def __init__(self, name):
        self.name = name
        self._active = False
        Library.libraries.append(self)

    def __str__(self):
        return self.name
    
    def list_Libraries():
        for library in Library.libraries:
            print(f"{library.name} | {library.active}")

    def toggle_state(self):
        self._active = not self._active

    @property
    def active(self):
        "Ativada" if self._active else "Desativada"
    
city_library = Library("City Library")
shopping_library = Library("Shopping Library")
city_library.toggle_state()
shopping_library.toggle_state()

Library.list_Libraries()