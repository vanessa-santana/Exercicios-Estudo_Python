#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('-=-' *20)
print('Analise de Emprestimo')
print('-=-' *20)

valorCasa=float(input('Qual valor da casa? R$ '))
salario=float(input('Qual o salario? R$ '))
qtdAnos=int(input('Quantos anos ira pagar? '))

prestacaoMensal=valorCasa/(qtdAnos*12)
salario30 = salario*0.30
if prestacaoMensal > salario30:
    print('NEGADO! Valor da prestação de R${:.2F} é maior que o valor de 30% do salario, que é R${:.2f}'.format(prestacaoMensal,salario30))
else:
    print('Aprovado')
