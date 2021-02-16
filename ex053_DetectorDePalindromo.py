# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase=str(input('Digite uma frase: ')).strip().upper()

#transforma em lista 
lista=frase.split() 
#em lista, faz join para agrupar sem os espaços
junto=''.join(lista)

inverso=''
#for para inverter
for letra in range (len(junto)-1,-1,-1):
    inverso+=junto[letra]

print('O inverso de {} é {}'.format(junto,inverso))

if junto==inverso:
    print('É um Palindromo')
else:
    print('Não é um Palindromo')