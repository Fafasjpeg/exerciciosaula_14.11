class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        self.__saldo = self.__saldo + valor
        


    def sacar(self, valor):
        if (valor>=self.__saldo):            
            print("Saldo Insuficiente")

        else:
            self.__saldo = self.__saldo - valor
            

    def exibir_saldo(self):
        print(f"Saldo: {self.__saldo}")

Conta1 = Conta("Fabio", 100)
Conta1.depositar(50)
Conta1.sacar(30)
Conta1.sacar(89)
Conta1.exibir_saldo()

