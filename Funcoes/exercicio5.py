#Implemente a função calcular_salario, que recebe o salário atual de um funcionário e retorna o salário com um reajuste de aumento, sendo que:
# - Caso o salário seja maior que R$ 2.000,00, o funcionário receberá 7% de aumento.
# - Caso contrário, o funcionário receberá 15% de aumento.

def calcular_salario (a):
    if a > 2000:
        salario = a + (a * 0.07)

    else:
        salario = a + (a * 0.15)

    return salario

a = float(input())

print (calcular_salario(a))

