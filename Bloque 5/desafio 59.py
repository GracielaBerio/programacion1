# Desafio 59

# Clase Libro
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn

    # getters
    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_isbn(self):
        return self.__isbn

    # Método para mostrar información del libro
    def mostrar_info(self):
        return f"Título: {self.__titulo}, Autor: {self.__autor}, ISBN: {self.__isbn}"


# Clase que hereda de Libro
class LibroDigital(Libro):
    def __init__(self, titulo, autor, isbn, formato, tamaño_archivo):
        super().__init__(titulo, autor, isbn)
        self.formato = formato
        self.tamaño_archivo = tamaño_archivo

    def mostrar_info(self):
        return (super().mostrar_info() +
                f", Formato: {self.formato}, Tamaño: {self.tamaño_archivo} MB")


# Subclase LibroDigital
class EBook(LibroDigital):
    def __init__(self, titulo, autor, isbn, formato, tamaño_archivo, enlace_descarga):
        super().__init__(titulo, autor, isbn, formato, tamaño_archivo)
        self.enlace_descarga = enlace_descarga

    # Sobrescribir método
    def mostrar_info(self):
        return (super().mostrar_info() +
                f", Enlace de descarga: {self.enlace_descarga}")


# Libro de ejemplo

ebook = EBook("El principito", "Antoine de Saint-Exupéry", " 978-950-691-0969", "PDF", 1.89, "https://digitales.bcn.gob.ar/files/textos/El-Principitocompleto.pdf")
print(ebook.mostrar_info())

# 
