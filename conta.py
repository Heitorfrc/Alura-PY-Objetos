

class Conta :

    def __init__(self, numero, titular, saldo, limite) -> None:
        print("Construindo Objeto ...{}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

conta = Conta(123, "Heitor", 55.0, 1000.0)

conta2 = Conta(321, "Marco", 100.0, 1000.0)

print(conta.titular)