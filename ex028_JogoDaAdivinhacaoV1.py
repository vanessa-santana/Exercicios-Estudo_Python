#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

escolhaComp= randint(0,5)
#print('Pensei no num {}'.format(escolhaComp))

print('-=-' *20)
print('Pensei em um numero entre 0 e 5. Tente Adivinhar...')
print('-=-' *20)

jogador=int(input("Em qual numero eu pensei: "))
print('PROCESSANDO...')
sleep(2)
if jogador == escolhaComp:
    print('Parabens, vc conseguiu me vencer! Pensei no num {}'.format(jogador))
else:
    print('Errrroooouu, pensei no num {} e não no num {}'.format(escolhaComp,jogador))


