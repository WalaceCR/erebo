
class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        print("Pegando o nome!!!")
        return self.__nome

    @nome.setter
    def nome(self, nome):
        print("Alterando o nome!!!")
        self.__nome = nome
