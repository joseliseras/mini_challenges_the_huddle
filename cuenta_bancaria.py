class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        # Constructor que inicializa el titular de la cuenta y el saldo inicial.
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self):
        # Método para depositar dinero en la cuenta.
        monto = float(input("Ingrese el monto a depositar: "))
        if monto > 0:
            self.saldo += monto
            print(f"Depósito realizado: {monto} Guaranies")
        else:
            print("El monto a depositar debe ser positivo.")
        self.consultar_saldo()

    def retirar(self):
        # Método para retirar dinero de la cuenta.
        monto = float(input("Ingrese el monto a retirar: "))
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro realizado: {monto} Guaranies")
        else:
            print("Fondos insuficientes o monto inválido.")
        self.consultar_saldo()

    def consultar_saldo(self):
        # Método para consultar el saldo actual de la cuenta.
        print(f"Saldo actual de {self.titular}: {self.saldo} Guaranies")

# Ejemplo de uso de la clase CuentaBancaria
def main():
    titular = input("Ingrese el nombre del titular de la cuenta: ")
    saldo_inicial = float(input("Ingrese el saldo inicial de la cuenta: "))
    cuenta = CuentaBancaria(titular, saldo_inicial)

    while True:
        print("\nOpciones:")
        print("1. Depositar dinero")
        print("2. Retirar dinero")
        print("3. Consultar saldo")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            cuenta.depositar()
        elif opcion == '2':
            cuenta.retirar()
        elif opcion == '3':
            cuenta.consultar_saldo()
        elif opcion == '4':
            print("Gracias por utilizar el sistema bancario.")
            break
        else:
            print("Opción inválida. Por favor, elija una opción del 1 al 4.")

if __name__ == "__main__":
    main()
