from conta import Conta
from poupanca import Poupanca
from corrente import Corrente

# conta1 = Conta("125", "355", 500)
# print(conta1.saldo)
# conta1.depositar(10)
# print(conta1.saldo)
# conta1.sacar(20)
# print(conta1.saldo)
# conta1.sacar(500)
# print(conta1.saldo)

# poupanca1 = Poupanca("125", "355", 500)
# print(poupanca1.saldo)
# poupanca1.depositar(100)
# print(poupanca1.saldo)

corrente1 = Corrente("135", "355", 500)
print(corrente1.saldo)
corrente1.sacar(100)
print(corrente1.saldo)