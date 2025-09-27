#Desafío 76: 
#Construye un árbol binario simple con al menos 3 niveles de profundidad. 
#Cada nodo debe contener un número entero como valor. Una vez construido el árbol, 
#implementa una función que imprima los valores de los nodos siguiendo un recorrido en preorden.

class Nodo:
    def __init__(self, valor):
        # Inicializa un nodo con un valor entero
        self.valor = valor
        self.izquierdo = None   # Referencia al hijo izquierdo
        self.derecho = None     # Referencia al hijo derecho

class ArbolBinario:
    def __init__(self):
        self.raiz = None  # Inicialmente el árbol está vacío
    
    def construir_arbol(self):
        # Construye el árbol con al menos 3 niveles de profundidad
        self.raiz = Nodo(10)  # Nodo raíz
        self.raiz.izquierdo = Nodo(5)
        self.raiz.derecho = Nodo(15)

        self.raiz.izquierdo.izquierdo = Nodo(3)
        self.raiz.izquierdo.derecho = Nodo(7)

        self.raiz.derecho.izquierdo = Nodo(12)
        self.raiz.derecho.derecho = Nodo(18)

        # Nivel 4 para profundidad adicional en el subárbol izquierdo
        self.raiz.izquierdo.izquierdo.izquierdo = Nodo(1)

    def preorden(self, nodo):
        # Recorre el árbol en preorden: raíz, subárbol izquierdo, subárbol derecho
        if nodo is None:
            return
        print(nodo.valor, end=' ')  # Visita el nodo actual
        self.preorden(nodo.izquierdo)  # Recorre el subárbol izquierdo
        self.preorden(nodo.derecho)    # Recorre el subárbol derecho


# Uso del árbol
arbol = ArbolBinario()
arbol.construir_arbol()  # Crea la estructura del árbol
print("Recorrido en preorden:")
arbol.preorden(arbol.raiz)  # Imprime los valores en preorden



