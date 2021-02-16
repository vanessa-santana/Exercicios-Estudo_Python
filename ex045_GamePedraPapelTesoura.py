# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

itens=['Pedra','Papel','Tesoura']
computador=randint(0,2)
# print('O computador escolheu {}'.format(itens[computador])) #modo teste variavel computador e lista

print(''' Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
''')
jogador=int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

print('-='*11)
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))
print('-='*11)

if computador ==0:
    if jogador==0: 
        print('EMPATE')
    elif jogador==1:
        print('JOGADOR VENCE')
    elif jogador==2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada Inválida')

elif computador==1:
    if jogador==0: 
        print('COMPUTADOR VENCE')
    elif jogador==1:
        print('EMPATE')
    elif jogador==2:
        print('JOGADOR VENCE')
    else:
        print('Jogada Inválida')

elif computador==2:
    if jogador==0: 
        print('JOGADOR VENCE')
    elif jogador==1:
        print('COMPUTADOR VENCE')
    elif jogador==2:
        print('EMPATE')
    else:
        print('Jogada Inválida')
