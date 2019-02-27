# dicionário de dados em python

'''conta = {
    "numero" : 123,
    "titular" : "Luana",
    "saldo" : 1242334546.90
}


conta2 = {
    "numero" : 456,
    "titular" : "Walace",
    "saldo" : -1242334546.90
}'''

conta = {"numero": 21332, "titular": "Walace", "saldo": 24.90}


def sacar(conta, saldo):
    print(conta)
    conta["saldo"] -= saldo
    return conta["saldo"]


def depositar(conta, saldo):
    print(conta)
    conta["saldo"] += saldo
    return conta["saldo"]


def extrato(conta):
    print("Saldo atual: {}".format(conta["saldo"]))


sacar(conta, 25)
depositar(conta, 40)
extrato(conta)
