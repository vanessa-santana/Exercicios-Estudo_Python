''' Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer. '''

from random import randint

computador=randint(0,10)


print('''
Sou seu computador...
Acabei de pensar em um numero entre 0 e 10.
Será que você consegue adivinhar qual foi?? ''')


acertou=False
tentativas=0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    tentativas+=1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente novamente.')
        elif jogador > computador:
            print('Menos...Tente novamente.')

print('Acertou com {} tentativas. Parabens'.format(tentativas)) 


''' Outro modo 

palpite=int(input('Qual o seu palpite? '))

cont=0
while palpite != computador:
    if palpite != computador:
        if palpite < computador:
            print('Mais...Tente novamente.')
            palpite=int(input('Qual o seu palpite? '))
            cont+=1
        else:
            print('Menos...Tente novamente.')
            palpite=int(input('Qual o seu palpite? '))
            cont+=1

print('Acertou com {} tentativas. Parabéns'.format(cont)) 
 '''
