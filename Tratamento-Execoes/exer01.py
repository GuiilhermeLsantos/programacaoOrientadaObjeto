#Nesta questão você deve identificar as partes problemáticas do código
#  e reescrevê-lo utilizando tratamento de exceções. 
#Ou seja, devem ser identificadas todas as exceções que podem ser geradas e, para cada uma,
# deve ser dado o tratamento adequado que, nesse exercício, significa alertar o usuário quanto ao problema. 


try:
    x = int(input('Primeiro valor:'))
    y = int(input('Segundo valor:'))
    z = x / y
    print('O resultado da divisão é:', z)

except ZeroDivisionError:
    print('O valor não pode ser 0')
except ValueError:
    print('O valor informado é invalido')
except Exception:
    print('Algo de errado não está certo!')
else:
    print('Fim do Programa!!!')