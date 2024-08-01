class ColaDePrioridad:
    def __init__(self):
        self.cola = []

    def insertar(self, elemento, prioridad):
        # Inserta un elemento en la cola con su prioridad
        self.cola.append((prioridad, elemento))
        self.cola.sort(reverse=True)  # Ordenamos de mayor a menor prioridad

    def eliminar(self):
        # Elimina el elemento con la mayor prioridad
        if self.cola:
            return self.cola.pop(0)[1]  # Devuelve solo el elemento, sin la prioridad
        else:
            print("La cola está vacía")
            return None

    def mostrar(self):
        # Muestra todos los elementos en la cola con sus prioridades
        if not self.cola:
            print("La cola está vacía")
        else:
            for prioridad, elemento in self.cola:
                print(f"Elemento: {elemento}, Prioridad: {prioridad}")

# Crear una instancia de la cola de prioridad
cola = ColaDePrioridad()

# Insertamos elementos
cola.insertar("elemento1", 5)
cola.insertar("elemento2", 1)
cola.insertar("elemento3", 3)
cola.insertar("elemento4", 2)
cola.insertar("elemento5", 4)

# Mostramos los elementos en la cola
print("Estado inicial de la cola:")
cola.mostrar()

# Eliminamos los elementos uno a uno y mostramos el estado de la cola
for i in range(5):
    eliminado = cola.eliminar()
    if eliminado:
        print(f"\nElemento eliminado: {eliminado}")
        print("Estado de la cola después de eliminar:")
        cola.mostrar()
