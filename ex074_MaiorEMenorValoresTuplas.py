#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.


from random import randint

num=(randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))

print('Sorteado os valores:')
for n in num:
    print(f'{n} ',end='')

print(f'\nMaior numero é: {max(num)}')
print(f'Menor numero é: {min(num)}')