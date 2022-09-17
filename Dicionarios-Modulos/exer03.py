# Escreva uma função que conta a quantidade de vogais em um texto e armazena tal quantidade em um dicionário,
# onde a chave é a vogal e o valor é a quantidade de vezes que essa vogal aparece no texto. 
# A função deve receber o texto como parâmetro de entrada, e retornar o dicionário.

# Exemplo: 
# Para o texto abaixo:
#'faculdade de tecnologia impacta'
# A função deve retornar o seguinte dicionário:
# {'a': 5, 'u': 1, 'e': 3, 'o': 2, 'i': 2}


def conta_vogais(texto):
    dicionario = {}
    lista_vogais = 'aeiou'

    for letra in texto:
        letra = letra.lower()
        if letra in lista_vogais:
            if letra in dicionario: 
                dicionario[letra] += 1
            else:
                dicionario[letra] = 1
    return dicionario

texto = 'faculdade de tecnologia impacta'
dicionario = conta_vogais(texto)
print(dicionario)
