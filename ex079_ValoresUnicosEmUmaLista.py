'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
 Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, 
 em ordem crescente. '''

listaNum=list()

while True:
    num=int(input('Digite um valor: '))

    if num not in listaNum:
        listaNum.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor Duplicado. Não adicionado...')

    resp=' '
    while resp not in 'SN':
        resp=str(input('Deseja continuar [S/N]: ')).upper().strip()[0]

    if resp=='S':
        print('-'*30)

    if resp=='N':
        break

print('-='*60)
listaNum.sort() #coloca em ordem crescente
print(f'Os numeros Digitados e em ordem crescebte são: {listaNum}')