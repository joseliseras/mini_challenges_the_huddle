class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            self._insertar_recursivo(self.raiz, nuevo_nodo)

    def _insertar_recursivo(self, actual, nuevo_nodo):
        if nuevo_nodo.valor < actual.valor:
            if actual.izquierdo is None:
                actual.izquierdo = nuevo_nodo
            else:
                self._insertar_recursivo(actual.izquierdo, nuevo_nodo)
        elif nuevo_nodo.valor > actual.valor:
            if actual.derecho is None:
                actual.derecho = nuevo_nodo
            else:
                self._insertar_recursivo(actual.derecho, nuevo_nodo)

    def imprimir_inorden(self):
        self._imprimir_inorden_recursivo(self.raiz)

    def _imprimir_inorden_recursivo(self, actual):
        if actual is not None:
            self._imprimir_inorden_recursivo(actual.izquierdo)
            print(actual.valor, end=' ')
            self._imprimir_inorden_recursivo(actual.derecho)

# Ejemplo de uso
arbol = ArbolBinarioBusqueda()
valores = [10, 5, 15, 3, 7]

for valor in valores:
    arbol.insertar(valor)

print("Elementos en el árbol en orden inorden:") #imprime en orden ascendente
arbol.imprimir_inorden()

