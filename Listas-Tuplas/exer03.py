#Preencha uma lista com 10 números digitados pelo usuário. 
#A partir desta lista, gere uma lista com os números pares e outra com os números ímpares. 

#Exemplo: 
#Suponha que a lista digitada seja: [1, 4, 7, 9, 5, 3, 7, 9, 8, 8]. 
#Para esta lista, o programa deve gerar as seguintes listas:
#[4, 8, 8]
#[1, 7, 9, 5, 3, 7, 9]

lista = []

pares = []
impares = []

for a in range(10):
    lista.append(int(input("Digite os numeros: ")))

for a in lista:
    if a %2==0:
        pares.append(a)

    else:
        impares.append(a)

print(pares)
print(impares)
