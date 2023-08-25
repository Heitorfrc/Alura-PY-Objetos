

class Conta :

    def __init__(self, numero, titular, saldo, limite) -> None:
        print("Construindo Objeto ...{}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self) :
        print("Saldo de {} reais do titular {}".format(self.saldo, self.titular))

    def deposita(self, valor) :
        self.saldo += valor

    def saca(self, valor) :
        self.saldo -= valor



conta = Conta(123, "Heitor", 55.0, 1000.0)

conta2 = Conta(321, "Marco", 100.0, 1000.0)

conta.saca(15.0)

conta.extrato()

print(conta.titular)
