#Exercício 01
#Preencha uma lista com 10 números inteiros digitados pelo usuário e exiba:
#a) o maior número da lista
#b) o menor número da lista
#c) a média dos números contidos na lista

lista = []

for a in range(10):
    lista.append(int(input("Digite os numeros: ")))

maior = max(lista)
print(maior)
menor = min(lista)
print (menor)
soma = sum(lista)//10
print(soma)


