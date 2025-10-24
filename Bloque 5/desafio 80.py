# Desafío 80: Evaluación de expresiones Matemáticas con árboles
#"Los árboles de expresiones son una herramienta poderosa en ciencias de la computación 
#"y se utilizan comúnmente para evaluar expresiones matemáticas. En este desafío, 
#"te propongo construir y evaluar un árbol de expresiones para una expresión matemática dada.
#Tu tarea es escribir un programa en Python que haga lo siguiente:**
#* Construir el Árbol de Expresiones: Dada una expresión matemática en forma de cadena, construir el árbol de expresiones correspondiente. Puedes asumir que la expresión está bien formada y solo contiene números enteros, y los operadores +, -, *, /.
#* Evaluar el Árbol de Expresiones: Una vez construido el árbol, evaluarlo y devolver el resultado de la expresión.
#* Prueba tu Programa: Utiliza la expresión "5 + 3 * 4" para probar tu programa. El resultado debería ser 17.
## Consejos
#Puedes crear una clase Nodo para representar los nodos en tu árbol de expresiones. 
#Cada nodo debería tener un valor y dos hijos (izquierdo y derecho).
#Puedes crear funciones auxiliares para ayudarte a construir y evaluar el árbol de expresiones.
#Recuerda seguir las reglas de precedencia de operadores al construir el árbol.

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
