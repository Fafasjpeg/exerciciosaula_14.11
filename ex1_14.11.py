class Pessoa:
    def __init__(self, nome, idade):
        self.nome=nome
        self.idade=idade

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

p1 = Pessoa ("Maria", 67)
p2 = Pessoa ("joão", 39)
p1.exibir_informacoes()
p2.exibir_informacoes()