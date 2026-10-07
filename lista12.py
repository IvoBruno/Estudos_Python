class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False

    def ligar_desligar(self):
        self.ligado = not self.ligado
        if(self.ligado):
            print(f"O carro {self.marca} {self.modelo} está ligado.")
        else:
            print(f"O carro {self.marca} {self.modelo} está desligado.")
        

class Eletrico(Carro):
    def __init__(self, marca, modelo, autonomia):
        super().__init__(marca, modelo)
        self.autonomia = autonomia

    def ligar_desligar(self):
        self.ligado = not self.ligado
        if self.ligado:
            print(f"O carro elétrico {self.marca} {self.modelo} está desligado.")
        else:
            print(f"O carro elétrico {self.marca} {self.modelo} está ligado com autonomia de {self.autonomia} km.")

if __name__ == "__main__":
    pessoa1 = Pessoa("João", 30)
    pessoa1.falar()

    carro1 = Carro("Toyota", "Corolla")
    carro1.ligar_desligar()
    carro1.ligar_desligar()

    carro_eletrico = Eletrico("Tesla", "Model S", 500)
    carro_eletrico.ligar_desligar()
    carro_eletrico.ligar_desligar()

    familia = []
    familia.append(Pessoa("Antonio", 30))
    familia.append(Pessoa("Barbara", 28))
    familia.append(Pessoa("Carlos", 5))
    familia.append(Pessoa("Denise", 2))
    for pessoa in familia:
        pessoa.falar()
