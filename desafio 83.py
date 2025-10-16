# Desafío 83: Búsqueda binaria
def busqueda_binaria(lista, objetivo):
    inicio, fin = 0, len(lista) - 1          # inicializa los índices izquierdo (inicio) y derecho (fin)
    while inicio <= fin:                     # mientras el intervalo sea válido (aún haya elementos por revisar)
        medio = (inicio + fin) // 2          # calcula el índice medio (división entera)
        if lista[medio] == objetivo:         # si el elemento medio es el objetivo
            return medio                     # devuelve el índice donde se encontró
        elif lista[medio] < objetivo:        # si el valor medio es menor que el objetivo
            inicio = medio + 1               # desplaza el límite izquierdo a la derecha (buscar en la mitad superior)
        else:                                # en cualquier otro caso (lista[medio] > objetivo)
            fin = medio - 1                  # desplaza el límite derecho a la izquierda (buscar en la mitad inferior)
    return -1                                # si sale del bucle, el objetivo no está: devuelve -1

estudiantes = ["Ana", "Carlos", "Luis", "María", "Sofía"]  # lista ordenada de ejemplo (requisito para binaria)
nombre_buscado = "Luis"                                   # valor a buscar
indice = busqueda_binaria(estudiantes, nombre_buscado)    # llamada a la función
if indice != -1:                                          # si el índice no es -1 significa que se encontró
    print(f"{nombre_buscado} encontrado en la posición {indice}")  # imprime la posición encontrada
else:
    print(f"{nombre_buscado} no está en la lista.")      # si no se encontró, informa al usuario

def binaria(lst, x):
    i, j = 0, len(lst)-1                    # inicializa i (inicio) y j (fin)
    while i <= j:                           # mientras el intervalo [i, j] sea válido
        m = (i+j)//2                        # calcula el medio m
        if lst[m]==x: return m              # si coincide, devuelve el índice m inmediatamente
        if lst[m]<x: i=m+1                  # si el medio es menor que x, mover i a la derecha
        else: j=m-1                         # si el medio es mayor que x, mover j a la izquierda
    return -1                               # si no se encuentra, devuelve -1
