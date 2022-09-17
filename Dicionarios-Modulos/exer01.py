# Preencha um dicionário com as informações de 5 produtos.
#  - Utilize o nome do produto como chave e o preço como valor. 
#  - Solicite os dados ao usuário.
# Percorra o dicionário e exiba o nome dos produtos com preço superior a R$ 50.00

#Exemplo:
# Veja um exemplo da estrutura do dicionário.
# {'Caneta': 3.0, 'Pen Drive': 100.0, 'Teclado': 30.0}

produtos = {}

for n in range(5):
    nome = input("Digite um Nome: ")
    preco = float (input("Digite um Preco: "))
    produtos [nome] = preco

for nome in produtos:
    if produtos[nome] >= 50.00:
        print(nome)
    

