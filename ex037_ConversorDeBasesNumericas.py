#Escreva um programa em Python que leia um número inteiro qualquer e 
# peça para o usuário escolher qual será a base de conversão:
#1 para binário, 2 para octal e 3 para hexadecimal.

number=int(input('Digite um numero: '))
print(''' Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''') 
opcao=int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(number,bin(number)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(number,oct(number)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(number,hex(number)[2:]))
else:
    print('Código Inválido. Tente novamente!')