#Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 
from random import randint

while True:
    jogador=int(input("Diga um valor:"))
    computador=randint(0,11)
    total = jogador + computador
    tipo= ' '

    while tipo not in 'PI':
        tipo=str(input('Par ou Impar? (P/I):')).strip()[0].upper()
    print(f'Voce jogou {jogador} e o computador {computador}. Total de {total}')
    
    if tipo =='P':
        if total %2==0:
            print('Você venceu')
            v+=1
        else:
            print('Voce perdeu')
            break
    elif tipo == 'I':
        if total %2==1:
            print('Você venceu')
            v+=1
        else:
            print('Voce perdeu')
            break
    print('Vamos jogar novamente...')
print(f'Game Over! Voce perdeu {v} vezes.')