#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

precoProd=float(input('Digite o valor do produto: '))

novoPreco=precoProd-(precoProd*(5/100))

print('O valor do produto de R$ {:.2f} com 5% de desconto é de R$ {:.2f}'.format(precoProd,novoPreco) )