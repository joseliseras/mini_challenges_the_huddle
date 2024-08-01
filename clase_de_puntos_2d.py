class Punto2D:
    def __init__(self, x, y):
        # Constructor que inicializa las coordenadas x e y del punto.
        self.x = x
        self.y = y

    def __repr__(self):
        # Representación en cadena que facilita la visualización de las coordenadas del punto.
        return f"(x={self.x}, y={self.y})"

    def imprimir_coordenadas(self):
        # Método que imprime las coordenadas del punto.
        print(f"Coordenadas del punto: (x={self.x}, y={self.y})")

def crear_matriz_de_puntos(tamano):
    # Crea una matriz de objetos Punto2D donde cada punto representa sus índices en la matriz
    return [[Punto2D(x, y) for x in range(tamano)] for y in range(tamano)]

def imprimir_matriz(matriz):
    # Imprime la matriz con un formato legible
    for fila in matriz:
        for punto in fila:
            print(punto, end=' ')
        print()  # Salto de línea después de cada fila

# Crear una matriz de puntos 10x10
matriz_de_puntos = crear_matriz_de_puntos(10)

# Imprimir la matriz de puntos
print("Matriz de Puntos 2D:")
imprimir_matriz(matriz_de_puntos)

# Ejemplo de cómo imprimir las coordenadas de un punto específico (p.ej., en la posición [2][3])
print("\nCoordenadas de un punto específico (2,3):")
matriz_de_puntos[2][3].imprimir_coordenadas()
