#Crie dois objetos da classe Funcionario
#Utilize o método aumentar_salario para atualizar os salários dos funcionários
#Método construtor. Deve fazer uma validação do salário e, se o salário informado for negativo, deve definí-lo como zero.
#Aumentar o salário do funcionário em 10%.
class Funcionario:
    def __init__(self, nome, sobrenome, salario):

        self.nome = nome
        self.sobrenome = sobrenome
        self.salario = salario

    def aumentar_salario(self):
        if self.salario < 0:
            self.salario = 0.0
        else:
           self.salario = self.salario * 0.10 + self.salario 

func1 = Funcionario('Paulo', 'Vieira', 2000)
func2 = Funcionario('Maria', 'Silva', -4000)

func1.aumentar_salario()
func2.aumentar_salario()

print('Salario: ', func1.salario)
print('Salario: ', func2.salario)    


