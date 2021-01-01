from conta import Conta

class Corrente(Conta):

    def __init__(self, numero, agencia, saldo):
        Conta.__init__(self, numero, agencia, saldo)

    def sacar(self, saque):
        if saque > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo = (self.saldo - saque) * 0.90

    def depositar(self, deposito):
        self.saldo = self.saldo + deposito
