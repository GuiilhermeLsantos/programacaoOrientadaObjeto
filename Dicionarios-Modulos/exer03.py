# Escreva uma função que conta a quantidade de vogais em um texto e armazena tal quantidade em um dicionário,
# onde a chave é a vogal e o valor é a quantidade de vezes que essa vogal aparece no texto. 
# A função deve receber o texto como parâmetro de entrada, e retornar o dicionário.

# Exemplo: 
# Para o texto abaixo:
#'faculdade de tecnologia impacta'
# A função deve retornar o seguinte dicionário:
# {'a': 5, 'u': 1, 'e': 3, 'o': 2, 'i': 2}

# exemplo de como percorrer uma string
# texto = 'faculdade de tecnologia impacta'
# for caractere in texto:
#   if caractere == 'a':	


def conta_vogais(texto):
    dicionario = {}
    lista_vogais = 'aeiou'

    for letra in texto: # percorre caracter
        letra = letra.lower() # converte em minusculo
        if letra in lista_vogais:  # se é uma vogal
            if letra in dicionario: # se está no dicionario 
                dicionario[letra] += 1
            else:
                dicionario[letra] = 1
    return dicionario

texto = 'faculdade de tecnologia impacta'
dicionario = conta_vogais(texto)
print(dicionario)
