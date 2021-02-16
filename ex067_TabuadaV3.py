''' Faça um programa que mostre a tabuada de vários números, um de cada vez, 
para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. '''

while True:
    print('-'*30)
    num=int(input('Tabuada de qual valor? '))
    print('-'*30)

    if num < 0:
        print('Programa de Tabuada Encerrado!')
        break

    for i in range(1,11):
         print(f'{i:2} x {num:2} = {(i*num):2}')
