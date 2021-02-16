#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 

listaNum =[]
maior=menor=posicao=0
for c in range(0,5):
    listaNum.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c==0:
        maior=menor=listaNum[0]
        posicao=c
    else:
        if listaNum[c] > maior:
            maior=listaNum[c]

        if listaNum[c] < menor:
            menor=listaNum[c]


print('-'*30)
print(f'Digitado os valores: {listaNum}')
print(f'Maior numero digitado foi o {maior} nas posições ',end='')
#Varrer a lista para achar a posição usando o enumerate
for indice, valor in enumerate(listaNum):
    if valor == maior:
        print(f'{indice}...',end='')
print()

print(f'Menor numero digitado foi o {menor} nas posições ',end='')
for indice, valor in enumerate(listaNum):
    if valor == menor:
        print(f'{indice}...',end='')
print()
