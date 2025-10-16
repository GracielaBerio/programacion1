# Desafío 84: Ordenamiento por selección

def ordenar_por_promedio(lista):
    n = len(lista)                         # Calcula la cantidad de elementos en la lista (número de estudiantes)
    
    for i in range(n):                     # Recorre cada posición de la lista desde el inicio hasta el final
        max_idx = i                        # Supone que el elemento en la posición 'i' tiene el promedio más alto
        for j in range(i+1, n):            # Recorre el resto de la lista (desde i+1 hasta el final)
            # Compara los promedios (índice 1 de cada tupla)
            if lista[j][1] > lista[max_idx][1]:  # Si encuentra un promedio mayor al actual máximo
                max_idx = j                # Actualiza el índice del máximo encontrado
        # Intercambia el elemento actual con el que tiene el promedio más alto encontrado
        lista[i], lista[max_idx] = lista[max_idx], lista[i]

# Lista de estudiantes con sus respectivos promedios (nombre, promedio)
estudiantes = [("Ana", 8.5), ("Luis", 9.2), ("María", 7.8), ("Carlos", 9.5)]

# Llama a la función para ordenar la lista según el promedio (de mayor a menor)
ordenar_por_promedio(estudiantes)

print("Estudiantes ordenados por promedio (descendente):")  # Mensaje informativo antes de mostrar resultados

# Recorre la lista ya ordenada e imprime cada estudiante con su promedio
for e in estudiantes:
    print(e)
