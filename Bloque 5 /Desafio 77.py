#Desafío 77
#Dado un árbol binario con números enteros en cada nodo, 
#implementa una función que recorra el árbol en inorden 
# y calcule la suma de todos los valores almacenados en los nodos. El programa debe devolver el resultado final de la suma.


class Nodo:
    def __init__(self, valor):
        # Inicializa un nodo con un valor entero
        self.valor = valor
        # Referencia al hijo izquierdo del nodo, inicialmente None
        self.izquierdo = None
        # Referencia al hijo derecho del nodo, inicialmente None
        self.derecho = None

def suma_inorden(nodo):
    # Si el nodo es None (caso base), retorna 0 para no afectar la suma
    if nodo is None:
        return 0
    # Recorre recursivamente el subárbol izquierdo,
    # suma el valor del nodo actual,
    # y luego recorre el subárbol derecho
    return suma_inorden(nodo.izquierdo) + nodo.valor + suma_inorden(nodo.derecho)

# Ejemplo de uso:
raiz = Nodo(10)                # Nodo raíz con valor 10
raiz.izquierdo = Nodo(5)      # Hijo izquierdo con valor 5
raiz.derecho = Nodo(15)       # Hijo derecho con valor 15
raiz.izquierdo.izquierdo = Nodo(3)  # Subárbol izquierdo-izquierdo con valor 3
raiz.izquierdo.derecho = Nodo(7)    # Subárbol izquierdo-derecho con valor 7

# Calcula la suma de todos los valores en el árbol mediante recorrido inorden
resultado = suma_inorden(raiz)

# Imprime el resultado de la suma
print("Suma de todos los nodos:", resultado)

