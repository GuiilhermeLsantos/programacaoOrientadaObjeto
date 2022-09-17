#O código abaixo lança uma exceção e interrompe a execução do programa. 
#Utilizando tratamento de exceções, corrija o programa com o objetivo de alertar o usuário sobre o erro ocorrido, 
# e impedir que o programa seja interrompido bruscamente.


from logging import exception


try:
    def funcao_1():
        print('Início da função')
        lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for i in range(15):
            print(lista[i])
        print('Fim da função')
    
    print('Início do programa')
    funcao_1()
    print('Fim do programa')
except IndexError:
    print('Erro:! O numero de indice na função é Maior que a Lista')
except Exception:
    print('Algo de errado não está certo')
finally:
    print('Fim do Programa')