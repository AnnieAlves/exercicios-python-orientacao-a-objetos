# O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres.
# Modele um sistema orientado a objetos para representar contas correntes do Banco Delas seguindo os requisitos abaixo.

# 1. Cada conta corrente pode ter um ou mais clientes como titular.
# 2. O banco controla apenas o nome, o telefone e a renda mensal de cada cliente.
# 3. A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos.
#    Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente. Quando ela
#    fizer um depósito, aumentaremos o saldo.
# 4. Clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda
#    mensal, ou seja, elas podem sacar valores que deixam a sua conta com valor negativo até
#    -renda_mensal.
# 5. Clientes homens por enquanto não têm direito a cheque especial.

# Para modelar seu sistema, utilize obrigatoriamente os conceitos "classe", "herança", "propriedades",
# "encapsulamento" e "classe abstrata"


from abc import ABC, abstractmethod
class Cliente(ABC):

    def __init__(self, nome, telefone, renda, id):
        self.nome = nome
        self.telefone = telefone
        self.renda = renda
        self.id = id

    @abstractmethod
    def get_limite(self):
        pass

    def pode_sacar(self, conta, valor):
        if any(self.id == cliente.id for cliente in conta.titulares):
            if (conta.saldo - valor) >= conta.get_limite_conta():
                return True
            else:
                print("\033[91mSaldo insuficiente\033[0m")
        else:
            print("\033[91mSomente titulares da conta podem realizar saques\033[0m")

    def sacar(self, conta, valor):
        if self.pode_sacar(conta, valor):
            conta.saldo -= valor
            conta.operacoes.append(f"Saque realizado no valor de R${valor:.2f}")
            print(f"Saldo na conta: R${conta.saldo:.2f}")

    def depositar(self, conta, valor):
        conta.saldo += valor
        conta.operacoes.append(f"Depósito realizado no valor de R${valor:.2f}")
        print(f"Saldo na conta: R${conta.saldo:.2f}")


class ClienteMulher(Cliente):
    def __init__(self, nome, telefone, renda, id):
        super().__init__(nome, telefone, renda, id)

    def get_limite(self):
        return -self.renda



class ClienteHomem(Cliente):
    def __init__(self, nome, telefone, renda, id):
        super().__init__(nome, telefone, renda, id)

    def get_limite(self):
        return 0



class ContaCorrente:
    def __init__(self, titulares):
        self.titulares = titulares
        self.saldo = 0
        self.operacoes = []

    def get_limite_conta(self):
        limite = 0
        for titular in self.titulares:
            limite += titular.get_limite()
        return limite


aline = ClienteMulher("Aline", "920008289", 6000, 1)
alan = ClienteHomem("Alan", "997715704", 5000, 44)

cris = ClienteMulher("Cris", "922026022", 4000, 17)
luana = ClienteMulher("Luana", "901140566", 4000, 11)

conta_01 = ContaCorrente([aline, alan])
conta_02 = ContaCorrente([cris, luana])

print(conta_01.get_limite_conta())
print(conta_02.get_limite_conta())


aline.depositar(conta_01, 3000)
alan.sacar(conta_01, 5000)
aline.sacar(conta_01, 8000)
print(f"\n{conta_01.operacoes}\n")


cris.depositar(conta_02, 10000)
luana.sacar(conta_01, 2500)
luana.sacar(conta_02, 25000)












