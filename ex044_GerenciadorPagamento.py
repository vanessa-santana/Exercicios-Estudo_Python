''' Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal 
e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros '''

print('{:=^40}'.format(' Lojas '))

preco=float(input('Preço das Compras: R$ '))
print(''' Formas de Pagamento
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao=int(input('Qual a opção? '))
if opcao==1:
    novoPreco=preco-(preco*0.1)
    print('Sua compra de R${:.2f} terá desconto de 10%. Total a pagar R${:.2f}'.format(preco,novoPreco))
elif opcao==2:
    novoPreco=preco-(preco*0.05)
    print('Sua compra de R${:.2f} terá desconto de 5%. Total a pagar R${:.2f}'.format(preco,novoPreco))
elif opcao==3:
    novoPreco=preco/2
    print('Sua compra de R${:.2f} será parcelada em 2x. Valor por parcela R${:.2f}'.format(preco,novoPreco))
elif opcao==4:
    parc=int(input('Quantas parcelas? '))
    novoPreco=preco*1.2
    valorParc=novoPreco/parc
    print('Sua compra sera parcelado em {}x de R${:.2f} com juros'.format(parc,valorParc))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco,novoPreco))
else:
    print('Opção Invalida. Tente novamente')
    