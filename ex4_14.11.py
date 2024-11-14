class Animal:
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        print("Au Au")

class Gato(Animal):
    def emitir_som(self):
        print("Miau")

cachorro1= Cachorro()
gato1= Gato()
cachorro1.emitir_som()
gato1.emitir_som()