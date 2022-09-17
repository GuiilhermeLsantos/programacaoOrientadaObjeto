class ContaBancaria:

    def __init__(self, numero, titular, senha):

        self.numero = numero
        self.titular = titular
        self.senha = senha
        self.saldo = 0 

    def depositar(self, valor, senha):
        if self.senha == senha:
            self.saldo = self.saldo + valor
            print("Deposito realizado com sucesso")
        else:
            print("Senha incorreta")

    def sacar(self, valor, senha):
        if self.senha == senha:
            self.saldo = self.saldo - valor 
            print("Saque realizado com sucesso")
        else:
            print("Senha incorreta")


conta = ContaBancaria(1234, "Guilherme", 9964)
print(conta.saldo)

valor = float(input("Valor para deposito: "))
senha = int(input("Informe a senha: "))
conta.depositar(valor, senha)
print(conta.saldo)


valor = float(input("Valor para saque: "))
senha = int(input("Informe a senha: "))
conta.sacar(valor, senha)
print(conta.saldo)





    