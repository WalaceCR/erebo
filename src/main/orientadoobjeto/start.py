from src.main.orientadoobjeto.conta import Conta

nova_conta = Conta(1, "Luana", 323434545.90, 500000000.90)
nova_conta2 = Conta(1, "Walace", -900000.90, 500000000.90)
nova_conta3 = Conta(1, "Luana e Walace", 323434545.90, 500000000.90)

nova_conta.extrato()
nova_conta.depositar(3234345689.90)
nova_conta.saque(323434000.90)
nova_conta.extrato()
nova_conta2.extrato()
nova_conta2.depositar(3234345689.90)
nova_conta2.saque(0.00)
nova_conta2.extrato()
nova_conta3.extrato()
nova_conta3.depositar(3234345689.90)
nova_conta3.saque(323434000.90)
nova_conta3.extrato()
nova_conta2.transfere(nova_conta2, nova_conta3, 1000.00)
nova_conta3.extrato()

##cada nova execução gera um objeto diferente como exemplo 0x7f5f57f08c50, 0x7f5f57f55555 e etc.
##print("Retornando uma nova conta {} do titular {}".format(nova_conta, nova_conta.titular))
##print("Retornando uma nova conta {} do titular {}".format(nova_conta2, nova_conta2.titular))
##print("Retornando uma nova conta {} do titular {}".format(nova_conta3, nova_conta3.titular))
