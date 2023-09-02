# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.


class Carro:

    def __init__(self, cor, modelo):
        self.ligado = False
        self.cor = cor
        self.modelo = modelo
        self.velocidade = 0
        self.velocidade_max = 200

    def liga(self):
        if not self.ligado:
            self.ligado = True
            print("\nO carro foi ligado\n")
        else:
            print("\nO carro já está ligado\n")

    def desliga(self):
        if self.velocidade > 0:
            print("Para desligar o carro primeiro pare-o")
            return
        else:
            if self.ligado:
                self.ligado = False
                self.velocidade = 0
                print("\nO carro foi desligado\n")
            else:
                print("\nO carro já está desligado\n")

    def acelera(self):
        if not self.ligado:
            print("\nPara acelerar ligue o carro\n")
            return
        else:
            if self.velocidade < self.velocidade_max:
                self.velocidade += 5
                print(f"Velocidade atual: {self.velocidade}km/h")
            else:
                print(f"\nO carro já está na velocidade máxima ({self.velocidade_max}km/h)\n")



    def desacelera(self):
        if not self.ligado:
            print("\nNão é possivel desacelerar pois o carro está desligado\n")
        else:
            if self.velocidade > 0:
                self.velocidade -= 5
                print(f"Velocidade atual: {self.velocidade}km/h")
                if self.velocidade == 0:
                    print("O carro parou.")
            else:
                print("\nO carro já está parado\n")



    def __str__(self) -> str:
        estado_motor = "ligado" if self.ligado else "desligado"
        return (f'O carro {self.modelo} da cor {self.cor} está  {estado_motor} há {self.velocidade}km/h')


# Crie uma instância da classe carro.

meu_carro = Carro(cor="Cinza", modelo="R19")

# Faça o carro "andar" utilizando os métodos da sua classe.

meu_carro.liga()

for _ in range(41):
    meu_carro.acelera()

print(f"\n {meu_carro} \n")

# Faça o carro "parar" utilizando os métodos da sua classe.

while meu_carro.velocidade > 0:
    meu_carro.desacelera()

print(f"\n {meu_carro} \n")



