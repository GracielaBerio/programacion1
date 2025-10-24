#Desafío 79: 
#Dado un conjunto de números enteros únicos, construye un árbol de búsqueda binaria (ABB) 
#que inserte los valores de manera que el subárbol izquierdo de cada nodo contenga solo nodos con valores menores, 
#y el subárbol derecho solo nodos con valores mayores. Una vez construido el árbol, 
#implementa una función para buscar un número dado y devuelva si ese número existe en el árbol o no.


class Nodo:
    def __init__(self, valor):
        # Inicializa un nodo con un valor entero
        self.valor = valor
        # Referencia al hijo izquierdo (nodos con valores menores)
        self.izquierdo = None
        # Referencia al hijo derecho (nodos con valores mayores)
        self.derecho = None

class ArbolBusquedaBinaria:
    def __init__(self):
        # Inicialmente el árbol está vacío, raíz es None
        self.raiz = None

    def insertar(self, valor):
        # Inserta un valor en el árbol, actualiza la raíz si está vacía
        self.raiz = self._insertar_rec(self.raiz, valor)

    def _insertar_rec(self, nodo, valor):
        # Método recursivo para insertar un nuevo nodo en el árbol
        if nodo is None:
            # Si no hay nodo, crea uno nuevo con el valor
            return Nodo(valor)
        # Si el valor es menor que el nodo actual, insertar en subárbol izquierdo
        if valor < nodo.valor:
            nodo.izquierdo = self._insertar_rec(nodo.izquierdo, valor)
        # Si el valor es mayor, insertar en subárbol derecho
        elif valor > nodo.valor:
            nodo.derecho = self._insertar_rec(nodo.derecho, valor)
        # Devuelve el nodo actual después de inserción (sin cambios si valor igual)
        return nodo

    def buscar(self, valor):
        # Busca si un valor existe en el árbol
        return self._buscar_rec(self.raiz, valor)

    def _buscar_rec(self, nodo, valor):
        # Método recursivo para buscar un valor en el árbol
        if nodo is None:
            # Si el nodo es None, no se encontró, retorna False
            return False
        if valor == nodo.valor:
            # Si el valor coincide con el nodo actual, se encontró
            return True
        elif valor < nodo.valor:
            # Si el valor es menor, buscar en subárbol izquierdo
            return self._buscar_rec(nodo.izquierdo, valor)
        else:
            # Si el valor es mayor, buscar en subárbol derecho
            return self._buscar_rec(nodo.derecho, valor)

# Ejemplo de uso
abb = ArbolBusquedaBinaria()
valores = [10, 5, 15, 3, 7, 12, 18]

# Insertar valores para construir el árbol
for v in valores:
    abb.insertar(v)

# Buscar valores y mostrar si existen en el árbol
print("Buscar 7:", abb.buscar(7))    # True
print("Buscar 20:", abb.buscar(20))  # False
