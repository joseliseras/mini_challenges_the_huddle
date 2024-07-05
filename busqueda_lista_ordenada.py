def busqueda_binaria(lista,buscado):
    inicio = 0
    final = len(lista)  

    while inicio <= final:
        medio = (inicio + final) // 2 
        if lista[medio] == buscado:
            return medio
        elif lista[medio] < buscado:
            inicio = medio + 1 
        else:
            final = medio -1 
    return None

lista = [2,4,6,7,9,12,14,17,20,21]

buscado = 14

resultado = busqueda_binaria(lista,buscado)

if resultado == None:
    print(f"El elemento {buscado} no se encuentra en la lista")
else:
    print(f"El elemento {buscado} se encuentra en la poscion {resultado}")

