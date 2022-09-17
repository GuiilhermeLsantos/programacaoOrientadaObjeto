#Implemente uma classe Funcionario.

#Crie um programa que utilize esta classe. O programa deve pedir ao usuário o nome e o salário do funcionário 
# e criar um objeto da classe Funcionario. 
#Depois, deve solicitar ao usuário o percentual de aumento e executar o método aumentar_salario. 
# Na sequência deve imprimir o salário do funcionário atualizado.


class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentar_salario(self, percentual):
        self.salario = (self.salario * percentual / 100) + self.salario


n = input("Nome: ")
s = float(input("Salario: "))
funcionario1 = Funcionario(n, s)
p = float(input("Percentual de aumento: "))
funcionario1.aumentar_salario(p)

print("O nome do funcioario: ", funcionario1.nome)
print("O salario do funcionario é: ", funcionario1.salario)