def ord_burbuja(arreglo):
    n = len(arreglo)

    for i in range(n-1):       # <-- bucle padre
        print(f"{i+1} Recorrido (i = {i})")
        for j in range(n-1-i): # <-- bucle hijo
            print("j =", j)
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]

elementos = [19, 3, 1, 8, 14]
ord_burbuja(elementos)

print(elementos)