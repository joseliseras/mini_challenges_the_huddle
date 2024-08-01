class Animal:
    def hacerSonido(self):
        # Método genérico para hacer un sonido
        print("Este animal hace un sonido.")

class Perro(Animal):
    def hacerSonido(self):
        # Sobrescritura del método para hacer el sonido específico de un perro
        print("Guau guau!")

class Gato(Animal):
    def hacerSonido(self):
        # Sobrescritura del método para hacer el sonido específico de un perro
        print("miau miau!")

# Ejemplo de uso
animal_generico = Animal()
animal_generico.hacerSonido()

perro = Perro()
perro.hacerSonido()

animal_generico.hacerSonido()
gato= Gato()
gato.hacerSonido()
