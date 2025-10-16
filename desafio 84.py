# Desafío 85: Árbol de clasificación por rendimiento

class NodoABB:
    def __init__(self, nombre, promedio):
        self.nombre = nombre        # Guarda el nombre del estudiante en el nodo.
        self.promedio = promedio    # Guarda el promedio (clave usada para ordenar en el ABB).
        self.izq = None             # Referencia al hijo izquierdo (nodos con promedio menor).
        self.der = None             # Referencia al hijo derecho (nodos con promedio mayor o igual).

def insertar(raiz, nombre, promedio):
    if raiz is None:
        return NodoABB(nombre, promedio)   # Si la posición está vacía, crea y devuelve un nuevo nodo.
    if promedio < raiz.promedio:
        raiz.izq = insertar(raiz.izq, nombre, promedio)  # Si el promedio es menor, insertar en subárbol izquierdo.
    else:
        raiz.der = insertar(raiz.der, nombre, promedio)  # Si es mayor o igual, insertar en subárbol derecho.
    return raiz   # Devuelve la raíz (posible actualizada) del subárbol.

def inorden(raiz):
    if raiz:
        inorden(raiz.izq)                       # Recorre recursivamente el subárbol izquierdo (menores).
        print(f"{raiz.nombre}: {raiz.promedio}")# Visita el nodo actual (imprime nombre y promedio).
        inorden(raiz.der)                       # Recorre recursivamente el subárbol derecho (mayores/iguales).

#  uso
datos = [("Ana", 8.5), ("Luis", 9.2), ("María", 7.8), ("Carlos", 9.5)]
arbol = None
for nombre, prom in datos:
    arbol = insertar(arbol, nombre, prom)  # Inserta cada tupla (nombre, promedio) en el ABB.

print("Estudiantes en orden ascendente de promedio:")
inorden(arbol)  # Imprime los estudiantes en orden ascendente según su promedio (por recorrido inorden).

# Desafío 85: Árbol de clasificación por rendimiento (versión compacta)

class NodoABB:
    def __init__(self,n,p): 
        self.nombre = n          # Asigna el nombre del estudiante al nodo
        self.promedio = p        # Asigna el promedio del estudiante (clave para ordenar en el ABB)
        self.izq = self.der = None  # Inicializa punteros a los subárboles izquierdo y derecho como None

def ins(r,n,p):
    if not r: 
        return NodoABB(n,p)     # Si el nodo actual es None, crea un nuevo nodo y lo devuelve
    # La siguiente línea maneja la inserción recursiva de forma compacta:
    # - Determina si el promedio es menor o mayor/igual que el nodo actual
    # - Inserta en el subárbol izquierdo si es menor, derecho si es mayor o igual
    # - Usa __setattr__ para asignar el resultado recursivo al subárbol correspondiente
    (r.izq if p<r.promedio else r.der).__setattr__(
        'izq' if p<r.promedio else 'der', 
        ins(r.izq if p<r.promedio else r.der,n,p)
    ) if (p<r.promedio and r.izq) or (p>=r.promedio and r.der) else (r:=ins(None,n,p))
    return r                     # Devuelve la raíz actual del árbol (posiblemente actualizada)

def ino(r):
    if r: 
        ino(r.izq)               # Recorre primero el subárbol izquierdo (menores)
        print(f"{r.nombre}: {r.promedio}")  # Visita el nodo actual (imprime nombre y promedio)
        ino(r.der)               # Recorre el subárbol derecho (mayores/iguales)
