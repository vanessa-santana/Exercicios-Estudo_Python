'''
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso. '''

from time import sleep

primeiro=int(input('Primeiro valor: '))
segundo=int(input('Segundo valor: '))

sair=False
while not sair:
    print ('=-=='*10)
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao=int(input('>>>>>> Qual é a sua opção? '))

    if opcao==5:
        sair=True
    else:
        if opcao==1:
            soma=primeiro+segundo
            print('A soma entre {} e {} é {}'.format(primeiro,segundo,soma))
        elif opcao==2:
            multip=primeiro*segundo
            print('A multiplicação entre {} e {} é {}'.format(primeiro,segundo,multip))
        elif opcao==3:
            if primeiro > segundo:
                maior = primeiro
            else:
                maior = segundo
            print('O maior numero entre {} e {} é {}'.format(primeiro,segundo,maior))
        elif opcao==4:
            primeiro=int(input('Primeiro valor: '))
            segundo=int(input('Segundo valor: '))
        else:
            print('Opção Invalida. Tente Novamente')   
       

print('Finalizando o programa!...')
print ('=-=='*10)
sleep(1)
print('Encerrado')