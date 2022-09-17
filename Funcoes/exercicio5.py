def calcular_salario (a):
    if a > 2000:
        salario = a + (a * 0.07)

    else:
        salario = a + (a * 0.15)

    return salario

a = float(input())

print (calcular_salario(a))

