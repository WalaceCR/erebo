
class Conta:

    ##construtor da classe, aqui dentro crio as variáveis/atributos da classe
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
