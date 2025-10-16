# Desafío 81: Recorrido por niveles
from collections import deque   # Importa deque (cola doble) desde collections; deque permite operaciones FIFO eficientes.

class Nodo:
    def __init__(self, grado, estudiantes):
        self.grado = grado                 # Almacena el número o nombre del grado en el nodo.
        self.estudiantes = estudiantes     # Lista (o colección) con los nombres de los estudiantes del grado.
        self.hijos = []  # Lista de nodos hijos
        # Inicializa una lista vacía para contener nodos hijos (niveles inferiores en este ejemplo).

def recorrido_por_niveles(raiz):
    if not raiz:
        return                           # Si la raíz es None o falsy, no hay nada que recorrer: salir de la función.
    
    cola = deque([raiz])                 # Crea una cola FIFO e inserta la raíz. Usamos deque para popleft() eficiente.
    
    while cola:                          # Mientras haya elementos en la cola (nodos por visitar)
        nivel_actual = cola.popleft()    # Extrae el primer nodo en la cola (comportamiento FIFO).
        # Imprime el grado y la lista de estudiantes del nodo actual.
        # join convierte la lista de estudiantes en una cadena separada por comas.
        print(f"Grado {nivel_actual.grado}: {', '.join(nivel_actual.estudiantes)}")
        
        # Agregar los hijos del nodo actual a la cola
        for hijo in nivel_actual.hijos:  # Recorre cada hijo del nodo actual
            cola.append(hijo)           # Añade el hijo al final de la cola para procesarlo después

# uso
raiz = Nodo(12, ["Ana", "Luis"])       # Crea el nodo raíz representando, por ejemplo, 12º grado y sus estudiantes.
grado11 = Nodo(11, ["María", "Pedro"]) # Crea un nodo para 11º grado.
grado10 = Nodo(10, ["Sofía", "Carlos"])# Crea un nodo para 10º grado.
raiz.hijos.extend([grado11, grado10])  # Añade grado11 y grado10 como hijos de la raíz (orden: primero 11 luego 10).

print("Recorrido por niveles (de mayor a menor grado):")
recorrido_por_niveles(raiz)            # Llama a la función para imprimir el recorrido por niveles iniciando desde la raíz.
