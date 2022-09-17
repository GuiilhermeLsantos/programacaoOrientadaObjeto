#Implemente a função soma_divisores, que recebe como parâmetro de entrada um número positivo e retorna a soma de todos os divisores desse número.

#Por exemplo:
# - caso o número seja 15, o retorno deve ser 24 (1 + 3 + 5 + 15).
# - caso o número seja 30, o retorno deve ser 72 (1 + 2 + 3 + 5 + 6 + 10 + 15 + 30)

def soma_divisores(n):
    soma = 0
    for a in range(1, n+1):
        if n % a == 0:
            soma = soma + a
    return soma

a = int(input('Informe um número inteiro: '))
print(soma_divisores(a))
