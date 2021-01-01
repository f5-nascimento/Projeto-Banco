class Conta:

    def __init__(self, numero, agencia, saldo):

        self.numero = numero
        self.agencia = agencia
        self.saldo = saldo

    def sacar(self, saque):
        if saque > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo = self.saldo - saque

    def depositar(self, deposito):
        self.saldo = self.saldo + deposito

