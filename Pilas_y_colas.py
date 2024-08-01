class Pila:
    def __init__(self):
        self.elementos = []

    def insertar(self, elemento):
        if len(self.elementos) < 5:
            self.elementos.append(elemento)
        else:
            print("La pila está llena")

    def eliminar(self):
        if self.elementos:
            return self.elementos.pop()
        else:
            print("La pila está vacía")
            return None

    def mostrar(self):
        print("Elementos en la pila:")
        for elemento in reversed(self.elementos):
            print(elemento)

# Ejemplo de uso de la Pila
pila = Pila()
pila.insertar('a')
pila.insertar('b')
pila.insertar('c')
pila.insertar('d')
pila.insertar('e')
pila.mostrar()
print("Elemento eliminado:", pila.eliminar())
pila.mostrar()
