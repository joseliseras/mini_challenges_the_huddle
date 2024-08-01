class Motor:
    def __init__(self, tipo, caballos_de_fuerza):
        self.tipo = tipo  # Tipo de motor, como "gasolina", "diesel", "eléctrico"
        self.caballos_de_fuerza = caballos_de_fuerza  # Potencia del motor

    def describir_motor(self):
        # Método que imprime la descripción del motor
        return f"Motor de tipo {self.tipo} con {self.caballos_de_fuerza} caballos de fuerza."

class Auto:
    def __init__(self, marca, modelo, tipo_motor, caballos_de_fuerza):
        self.marca = marca
        self.modelo = modelo
        # Crear una instancia de Motor como parte del Auto
        self.motor = Motor(tipo_motor, caballos_de_fuerza)

    def describir_auto(self):
        # Método para describir el auto, incluyendo los detalles del motor
        descripcion_motor = self.motor.describir_motor()
        return f"Auto {self.marca} modelo {self.modelo}, equipado con un {descripcion_motor}"

# Ejemplo de uso
mi_auto = Auto("Toyota", "Corolla", "gasolina", 132)
print(mi_auto.describir_auto())
