# Desafío 82: Búsqueda secuencial en matriz

def buscar_calificacion(tabla, valor_buscado):
    # Recorre cada fila de la tabla junto con su índice 'i'
    for i, fila in enumerate(tabla):
        # Recorre cada elemento (calificación) de la fila con su índice 'j'
        for j, calificacion in enumerate(fila):
            # Compara si la calificación actual coincide con el valor buscado
            if calificacion == valor_buscado:
                return i, j  # Si la encuentra, devuelve las posiciones (índice de estudiante, índice de materia)
    return None  # Si no se encuentra el valor en toda la matriz, devuelve None

# tabla [estudiantes x materias]
# Cada fila representa a un estudiante y cada columna a una materia.
tabla = [
    [8, 7, 9],   # Calificaciones del Estudiante 0
    [6, 10, 8],  # Calificaciones del Estudiante 1
    [7, 7, 6]    # Calificaciones del Estudiante 2
]

# Llamada a la función buscando la calificación 10
resultado = buscar_calificacion(tabla, 10)

# Verifica si la función devolvió una posición (es decir, si encontró el valor)
if resultado:
    # Si encontró la calificación, muestra en qué estudiante (fila) y materia (columna) se encuentra
    print(f"Calificación encontrada en Estudiante {resultado[0]}, Materia {resultado[1]}")
else:
    # Si no la encontró, muestra un mensaje indicándolo
    print("Calificación no encontrada.")
    
    
    # Desafío 82

def buscar_valor(tabla, valor):
    # La función busca de manera secuencial un valor dentro de una matriz (lista de listas).
    # Si lo encuentra, devuelve una tupla (i, j) con la posición:
    #   i → índice de la fila (estudiante)
    #   j → índice de la columna (materia)
    # Si no lo encuentra, devuelve None.

    return next(                              # 'next()' devuelve el primer elemento de un generador.
        (                                     # Abre la expresión generadora.
            (i, j)                            # Valor a devolver por cada coincidencia: una tupla con índices (fila, columna).
            for i, f in enumerate(tabla)      # Recorre las filas de la tabla con su índice 'i' (enumerate da índice y fila).
            for j, v in enumerate(f)          # Recorre cada valor 'v' dentro de la fila 'f', junto con su índice 'j'.
            if v == valor                     # Condición: solo genera la tupla (i, j) si el valor coincide con el buscado.
        ),
        None                                  # Valor por defecto que devuelve 'next()' si no se encuentra ninguna coincidencia.
    )

