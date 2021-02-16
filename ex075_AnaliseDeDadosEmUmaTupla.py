'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares. '''

tupla =(int(input('Digite o primeiro numero: ')),
        int(input('Digite o segundo numero: ')),
        int(input('Digite o terceiro numero: ')),
        int(input('Digite o quarto numero: ')))


print(f'Digitou os numeros: {tupla}')
print(f'Num 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'Num 3 apareceu na {tupla.index(3)+1}ª posição')
else:
    print('O numero 3 não foi digitado em nenhuma posição')
print('Os valores pares foram: ',end='')
for n in tupla:
    if n %2==0:
        print(n,end=' ')
