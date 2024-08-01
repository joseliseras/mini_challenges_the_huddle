from math import pi

class Figura:
    def imprimir(self):
        # Método que debería ser implementado por las clases derivadas
        raise NotImplementedError("Este método debe ser sobrescrito por subclases")

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def imprimir(self):
        # Implementación específica para Círculo
        area = pi * self.radio ** 2
        perimetro = 2 * pi * self.radio
        print(f"Círculo de radio {self.radio}")
        print(f"Área: {area:.2f}")
        print(f"Perímetro: {perimetro:.2f}")

# Ejemplo de uso
circulo = Circulo(5)
circulo.imprimir()
