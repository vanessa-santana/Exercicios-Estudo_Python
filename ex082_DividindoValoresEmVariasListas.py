''' Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, 
respectivamente. Ao final, mostre o conteúdo das três listas geradas.

listaTotal=[]
listaNumPar=[]
listaNumImpar=[]
while True:
    num=int(input('Digite um numero: '))

    listaTotal.append(num)

    if num % 2==0:
        listaNumPar.append(num)
    else:
        listaNumImpar.append(num)

    resp=' '
    while resp not in 'SN':
        resp=str(input('Deseja Continuar? [S/N] ')).upper().strip()[0]
    
    if resp=='N':
        break

print(f'A lista completa: {listaTotal}')
print(f'A lista Par: {listaNumPar}')
print(f'A lista Impar: {listaNumImpar}') '''

#Modo 2:

num=list()
listaNumPar=list()
listaNumImpar=list()

while True:
    num.append(int(input('Digite um numero: ')))

    resp=' '
    while resp not in 'SN':
        resp=str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    
    if resp=='N':
        break

for i, v in enumerate(num):
    if v % 2 ==0:
        listaNumPar.append(v)
    elif v % 2==1:
        listaNumImpar.append(v)
print('-='*30)
print(f'A lista completa: {num}')
print(f'A lista Par: {listaNumPar}')
print(f'A lista Impar: {listaNumImpar}')
