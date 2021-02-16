'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves. '''

listaPrincipal=[]
listaTemporario=[]
maior=menor=0
while True:
    listaTemporario.append(str(input('Nome: ')))
    listaTemporario.append(float(input('Peso: ')))
    
    #antes de limpar a lista temporaria, sera feita a analise de maior e menor (peso)
    if len(listaPrincipal)==0:
        maior=menor=listaTemporario[1]
    else:
        if listaTemporario[1]>maior:
            maior=listaTemporario[1]
        if listaTemporario[1]<menor:
            menor=listaTemporario[1]
    listaPrincipal.append(listaTemporario[:]) #Cria uma copia
    #como adicionara repetidamente as inclusões na impressão, precisa limpar o temporario para receber a prox variavel
    listaTemporario.clear()

    resp=' '
    while resp not in 'SN':
        resp=str(input('Deseja Continuar? [S/N]: ')).upper().strip()[0]

    if resp =='N':
        break

print('-'*30)
print(f'Os dados foram {listaPrincipal}')
print(f'Quantidade de pessoas cadastradas: {len(listaPrincipal)}')
print(f'O maior peso foi de {maior} kilos, nomes: ',end='')
for pessoa in listaPrincipal:
    if pessoa[1] == maior:
        print(f'[{pessoa[0]}] ',end='')
print()
print(f'O menor peso foi de {menor} kilos, nomes: ',end='')
for pessoa in listaPrincipal:
    if pessoa[1]==menor:
        print(f'[{pessoa[0]}] ',end='')




