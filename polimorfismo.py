
class Conta :

    def __init__(self, codigo) :
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor_depositado) :
        self._saldo += valor_depositado

    def __str__(self) -> str:
        return "O código da conta é {}, e o saldo da conta é {}".format(self._codigo, self._saldo)
        

class ContaCorrente(Conta) :
    
    def passa_o_mes(self) :
        self._saldo -= 2


class ContaPoupanca(Conta) :

    def passa_o_mes(self) :
        self._saldo *= 1.01
        self._saldo -= 3

'''
conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta16.passa_o_mes()
print(conta16)

conta17 = ContaPoupanca(17)
conta17.deposita(1000)
conta17.passa_o_mes()
print(conta17)
'''

# outra maneira de instanciar

conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta17 = ContaPoupanca(17)
conta17.deposita(1000)

contas = [conta16, conta17]

for conta in contas :
    conta.passa_o_mes()
    print(conta)

