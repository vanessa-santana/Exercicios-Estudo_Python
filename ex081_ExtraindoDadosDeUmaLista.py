'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista. '''

listaNum=[]
while True:
    #num=int(input('Digite um numero: '))
    listaNum.append(int(input('Digite um numero: ')))

    resp=' '
    while resp not in 'SN':
        resp=str(input('Deseja Continuar? [S/N]: ')).upper().strip()[0]

    if resp =='N':
        break

listaNum.sort(reverse=True)
print(f'Digitado {len(listaNum)} elementos')
print(f'Os valores em ordem decrescente : {listaNum}')
if 5 in listaNum:
    print('Valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado na lista')
