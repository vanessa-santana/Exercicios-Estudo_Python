''' Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores. '''

continuar=''
soma = contador= menor = maior=0

while continuar not in 'Nn':
    number=int(input('Digite um numero: '))
    continuar=str(input('Quer Continuar?[S/N]: ')).upper().strip()[0]
    soma+=number
    contador+=1
    if contador ==1:
        maior = menor = number
    else:
        if number > maior:
            maior = number
        if number < menor:
            menor = number
media=soma/contador
print('Digitou {} numeros e a media foi {}'.format(contador,media))
print('O maior valor foi {} e o menor foi {}'.format(maior,menor))
print('Fim')


