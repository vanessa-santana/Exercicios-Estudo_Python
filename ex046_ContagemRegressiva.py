#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

#imprimindo cabeçalho
print('{:=^40}'.format(' 2020 '))

#pausa de 1 segundo 
sleep(1)

#imprimindo cabeçalho
print('CONTAGEM REGRESSIVA PARA 2021')

#laço que começa em 10 ate 0 com passo -1

for cont in range (10,-1,-1):
    #imprimindo o contador
    print(cont)
    #pausa 1 seg
    sleep(1)

print('{:=^40}'.format(' FELIZ ANO NOVO! 2021!!!'))

