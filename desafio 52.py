class Libro:
    # Constructor con atributos privados
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn

    # --- Métodos getter y setter para título ---
    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    # --- Métodos getter y setter para autor ---
    def get_autor(self):
        return self.__autor

    def set_autor(self, autor):
        self.__autor = autor

    # --- Métodos getter y setter para ISBN ---
    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, isbn):
        self.__isbn = isbn

    # Método para mostrar toda la información
    def mostrar_info(self):
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.__autor}")
        print(f"ISBN: {self.__isbn}")


# --- Para resolver el desafío lo que hice fue que los datos como(título, autor e ISBN)
# --- no se puedan cambiar por descuido y guardándolos como si estuvieran en una cajita cerrada usando delante del nombre "--". 
# --- Luego le agregué los getters, que permiten ver la información, y los setters, que permiten modificarla de manera controlada. 
# --- Finalmente, creé el método mostrar_info(), que muestra todos los datos juntos de manera clara y práctica, ya sea para leerlos o usarlos.

# Programa principal

# Crear un libro
libro1 = Libro("La tregua", "Mario Benedetti", "978-84-376-0494-7")

# Mostrar datos iniciales
print(" Datos del libro original:")
libro1.mostrar_info()

# Usar getters
print("\n Accediendo con getters:")
print("Título:", libro1.get_titulo())
print("Autor:", libro1.get_autor())
print("ISBN:", libro1.get_isbn())

# Usar setters para modificar
print("\n Modificando con setters...")
libro1.set_titulo("Gracias por el fuego")
libro1.set_autor("Mario Benedetti")
libro1.set_isbn("978-84-376-0500-5")

# Mostrar datos modificados
print("\n Datos del libro actualizado:")
libro1.mostrar_info()
