class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_detalhes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}!")

carro1= Carro('Mitsubishi', 'v3', 2012)
carro2= Carro('Porshe', 'carrera', 2019)
carro1.exibir_detalhes()
carro2.exibir_detalhes()