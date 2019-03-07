
class Conta:

    ##self.__numero(mantenho o acesso ao atributo privado, acesso esse trem apenas pelo método)
    ##construtor da classe, aqui dentro crio as variáveis/atributos da classe
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo do felizardo {} é de {}".format(self.__titular, self.__saldo))

    def depositar(self, saldo):
        self.__saldo += saldo

    def saque(self, saldo):
        if saldo > self.__saldo:
            print("Saldo insuficiente para saque! Operação cancelada!!!")
        else:
            self.__saldo -= saldo
