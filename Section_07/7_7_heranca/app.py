class Veiculo:
    def __init__(self, rodas, marca):
        self.rodas = rodas
        self.marca = marca

    def ligar(self):
        print("Vruummmm!")

class Carro(Veiculo):
    def __init__(self, rodas, marca, teto_solar):
        super().__init__(rodas, marca)
        self.teto_solar = teto_solar

ferrari = Carro(4, "Ferrari", True)

print(ferrari.marca)

ferrari.ligar()

print(ferrari.teto_solar)

class Moto(Veiculo):
    def __init__(self, rodas, marca, protecao_lateral):
        super().__init__(rodas, marca)
        self.protecao_lateral = protecao_lateral

    def empinar(self):
        print("Empinou!!!")

moto = Moto(2, "Honda", False)

print(moto.marca)

moto.ligar()

moto.empinar()