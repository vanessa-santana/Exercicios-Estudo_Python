#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.

listagem = ('Lapis', 1.75,
            'Borracha', 2,
            'Caderno', 15,
            'Estojo', 25,
            'Transferidor', 4.28,
            'Compasso', 9.99,
            'Mochila', 128.32,
            'Canetas', 22.30,
            'Livro', 33.98)
#print(listagem)
print('-'*40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('-'*40)
for pos in range(0,len(listagem)):
    if pos % 2==0:
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'*40)