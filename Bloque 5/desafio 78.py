#Desafío 78: 
#Construye un árbol binario en el que cada nodo contiene un número entero. 
#Implementa una función que recorra el árbol en postorden y devuelva el valor máximo encontrado entre todos los nodos del árbol.

class Nodo:
    def __init__(self, valor):
        # Inicializa un nodo con el valor entero dado
        self.valor = valor
        # Referencia al hijo izquierdo (inicialmente None)
        self.izquierdo = None
        # Referencia al hijo derecho (inicialmente None)
        self.derecho = None

def max_postorden(nodo):
    # Caso base: si el nodo es None, retorna el menor valor posible para no afectar la comparación
    if nodo is None:
        return float('-inf')
    # Recursivamente obtiene el máximo en el subárbol izquierdo
    max_izq = max_postorden(nodo.izquierdo)
    # Recursivamente obtiene el máximo en el subárbol derecho
    max_der = max_postorden(nodo.derecho)
    # Retorna el valor máximo entre el nodo actual y los máximos de los subárboles
    return max(nodo.valor, max_izq, max_der)

# Ejemplo de uso:
raiz = Nodo(10)                      # Nodo raíz con valor 10
raiz.izquierdo = Nodo(5)            # Hijo izquierdo con valor 5
raiz.derecho = Nodo(15)             # Hijo derecho con valor 15
raiz.izquierdo.izquierdo = Nodo(3) # Subárbol izquierdo-izquierdo con valor 3
raiz.izquierdo.derecho = Nodo(7)   # Subárbol izquierdo-derecho con valor 7
raiz.derecho.derecho = Nodo(20)    # Subárbol derecho-derecho con valor 20

maximo = max_postorden(raiz)        # Calcula el máximo valor en el árbol
print("Valor máximo en el árbol (postorden):", maximo)  # Muestra el valor máximo
