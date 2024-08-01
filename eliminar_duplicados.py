def eliminar_duplicados(lista):
    # Convertir la lista a un conjunto para eliminar duplicados
    conjunto_sin_duplicados = set(lista)
    # Convertir el conjunto de vuelta a una lista
    lista_sin_duplicados = list(conjunto_sin_duplicados)
    return lista_sin_duplicados

# Ejemplo de uso de la función
lista_original = [1, 2, 3, 4, 5, 2, 3, 4, 5, 5]
lista_sin_duplicados = eliminar_duplicados(lista_original)
print("Lista original:", lista_original)
print("Lista sin duplicados:", lista_sin_duplicados)
