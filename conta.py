
class Conta :

    def __init__(self, numero, titular, saldo, limite) -> None:
        print("Construindo Objeto ...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self) :
        print("Saldo de {} reais do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor) :
        self.__saldo += valor

    def saca(self, valor) :
        self.__saldo -= valor

    def transfere(self, valor, destino) :
        self.saca(valor)
        destino.deposita(valor)       

    def get_saldo(self) :
        return self.__saldo
    
    def get_titular(self) :
        return self.__titular
    
    def get_limite(self) :
        return self.__limite
    
    def set_limite(self, novo_limite) :
        self.__limite = novo_limite



conta = Conta(123, "Heitor", 55.0, 1000.0)

conta2 = Conta(321, "Marco", 100.0, 1000.0)

conta.transfere(15.0, conta2)

conta.extrato()

conta2.extrato()

conta.get_saldo()

conta.get_limite()

conta.get_titular()

conta.set_limite(2000.0)

print(conta._Conta__titular)

print(conta._Conta__limite)
