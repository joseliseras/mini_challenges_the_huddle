from math import pi
from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

class Rectangulo(FormaGeometrica):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

    def calcular_perimetro(self):
        return 2 * (self.ancho + self.alto)

class Circulo(FormaGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * pi * self.radio

# Ejemplo de uso
rectangulo = Rectangulo(10, 20)
print(f"Área del rectángulo: {rectangulo.calcular_area()} unidades cuadradas")
print(f"Perímetro del rectángulo: {rectangulo.calcular_perimetro()} unidades")

circulo = Circulo(5)
print(f"Área del círculo: {circulo.calcular_area():.2f} unidades cuadradas")
print(f"Perímetro del círculo: {circulo.calcular_perimetro():.2f} unidades")
