''' Crie um programa onde o usuário possa digitar sete valores numéricos e 
cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, 
mostre os valores pares e ímpares em ordem crescente. '''

#possivel declarar uma lista contendo duas listas
num=[[],[]]
valor=0
for i in range (1,8):
    valor=int(input(f'Digite o {i}º valor: '))

    if valor %2==0:
        num[0].append(valor)
    else:
        num[1].append(valor)

print('-='*30)
print(f'A lista: {num}')
num[0].sort()
num[1].sort()
print(f'A lista par ordenada: {num[0]}')
print(f'A lista impar ordenada: {num[1]}')