'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não.
No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''

total = qtdProd1000 = menorPreco = 0
nomeMenor=' '
while True:
    produto=str(input('Digite o nome do produto: ')).strip().title()
    preco=float(input('Digite o valor do produto R$: '))
    
    total+=preco
    menorPreco=preco
    nomeMenor=produto

    if preco > 1000:
        qtdProd1000+=1
    
    if preco < menorPreco:
        menorPreco=preco 
        nomeMenor=produto

    resp=' '
    while resp not in 'SN':
        resp=str(input('Quer continuar? [S/N]: ')).strip()[0].upper()

    if resp =='N':
        break
print ('------------------- FIM DO PROGRAMA -------------------')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {qtdProd1000} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {nomeMenor} que custa R${menorPreco:.2f}')