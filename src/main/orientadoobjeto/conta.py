
class Conta:

    ##self.__numero(mantenho o acesso ao atributo privado, acesso esse trem apenas pelo método)
    ##construtor da classe, aqui dentro crio as variáveis/atributos da classe
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("Saldo do felizardo {} é de {}".format(self.titular, self.saldo))

    def depositar(self, saldo):
        self.saldo += saldo

    def saque(self, saldo):
        if saldo > self.saldo:
            print("Saldo insuficiente para saque! Operação cancelada!!!")
        else:
            self.saldo -= saldo
