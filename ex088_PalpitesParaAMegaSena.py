'''aça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
cadastrando tudo em uma lista composta. '''

from random import randint
from time import sleep

print('-'*40)
print(f'{"PALPITES NA MEGA SENA":^40}')
print('-'*40)

quantidade=int(input('Quantos jogos para sorteio?: '))

lista=list()
jogos=list()

total=1
while total <=quantidade:
    contador=0
    while True:
        num=randint(1,60)
        if num not in lista:
            lista.append(num)
            contador+=1
        if contador >=6:
            break
    lista.sort()
    jogos.append(lista[:]) #copia da lista
    lista.clear()
    total+=1

print('-='*3, f'SORTEANDO {quantidade} JOGOS','-='*3)

for indice, listas in enumerate(jogos):
    print(f'Jogo {indice+1:^2}: {listas}')
    sleep(1)
print('-='*5,'< Boa Sorte! >','-='*5) 
