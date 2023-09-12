

class Conta :

    def __init__(self, numero, titular, saldo, limite) -> None :
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

    @property
    def saldo(self) :
        return self.__saldo
    
    @property
    def titular(self) :
        return self.__titular
    
    @property
    def limite(self) :
        return self.__limite
    
    @limite.setter
    def limite(self, limite) :
        self.__limite = limite


    


conta = Conta(123, "Heitor", 55.0, 1000.0)

conta2 = Conta(321, "Marco", 100.0, 1000.0)

conta.transfere(15.0, conta2)

conta.extrato()

conta2.extrato()

print(conta.saldo)

print(conta.titular)

conta.limite = 2000.0

print(conta._Conta__titular)

print(conta.limite)
