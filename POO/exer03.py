#Implemente a classe Televisao.

#Faça um programa para criar um objeto da classe Televisao e testar a sua classe.
# Veja abaixo um trecho de programa que utiliza a classe:


class Televisão:
    def __init__(self):

        self.canal = None     # valor pre definido
        self.volume = 0       # valor pre definido
        

    def aumentar_volume(self):
        self.volume +=1

    def diminuir_volume(self):
        self.volume -=1 

    def alterar_canal(self, canal ):
        self.canal = canal

tv = Televisão()
tv.alterar_canal(5)
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.diminuir_volume()
print(f'A tv está no canal {tv.canal}')             # A tv está no canal 5
print(f'A tv está no volume {tv.volume}')           # A tv está no volume 2

