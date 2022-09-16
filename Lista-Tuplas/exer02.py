#Preencha uma lista com 10 números inteiros digitados pelo usuário e exiba:
#a) a quantidade de números pares contidos na lista
#b) o somatório de todos os números ímpares contidos na lista.

lista = []

numeros_pares = 0
somatorio = 0

for a in range(10):
    lista.append(int(input("Digite os numeros: ")))

for a in lista :
    if a %2==0:
        numeros_pares +=1
    
    else :
        somatorio += a

print(numeros_pares)
print(somatorio)

        
