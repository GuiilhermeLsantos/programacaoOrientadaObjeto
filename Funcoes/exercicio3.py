#Implemente a função soma_dos_quadrados que receba dois numeros e devolve a soma dos seus quadrados.

def quadrado (a,b):
    c = a**2
    z = b**2
    soma = c + z
    return soma

a = int(input())
b = int(input())

print (quadrado(a,b))
