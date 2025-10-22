class Autor:
    
    def __init__(self, nombre="", nacionalidad=""):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.libros = []  

    
    def mostrar_autor(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")

   
    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro}' agregado correctamente.")

   
    def eliminar_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)
            print(f"Libro '{libro}' eliminado correctamente.")
        else:
            print(f"El libro '{libro}' no se encuentra en la lista.")

    
    def mostrar_libros(self):
        if self.libros:
            print(f"Libros de {self.nombre}:")
            for libro in self.libros:
                print(f"- {libro}")
        else:
            print(f"{self.nombre} aún no tiene libros registrados.")



# Programa principal

autor1 = Autor("Mario Benedetti", "Uruguayo")

autor1.mostrar_autor()

autor1.agregar_libro("La tregua")
autor1.agregar_libro("Gracias por el fuego")

autor1.mostrar_libros()

autor1.eliminar_libro("La tregua")

# Mostrar libros después de eliminar
autor1.mostrar_libros()


